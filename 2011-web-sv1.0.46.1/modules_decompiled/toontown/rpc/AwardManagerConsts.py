# uncompyle6 version 3.7.0
# Python bytecode 2.4 (62061)
# Decompiled from: Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 22:39:24) [MSC v.1916 32 bit (Intel)]
# Embedded file name: C:\Cygwin\home\toonpub\player_1_0_46_qa\toontown\src\rpc\AwardManagerConsts.py
GiveAwardErrors = Enum('Success, WrongGender, NotGiftable, FullMailbox, FullAwardMailbox, AlreadyInMailbox, AlreadyInGiftQueue, AlreadyInOrderedQueue, AlreadyInCloset, AlreadyBeingWorn, AlreadyInAwardMailbox, AlreadyInThirtyMinuteQueue, AlreadyInMyPhrases, AlreadyKnowDoodleTraining, AlreadyRented, GenericAlreadyHaveError, UnknownError, UnknownToon, ')
GiveAwardErrorStrings = {GiveAwardErrors.Success: 'success', GiveAwardErrors.WrongGender: 'wrong gender', GiveAwardErrors.NotGiftable: 'item is not giftable', GiveAwardErrors.FullMailbox: 'mailbox is full', GiveAwardErrors.FullAwardMailbox: 'award mailbox is full', GiveAwardErrors.AlreadyInMailbox: 'award already in mailbox.', GiveAwardErrors.AlreadyInGiftQueue: 'award already in gift queue.', GiveAwardErrors.AlreadyInOrderedQueue: 'award already in ordered queue.', GiveAwardErrors.AlreadyInCloset: 'award already in closet.', GiveAwardErrors.AlreadyBeingWorn: 'award already being worn.', GiveAwardErrors.AlreadyInAwardMailbox: 'award already in award mailbox', GiveAwardErrors.AlreadyInThirtyMinuteQueue: 'award already in 30 minute queue', GiveAwardErrors.AlreadyInMyPhrases: 'speed chat award already in my phrases', GiveAwardErrors.AlreadyKnowDoodleTraining: 'doodle training award already known', GiveAwardErrors.AlreadyRented: 'award is already rented', GiveAwardErrors.GenericAlreadyHaveError: 'generic-already-have error', GiveAwardErrors.UnknownError: 'unknown error', GiveAwardErrors.UnknownToon: 'toon not in database'}