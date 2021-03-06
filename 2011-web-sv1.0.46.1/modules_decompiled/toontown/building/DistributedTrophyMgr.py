# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\building\DistributedTrophyMgr.py
from direct.distributed import DistributedObject
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import TTLocalizer

class DistributedTrophyMgr(DistributedObject.DistributedObject):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('DistributedTrophyMgr')
    neverDisable = 1

    def __init__(self, cr):
        DistributedObject.DistributedObject.__init__(self, cr)

    def generate(self):
        if base.cr.trophyManager != None:
            base.cr.trophyManager.delete()
        base.cr.trophyManager = self
        DistributedObject.DistributedObject.generate(self)
        return

    def disable(self):
        base.cr.trophyManager = None
        DistributedObject.DistributedObject.disable(self)
        return

    def delete(self):
        base.cr.trophyManager = None
        DistributedObject.DistributedObject.delete(self)
        return

    def d_requestTrophyScore(self):
        self.sendUpdate('requestTrophyScore', [])