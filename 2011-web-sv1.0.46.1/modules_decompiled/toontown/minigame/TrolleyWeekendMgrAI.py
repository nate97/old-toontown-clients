# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\minigame\TrolleyWeekendMgrAI.py
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals, TTLocalizer
from toontown.ai import HolidayBaseAI

class TrolleyWeekendMgrAI(HolidayBaseAI.HolidayBaseAI):
    __module__ = __name__
    notify = DirectNotifyGlobal.directNotify.newCategory('TrolleyWeekendMgrAI')
    PostName = 'TrolleyWeekend'
    StartStopMsg = 'TrolleyWeekendStartStop'

    def __init__(self, air, holidayId):
        HolidayBaseAI.HolidayBaseAI.__init__(self, air, holidayId)

    def start(self):
        bboard.post(TrolleyWeekendMgrAI.PostName, True)
        simbase.air.newsManager.trolleyWeekendStart()
        messenger.send(TrolleyWeekendMgrAI.StartStopMsg)

    def stop(self):
        bboard.remove(TrolleyWeekendMgrAI.PostName)
        simbase.air.newsManager.trolleyWeekendEnd()
        messenger.send(TrolleyWeekendMgrAI.StartStopMsg)