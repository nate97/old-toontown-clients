# File: M (Python 2.2)

from PandaObject import *
from ToontownGlobals import *
import DirectNotifyGlobal

class MazeTreasure(PandaObject):
    RADIUS = 0.69999999999999996
    
    def __init__(self, model, pos, serialNum, gameId):
        self.serialNum = serialNum
        self.nodePath = model.copyTo(render)
        self.nodePath.setPos(pos[0], pos[1], 1.0)
        self.sphereName = 'treasureSphere%s-%s' % (gameId, self.serialNum)
        self.collSphere = CollisionSphere(0, 0, 0, self.RADIUS)
        self.collSphere.setTangible(0)
        self.collNode = CollisionNode(self.sphereName)
        self.collNode.setIntoCollideMask(WallBitmask)
        self.collNode.addSolid(self.collSphere)
        self.collNodePath = self.nodePath.attachNewNode(self.collNode)
        self.collNodePath.hide()
        self.accept('enter' + self.sphereName, self._MazeTreasure__handleEnterSphere)
        self.nodePath.flattenLight()

    
    def destroy(self):
        self.ignoreAll()
        self.nodePath.removeNode()
        del self.nodePath
        del self.collSphere
        self.collNodePath.removeNode()
        del self.collNodePath
        del self.collNode

    
    def _MazeTreasure__handleEnterSphere(self, collEntry):
        self.ignoreAll()
        messenger.send('MazeTreasureGrabbed', [
            self.serialNum])

    
    def showGrab(self):
        self.nodePath.reparentTo(hidden)
        self.collNode.setIntoCollideMask(BitMask32(0))


