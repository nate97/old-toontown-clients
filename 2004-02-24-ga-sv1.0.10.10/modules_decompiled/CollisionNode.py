# File: C (Python 2.2)

import types
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
import FFIExternalObject
import PandaNode

class CollisionNode(PandaNode.PandaNode, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        apply(self.constructor, _args)

    
    def constructor(self, name):
        self.this = libpanda._inPHwcay_1r(name)
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def getClassType():
        returnValue = libpanda._inPHwcacyU3()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)
    
    def setCollideMask(self, mask):
        returnValue = libpanda._inPHwcacMog(self.this, mask.this)
        return returnValue

    
    def setFromCollideMask(self, mask):
        returnValue = libpanda._inPHwca5b7f(self.this, mask.this)
        return returnValue

    
    def setIntoCollideMask(self, mask):
        returnValue = libpanda._inPHwcanRag(self.this, mask.this)
        return returnValue

    
    def getFromCollideMask(self):
        returnValue = libpanda._inPHwcaY8vI(self.this)
        import BitMask32
        returnObject = BitMask32.BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def getIntoCollideMask(self):
        returnValue = libpanda._inPHwcax1PJ(self.this)
        import BitMask32
        returnObject = BitMask32.BitMask32(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    
    def setCollideGeom(self, flag):
        returnValue = libpanda._inPHwcaO_9H(self.this, flag)
        return returnValue

    
    def getCollideGeom(self):
        returnValue = libpanda._inPHwca6KPh(self.this)
        return returnValue

    
    def clearSolids(self):
        returnValue = libpanda._inPHwca7zaG(self.this)
        return returnValue

    
    def getNumSolids(self):
        returnValue = libpanda._inPHwcarYJk(self.this)
        return returnValue

    
    def getSolid(self, n):
        returnValue = libpanda._inPHwcajUdZ(self.this, n)
        import CollisionSolid
        returnObject = CollisionSolid.CollisionSolid(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject.setPointer()

    
    def setSolid(self, n, solid):
        returnValue = libpanda._inPHwcaZq_i(self.this, n, solid.this)
        return returnValue

    
    def removeSolid(self, n):
        returnValue = libpanda._inPHwcaT94l(self.this, n)
        return returnValue

    
    def addSolid(self, solid):
        returnValue = libpanda._inPHwca4WYW(self.this, solid.this)
        return returnValue


