# File: D (Python 2.2)

from direct.showbase.ShowBaseGlobal import *
from direct.showbase.PandaObject import *
from direct.distributed.ClockDelta import *
from direct.interval.IntervalGlobal import *
from direct.distributed import DistributedObject
from direct.fsm import ClassicFSM
from direct.fsm import State
from pandac import NodePath
from direct.directutil import Mopath
from toontown.toonbase import ToontownGlobals

class DistributedBoat(DistributedObject.DistributedObject):
    
    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)
        self.eastWestMopath = Mopath.Mopath()
        self.westEastMopath = Mopath.Mopath()
        self.fsm = ClassicFSM.ClassicFSM('DistributedBoat', [
            State.State('off', self.enterOff, self.exitOff, [
                'DockedEast',
                'SailingWest',
                'DockedWest',
                'SailingEast']),
            State.State('DockedEast', self.enterDockedEast, self.exitDockedEast, [
                'SailingWest',
                'SailingEast',
                'DockedWest']),
            State.State('SailingWest', self.enterSailingWest, self.exitSailingWest, [
                'DockedWest',
                'SailingEast',
                'DockedEast']),
            State.State('DockedWest', self.enterDockedWest, self.exitDockedWest, [
                'SailingEast',
                'SailingWest',
                'DockedEast']),
            State.State('SailingEast', self.enterSailingEast, self.exitSailingEast, [
                'DockedEast',
                'DockedWest',
                'SailingWest'])], 'off', 'off')
        self.fsm.enterInitialState()

    
    def generate(self):
        self.boat = base.cr.playGame.hood.loader.boat
        base.cr.parentMgr.registerParent(ToontownGlobals.SPDonaldsBoat, self.boat)
        self.setupTracks()
        self.accept('enterdonalds_boat_floor', self._DistributedBoat__handleOnFloor)
        self.accept('exitdonalds_boat_floor', self._DistributedBoat__handleOffFloor)

    
    def setupTracks(self):
        boat = self.boat
        boat.unstash()
        dockSound = self.cr.playGame.hood.loader.dockSound
        foghornSound = self.cr.playGame.hood.loader.foghornSound
        bellSound = self.cr.playGame.hood.loader.bellSound
        self.eastWestMopath.loadFile('phase_6/paths/dd-e-w')
        ewBoatTrack = ParallelEndTogether(Parallel(MopathInterval(self.eastWestMopath, boat), SoundInterval(bellSound, node = boat)), SoundInterval(foghornSound, node = boat), name = 'ew-boat')
        self.westEastMopath.loadFile('phase_6/paths/dd-w-e')
        weBoatTrack = ParallelEndTogether(Parallel(MopathInterval(self.westEastMopath, boat), SoundInterval(bellSound, node = boat)), SoundInterval(foghornSound, node = boat), name = 'we-boat')
        PIER_TIME = 5.0
        eastPier = self.cr.playGame.hood.loader.geom.find('**/east_pier')
        ePierHpr = VBase3(90, -44.260100000000001, 0)
        ePierTargetHpr = VBase3(90, 0.25, 0)
        westPier = self.cr.playGame.hood.loader.geom.find('**/west_pier')
        wPierHpr = VBase3(-90.119100000000003, -110, 66.215999999999994)
        wPierTargetHpr = VBase3(-90.119100000000003, -66, 66.215999999999994)
        ePierDownTrack = Parallel(LerpHprInterval(eastPier, PIER_TIME, ePierHpr, ePierTargetHpr), SoundInterval(dockSound, node = eastPier), name = 'e-pier-down')
        ePierUpTrack = Parallel(LerpHprInterval(eastPier, PIER_TIME, ePierTargetHpr, ePierHpr), SoundInterval(dockSound, node = eastPier), name = 'e-pier-up')
        wPierDownTrack = Parallel(LerpHprInterval(westPier, PIER_TIME, wPierHpr, wPierTargetHpr), SoundInterval(dockSound, node = westPier), name = 'w-pier-down')
        wPierUpTrack = Parallel(LerpHprInterval(westPier, PIER_TIME, wPierTargetHpr, wPierHpr), SoundInterval(dockSound, node = westPier), name = 'w-pier-up')
        self.ewTrack = ParallelEndTogether(Parallel(ewBoatTrack, ePierDownTrack), wPierUpTrack, name = 'ew-track')
        self.weTrack = ParallelEndTogether(Parallel(weBoatTrack, wPierDownTrack), ePierUpTrack, name = 'we-track')

    
    def disable(self):
        base.cr.parentMgr.unregisterParent(ToontownGlobals.SPDonaldsBoat)
        self.ignore('enterdonalds_boat_floor')
        self.ignore('exitdonalds_boat_floor')
        self.fsm.request('off')
        DistributedObject.DistributedObject.disable(self)
        self.ewTrack.finish()
        self.weTrack.finish()

    
    def delete(self):
        self.eastWestMopath.reset()
        self.westEastMopath.reset()
        del self.eastWestMopath
        del self.westEastMopath
        del self.ewTrack
        del self.weTrack
        del self.fsm
        DistributedObject.DistributedObject.delete(self)

    
    def setState(self, state, timestamp):
        self.fsm.request(state, [
            globalClockDelta.localElapsedTime(timestamp)])

    
    def _DistributedBoat__handleOnFloor(self, collEntry):
        self.cr.playGame.getPlace().activityFsm.request('OnBoat')

    
    def _DistributedBoat__handleOffFloor(self, collEntry):
        self.cr.playGame.getPlace().activityFsm.request('off')

    
    def enterOff(self):
        return None

    
    def exitOff(self):
        return None

    
    def enterDockedEast(self, ts):
        self.weTrack.finish()
        return None

    
    def exitDockedEast(self):
        return None

    
    def enterSailingWest(self, ts):
        self.ewTrack.start(ts)

    
    def exitSailingWest(self):
        self.ewTrack.finish()

    
    def enterDockedWest(self, ts):
        self.ewTrack.finish()
        return None

    
    def exitDockedWest(self):
        return None

    
    def enterSailingEast(self, ts):
        self.weTrack.start(ts)

    
    def exitSailingEast(self):
        self.weTrack.finish()
        return None


