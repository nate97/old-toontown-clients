# File: F (Python 2.2)

import types
import libpandafx
import libpandafxDowncasts
import libpanda
import libpandaDowncasts
import libpandaexpress
import libpandaexpressDowncasts
from direct.ffi import FFIExternalObject
import Lens

class FisheyeLens(Lens.Lens, FFIExternalObject.FFIExternalObject):
    __CModuleDowncasts__ = [
        libpandafxDowncasts,
        libpandaDowncasts,
        libpandaexpressDowncasts]
    
    def __init__(self, *_args):
        FFIExternalObject.FFIExternalObject.__init__(self)
        if len(_args) == 1 and _args[0] == None:
            return None
        
        self.constructor(*_args)

    
    def constructor(self):
        self.this = libpandafx._inP1uO41U_J()
        self.userManagesMemory = 1

    
    def __del__(self):
        if self.userManagesMemory and self.this != 0:
            self.destructor()
        

    
    def destructor(self):
        if libpandafx and libpandafx._inP1uO4Lj5t:
            libpandafx._inP1uO4Lj5t(self.this)
        

    
    def getClassType():
        returnValue = libpandafx._inP1uO4JEaS()
        import TypeHandle
        returnObject = TypeHandle.TypeHandle(None)
        returnObject.this = returnValue
        if returnObject.this == 0:
            return None
        
        returnObject.userManagesMemory = 1
        return returnObject

    getClassType = staticmethod(getClassType)

