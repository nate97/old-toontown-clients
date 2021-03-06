# File: C (Python 2.2)

import DirectNotifyGlobal
import FSM
import State
import Place
import Elevator
import ToontownGlobals
from PandaModules import *

class CogHQLobby(Place.Place):
    notify = DirectNotifyGlobal.directNotify.newCategory('CogHQLobby')
    
    def __init__(self, hood, parentFSM, doneEvent):
        Place.Place.__init__(self, hood, doneEvent)
        self.parentFSM = parentFSM
        self.elevatorDoneEvent = 'elevatorDone'
        self.fsm = FSM.FSM('CogHQLobby', [
            State.State('start', self.enterStart, self.exitStart, [
                'walk',
                'tunnelIn',
                'teleportIn',
                'doorIn']),
            State.State('walk', self.enterWalk, self.exitWalk, [
                'elevator',
                'DFA',
                'doorOut']),
            State.State('doorIn', self.enterDoorIn, self.exitDoorIn, [
                'walk']),
            State.State('doorOut', self.enterDoorOut, self.exitDoorOut, [
                'walk']),
            State.State('teleportIn', self.enterTeleportIn, self.exitTeleportIn, [
                'walk']),
            State.State('elevator', self.enterElevator, self.exitElevator, [
                'walk']),
            State.State('DFA', self.enterDFA, self.exitDFA, [
                'DFAReject']),
            State.State('DFAReject', self.enterDFAReject, self.exitDFAReject, [
                'walk']),
            State.State('final', self.enterFinal, self.exitFinal, [
                'start'])], 'start', 'final')

    
    def load(self):
        self.parentFSM.getStateNamed('cogHQLobby').addChild(self.fsm)
        Place.Place.load(self)

    
    def unload(self):
        self.parentFSM.getStateNamed('cogHQLobby').removeChild(self.fsm)
        Place.Place.unload(self)

    
    def enter(self, requestStatus):
        self.zoneId = requestStatus['zoneId']
        Place.Place.enter(self)
        self.fsm.enterInitialState()
        base.playMusic(self.loader.music, looping = 1, volume = 0.80000000000000004)
        self.loader.geom.reparentTo(render)
        self.accept('doorDoneEvent', self.handleDoorDoneEvent)
        self.accept('DistributedDoor_doorTrigger', self.handleDoorTrigger)
        NametagGlobals.setMasterArrowsOn(1)
        how = requestStatus['how']
        self.fsm.request(how, [
            requestStatus])

    
    def exit(self):
        self.fsm.requestFinalState()
        self.ignoreAll()
        self.loader.music.stop()
        if self.loader.geom != None:
            self.loader.geom.reparentTo(hidden)
        
        Place.Place.exit(self)

    
    def enterWalk(self, teleportIn = 0):
        Place.Place.enterWalk(self, teleportIn)
        self.ignore('teleportQuery')
        toonbase.localToon.setTeleportAvailable(0)

    
    def enterElevator(self, distElevator):
        self.accept(self.elevatorDoneEvent, self.handleElevatorDone)
        self.elevator = Elevator.Elevator(self.fsm.getStateNamed('elevator'), self.elevatorDoneEvent, distElevator)
        self.elevator.load()
        self.elevator.enter()

    
    def exitElevator(self):
        self.ignore(self.elevatorDoneEvent)
        self.elevator.unload()
        self.elevator.exit()
        del self.elevator

    
    def detectedElevatorCollision(self, distElevator):
        self.fsm.request('elevator', [
            distElevator])

    
    def handleElevatorDone(self, doneStatus):
        self.notify.debug('handling elevator done event')
        where = doneStatus['where']
        if where == 'reject':
            self.fsm.request('walk')
        elif where == 'exit':
            self.fsm.request('walk')
        elif where == 'cogHQBossBattle':
            self.doneStatus = doneStatus
            messenger.send(self.doneEvent)
        else:
            self.notify.error('Unknown mode: ' + where + ' in handleElevatorDone')

    
    def enterTeleportIn(self, requestStatus):
        toonbase.localToon.setPosHpr(render, 0, 0, 0, 0, 0, 0)
        Place.Place.enterTeleportIn(self, requestStatus)


