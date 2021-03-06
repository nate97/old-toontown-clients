# File: P (Python 2.2)

from ShowBaseGlobal import *
from ToonBaseGlobal import *
import DirectNotifyGlobal
import PandaObject
import StateData
import FSM
import State
from ToontownMsgTypes import *
from ToontownGlobals import *
import ToontownGlobals
import TTHood
import DDHood
import MMHood
import BRHood
import DGHood
import DLHood
import SellbotHQ
import TutorialHood
import TaskManagerGlobal
import QuietZoneState
import ZoneUtil
import EstateHood
import Localizer

class PlayGame(PandaObject.PandaObject, StateData.StateData):
    notify = DirectNotifyGlobal.directNotify.newCategory('PlayGame')
    notify.setDebug(1)
    
    def __init__(self, parentFSM, doneEvent):
        StateData.StateData.__init__(self, doneEvent)
        self.place = None
        self.fsm = FSM.FSM('PlayGame', [
            State.State('start', self.enterStart, self.exitStart, [
                'quietZone']),
            State.State('quietZone', self.enterQuietZone, self.exitQuietZone, [
                'TTHood',
                'DDHood',
                'BRHood',
                'MMHood',
                'DGHood',
                'DLHood',
                'SellbotHQ',
                'TutorialHood',
                'EstateHood']),
            State.State('TTHood', self.enterTTHood, self.exitTTHood, [
                'quietZone']),
            State.State('DDHood', self.enterDDHood, self.exitDDHood, [
                'quietZone']),
            State.State('BRHood', self.enterBRHood, self.exitBRHood, [
                'quietZone']),
            State.State('MMHood', self.enterMMHood, self.exitMMHood, [
                'quietZone']),
            State.State('DGHood', self.enterDGHood, self.exitDGHood, [
                'quietZone']),
            State.State('DLHood', self.enterDLHood, self.exitDLHood, [
                'quietZone']),
            State.State('SellbotHQ', self.enterSellbotHQ, self.exitSellbotHQ, [
                'quietZone']),
            State.State('TutorialHood', self.enterTutorialHood, self.exitTutorialHood, [
                'quietZone']),
            State.State('EstateHood', self.enterEstateHood, self.exitEstateHood, [
                'quietZone'])], 'start', 'start')
        self.fsm.enterInitialState()
        self.parentFSM = parentFSM
        self.parentFSM.getStateNamed('playGame').addChild(self.fsm)
        self.hoodDoneEvent = 'hoodDone'
        self.hood = None

    
    def enter(self, hoodId, zoneId, avId):
        if hoodId == Tutorial:
            loaderName = 'townLoader'
            whereName = 'toonInterior'
        elif hoodId == MyEstate:
            self.getEstateZoneAndGoHome(avId, zoneId)
            return None
        else:
            loaderName = ZoneUtil.getLoaderName(zoneId)
            whereName = ZoneUtil.getToonWhereName(zoneId)
        self.fsm.request('quietZone', [
            {
                'loader': loaderName,
                'where': whereName,
                'how': 'teleportIn',
                'hoodId': hoodId,
                'zoneId': zoneId,
                'shardId': None,
                'avId': avId }])

    
    def exit(self):
        pass

    
    def load(self):
        pass

    
    def loadDnaStoreTutorial(self):
        self.dnaStore = DNAStorage()
        loader.loadDNAFile(self.dnaStore, 'phase_3.5/dna/storage_tutorial.dna')
        loader.loadDNAFile(self.dnaStore, 'phase_3.5/dna/storage_interior.dna')

    
    def loadDnaStore(self):
        if not hasattr(self, 'dnaStore'):
            self.dnaStore = DNAStorage()
            loader.loadDNAFile(self.dnaStore, 'phase_4/dna/storage.dna')
            self.dnaStore.storeFont('humanist', ToontownGlobals.getInterfaceFont())
            self.dnaStore.storeFont('mickey', ToontownGlobals.getSignFont())
            self.dnaStore.storeFont('suit', ToontownGlobals.getSuitFont())
            loader.loadDNAFile(self.dnaStore, 'phase_3.5/dna/storage_interior.dna')
        

    
    def unloadDnaStore(self):
        if hasattr(self, 'dnaStore'):
            self.dnaStore.resetNodes()
            self.dnaStore.resetTextures()
            del self.dnaStore
            ModelPool.garbageCollect()
            TexturePool.garbageCollect()
        

    
    def unload(self):
        self.unloadDnaStore()

    
    def enterStart(self):
        pass

    
    def exitStart(self):
        pass

    
    def handleHoodDone(self):
        doneStatus = self.hood.getDoneStatus()
        shardId = doneStatus['shardId']
        if shardId != None:
            self.doneStatus = doneStatus
            messenger.send(self.doneEvent)
            return None
        
        how = doneStatus['how']
        if how in [
            'tunnelIn',
            'teleportIn',
            'doorIn',
            'elevatorIn']:
            self.fsm.request('quietZone', [
                doneStatus])
        else:
            self.notify.error('Exited hood with unexpected mode %s' % how)

    
    def enterQuietZone(self, requestStatus):
        self.quietZoneDoneEvent = 'quietZoneDone'
        self.acceptOnce(self.quietZoneDoneEvent, self.handleQuietZoneDone)
        self.acceptOnce('enterWaitForSetZoneResponse', self.handleWaitForSetZoneResponse)
        self.quietZoneStateData = QuietZoneState.QuietZoneState(self.quietZoneDoneEvent)
        self.quietZoneStateData.load()
        self.quietZoneStateData.enter(requestStatus)

    
    def exitQuietZone(self):
        self.ignore(self.quietZoneDoneEvent)
        del self.quietZoneDoneEvent
        self.quietZoneStateData.exit()
        self.quietZoneStateData.unload()
        self.quietZoneStateData = None

    
    def handleWaitForSetZoneResponse(self, requestStatus):
        hoodId = requestStatus['hoodId']
        canonicalHoodId = ZoneUtil.getCanonicalZoneId(hoodId)
        toHoodPhrase = hoodNameMap[canonicalHoodId][0]
        hoodName = hoodNameMap[canonicalHoodId][1]
        zoneId = requestStatus['zoneId']
        loaderName = requestStatus['loader']
        avId = requestStatus.get('avId', -1)
        ownerId = requestStatus.get('ownerId', avId)
        count = hoodCountMap[canonicalHoodId]
        if loaderName == 'safeZoneLoader':
            count += safeZoneCountMap[canonicalHoodId]
        elif loaderName == 'townLoader':
            count += townCountMap[canonicalHoodId]
        
        if not (loader.inBulkBlock):
            if hoodId == MyEstate:
                if avId == -1:
                    loader.beginBulkLoad('hood', Localizer.HeadingToYourEstate, count, 1, Localizer.TIP_GENERAL)
                else:
                    owner = toonbase.tcr.identifyAvatar(ownerId)
                    if owner == None:
                        friend = toonbase.tcr.identifyAvatar(avId)
                        if friend != None:
                            avName = friend.getName()
                            loader.beginBulkLoad('hood', Localizer.HeadingToFriend % avName, count, 1, Localizer.TIP_GENERAL)
                        else:
                            self.notify.warning("we can't perform this teleport")
                            return None
                    else:
                        avName = owner.getName()
                        loader.beginBulkLoad('hood', Localizer.HeadingToEstate % avName, count, 1, Localizer.TIP_GENERAL)
            else:
                loader.beginBulkLoad('hood', Localizer.HeadingToHood % (toHoodPhrase, hoodName), count, 1, Localizer.TIP_GENERAL)
        
        if hoodId == Tutorial:
            self.loadDnaStoreTutorial()
        else:
            self.loadDnaStore()
        hoodClass = self.getHoodClassByNumber(canonicalHoodId)
        self.hood = hoodClass(self.fsm, self.hoodDoneEvent, self.dnaStore, hoodId)
        self.hood.load()
        self.hood.loadLoader(requestStatus)
        loader.endBulkLoad('hood')

    
    def handleQuietZoneDone(self):
        status = toonbase.tcr.handlerArgs
        hoodId = ZoneUtil.getCanonicalZoneId(status['hoodId'])
        hoodState = self.getHoodStateByNumber(hoodId)
        self.fsm.request(hoodState, [
            status])

    
    def enterTTHood(self, requestStatus):
        print 'enterTTHood'
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        self.hood.enter(requestStatus)

    
    def exitTTHood(self):
        print 'exitTTHood'
        self.ignore(self.hoodDoneEvent)
        self.hood.exit()
        self.hood.unload()
        self.hood = None
        toonbase.tcr.cache.flush()

    
    def enterDDHood(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        self.hood.enter(requestStatus)

    
    def exitDDHood(self):
        self.ignore(self.hoodDoneEvent)
        self.hood.exit()
        self.hood.unload()
        self.hood = None
        toonbase.tcr.cache.flush()

    
    def enterMMHood(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        self.hood.enter(requestStatus)

    
    def exitMMHood(self):
        self.ignore(self.hoodDoneEvent)
        self.hood.exit()
        self.hood.unload()
        self.hood = None
        toonbase.tcr.cache.flush()

    
    def enterBRHood(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        self.hood.enter(requestStatus)

    
    def exitBRHood(self):
        self.ignore(self.hoodDoneEvent)
        self.hood.exit()
        self.hood.unload()
        self.hood = None
        toonbase.tcr.cache.flush()

    
    def enterDGHood(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        self.hood.enter(requestStatus)

    
    def exitDGHood(self):
        self.ignore(self.hoodDoneEvent)
        self.hood.exit()
        self.hood.unload()
        self.hood = None
        toonbase.tcr.cache.flush()

    
    def enterDLHood(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        self.hood.enter(requestStatus)

    
    def exitDLHood(self):
        self.ignore(self.hoodDoneEvent)
        self.hood.exit()
        self.hood.unload()
        self.hood = None
        toonbase.tcr.cache.flush()

    
    def enterSellbotHQ(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        self.hood.enter(requestStatus)

    
    def exitSellbotHQ(self):
        self.ignore(self.hoodDoneEvent)
        self.hood.exit()
        self.hood.unload()
        self.hood = None
        toonbase.tcr.cache.flush()

    
    def enterTutorialHood(self, requestStatus):
        messenger.send('toonArrivedTutorial')
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        toonbase.localToon.book.obscureButton(1)
        toonbase.localToon.book.setSafeMode(1)
        toonbase.localToon.laffMeter.obscure(1)
        toonbase.localToon.chatMgr.obscure(1, 1)
        toonbase.localToon.obscureFriendsListButton(1)
        requestStatus['how'] = 'tutorial'
        self.hood.enter(requestStatus)

    
    def exitTutorialHood(self):
        self.unloadDnaStore()
        self.ignore(self.hoodDoneEvent)
        self.hood.exit()
        self.hood.unload()
        self.hood = None
        toonbase.tcr.cache.flush()
        toonbase.localToon.book.obscureButton(0)
        toonbase.localToon.book.setSafeMode(0)
        toonbase.localToon.laffMeter.obscure(0)
        toonbase.localToon.chatMgr.obscure(0, 0)
        toonbase.localToon.obscureFriendsListButton(-1)

    
    def enterEstateHood(self, requestStatus):
        self.accept(self.hoodDoneEvent, self.handleHoodDone)
        self.hood.enter(requestStatus)

    
    def exitEstateHood(self):
        self.ignore(self.hoodDoneEvent)
        self.hood.exit()
        self.hood.unload()
        self.hood = None
        toonbase.tcr.cache.flush()

    
    def getEstateZoneAndGoHome(self, avId, zoneId):
        self.doneStatus = {
            'avId': avId,
            'zoneId': zoneId,
            'hoodId': MyEstate,
            'loader': 'safeZoneLoader',
            'how': 'teleportIn',
            'shardId': None }
        self.acceptOnce('setLocalEstateZone', self.goHome)
        if avId > 0:
            toonbase.tcr.estateMgr.getLocalEstateZone(avId)
        else:
            toonbase.tcr.estateMgr.getLocalEstateZone(toonbase.localToon.getDoId())

    
    def goHome(self, ownerId, zoneId):
        self.notify.debug('goHome ownerId = %s' % ownerId)
        if ownerId > 0 and toonbase.tcr.identifyFriend(ownerId) == None:
            self.doneStatus['failed'] = 1
            taskMgr.remove('goHomeFailed')
            taskMgr.add(self.goHomeFailed, 'goHomeFailed')
            return None
        
        if self.doneStatus['zoneId'] != zoneId:
            self.doneStatus['where'] = 'house'
        else:
            self.doneStatus['where'] = 'estate'
        self.doneStatus['ownerId'] = ownerId
        self.fsm.request('quietZone', [
            self.doneStatus])

    
    def goHomeFailed(self, task):
        self.notify.debug('goHomeFailed')
        failedToVisitAvId = self.doneStatus.get('avId')
        if failedToVisitAvId > 0:
            message = Localizer.EstateTeleportFailedNotFriends % toonbase.tcr.identifyAvatar(failedToVisitAvId).getName()
        else:
            message = Localizer.EstateTeleportFailed
        self.notify.debug('goHomeFailed, why =: %s' % message)
        self.ignore('setLocalEstateZone')
        zoneId = toonbase.localToon.lastHood
        loaderName = ZoneUtil.getLoaderName(zoneId)
        whereName = ZoneUtil.getToonWhereName(zoneId)
        toonbase.localToon.setSystemMessage(0, message)
        self.fsm.request('quietZone', [
            {
                'loader': loaderName,
                'where': whereName,
                'how': 'teleportIn',
                'hoodId': zoneId,
                'zoneId': zoneId,
                'shardId': None }])
        return Task.done

    
    def getCatalogCodes(self, category):
        numCodes = self.dnaStore.getNumCatalogCodes(category)
        codes = []
        for i in range(numCodes):
            codes.append(self.dnaStore.getCatalogCode(category, i))
        
        return codes

    
    def getNodePathList(self, catalogGroup):
        result = []
        codes = self.getCatalogCodes(catalogGroup)
        for code in codes:
            np = self.dnaStore.findNode(code)
            result.append(np)
        
        return result

    
    def getNodePathDict(self, catalogGroup):
        result = { }
        codes = self.getCatalogCodes(catalogGroup)
        for code in codes:
            np = self.dnaStore.findNode(code)
            result[code] = np
        
        return result

    
    def getHoodClassByNumber(self, hoodNumber):
        if hoodNumber == ToontownCentral:
            return TTHood.TTHood
        elif hoodNumber == DonaldsDock:
            return DDHood.DDHood
        elif hoodNumber == TheBrrrgh:
            return BRHood.BRHood
        elif hoodNumber == MinniesMelodyland:
            return MMHood.MMHood
        elif hoodNumber == DaisyGardens:
            return DGHood.DGHood
        elif hoodNumber == DonaldsDreamland:
            return DLHood.DLHood
        elif hoodNumber == Tutorial:
            return TutorialHood.TutorialHood
        elif hoodNumber == MyEstate:
            return EstateHood.EstateHood
        elif hoodNumber == BossbotHQ:
            return BossbotHQ.BossbotHQ
        elif hoodNumber == SellbotHQ:
            return SellbotHQ.SellbotHQ
        elif hoodNumber == CashbotHQ:
            return CashbotHQ.CashbotHQ
        elif hoodNumber == LawbotHQ:
            return LawbotHQ.LawbotHQ
        else:
            self.notify.error('Unknown hoodNumber: ' + `hoodNumber`)

    
    def getHoodStateByNumber(self, hoodNumber):
        if hoodNumber == ToontownCentral:
            return 'TTHood'
        elif hoodNumber == DonaldsDock:
            return 'DDHood'
        elif hoodNumber == TheBrrrgh:
            return 'BRHood'
        elif hoodNumber == MinniesMelodyland:
            return 'MMHood'
        elif hoodNumber == DaisyGardens:
            return 'DGHood'
        elif hoodNumber == DonaldsDreamland:
            return 'DLHood'
        elif hoodNumber == Tutorial:
            return 'TutorialHood'
        elif hoodNumber == MyEstate:
            return 'EstateHood'
        elif hoodNumber == BossbotHQ:
            return 'BossbotHQ'
        elif hoodNumber == SellbotHQ:
            return 'SellbotHQ'
        elif hoodNumber == CashbotHQ:
            return 'CashbotHQ'
        elif hoodNumber == LawbotHQ:
            return 'LawbotHQ'
        else:
            self.notify.error('Unknown hoodNumber: ' + `hoodNumber`)

    
    def setPlace(self, place):
        self.place = place

    
    def getPlace(self):
        return self.place

    
    def getPlaceId(self):
        if self.hood:
            return self.hood.hoodId
        else:
            return None


