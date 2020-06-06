# File: B (Python 2.2)

from pandac.PandaModules import *
from toontown.toon import Toon
from toontown.hood import Place

class BattlePlace(Place.Place):
    
    def __init__(self, loader, doneEvent):
        Place.Place.__init__(self, loader, doneEvent)

    
    def load(self):
        Place.Place.load(self)
        Toon.loadBattleAnims()

    
    def setState(self, state, battleEvent = None):
        if battleEvent:
            self.fsm.request(state, [
                battleEvent])
        else:
            self.fsm.request(state)

    
    def enterWalk(self, flag = 0):
        Place.Place.enterWalk(self, flag)
        self.accept('enterBattle', self.handleBattleEntry)

    
    def exitWalk(self):
        Place.Place.exitWalk(self)
        self.ignore('enterBattle')

    
    def enterWaitForBattle(self):
        base.localAvatar.b_setAnimState('neutral', 1)

    
    def exitWaitForBattle(self):
        pass

    
    def enterBattle(self, event):
        self.loader.music.stop()
        base.playMusic(self.loader.battleMusic, looping = 1, volume = 0.90000000000000002)
        self.enterTownBattle(event)
        if not base.cr.isPaid():
            base.localAvatar.chatMgr.obscure(1, 0)
        
        base.localAvatar.b_setAnimState('off', 1)
        self.accept('teleportQuery', self.handleTeleportQuery)
        base.localAvatar.setTeleportAvailable(1)

    
    def enterTownBattle(self, event):
        self.loader.townBattle.enter(event, self.fsm.getStateNamed('battle'))

    
    def exitBattle(self):
        self.loader.townBattle.exit()
        self.loader.battleMusic.stop()
        base.playMusic(self.loader.music, looping = 1, volume = 0.80000000000000004)
        if not base.cr.isPaid():
            base.localAvatar.chatMgr.obscure(0, 0)
            base.localAvatar.chatMgr.normalButton.show()
        
        base.localAvatar.setTeleportAvailable(0)
        self.ignore('teleportQuery')

    
    def handleBattleEntry(self):
        self.fsm.request('battle')

    
    def enterFallDown(self, extraArgs = []):
        base.localAvatar.laffMeter.start()
        base.localAvatar.b_setAnimState('FallDown', callback = self.handleFallDownDone, extraArgs = extraArgs)

    
    def handleFallDownDone(self):
        base.cr.playGame.getPlace().setState('walk')

    
    def exitFallDown(self):
        base.localAvatar.laffMeter.stop()

    
    def enterSquished(self):
        base.localAvatar.laffMeter.start()
        base.localAvatar.b_setAnimState('Squish')
        taskMgr.doMethodLater(2.0, self.handleSquishDone, base.localAvatar.uniqueName('finishSquishTask'))

    
    def handleSquishDone(self, extraArgs = []):
        base.cr.playGame.getPlace().setState('walk')

    
    def exitSquished(self):
        taskMgr.remove(base.localAvatar.uniqueName('finishSquishTask'))
        base.localAvatar.laffMeter.stop()

    
    def enterZone(self, newZone):
        if isinstance(newZone, CollisionEntry):
            
            try:
                newZoneId = int(newZone.getIntoNode().getName())
            except:
                self.notify.warning('Invalid floor collision node in street: %s' % newZone.getIntoNode().getName())
                return None

        else:
            newZoneId = newZone
        self.doEnterZone(newZoneId)

    
    def doEnterZone(self, newZoneId):
        if newZoneId != self.zoneId:
            if newZoneId != None:
                base.cr.sendSetZoneMsg(newZoneId)
                self.notify.debug('Entering Zone %d' % newZoneId)
            
            self.zoneId = newZoneId
        


