# File: T (Python 2.2)

from PandaModules import *
import Localizer
WallBitmask = BitMask32.bit(0)
FloorBitmask = BitMask32.bit(1)
CameraBitmask = BitMask32.bit(2)
CatchGameBitmask = BitMask32.bit(3)
GhostBitmask = BitMask32.bit(4)
FurnitureSideBitmask = BitMask32.bit(5)
FurnitureTopBitmask = BitMask32.bit(6)
FurnitureDragBitmask = BitMask32.bit(7)
DefaultCameraFov = 52.0
MakeAToonCameraFov = 35.0
DefaultCameraFar = 400.0
DefaultCameraNear = 1.0
MaxFriends = 50
MaxBackCatalog = 50
MaxMailboxContents = 20
MaxHouseItems = 30
ExtraDeletedItems = 5
DeletedItemLifetime = 7 * 24 * 60
P_OnOrderListFull = -11
P_MailboxFull = -10
P_NoPurchaseMethod = -9
P_ReachedPurchaseLimit = -8
P_NoRoomForItem = -7
P_NotShopping = -6
P_NotAtMailbox = -5
P_NotInCatalog = -4
P_NotEnoughMoney = -3
P_InvalidIndex = -2
P_UserCancelled = -1
P_ItemAvailable = 1
P_ItemOnOrder = 2
FM_NondeletableItem = -6
FM_InvalidIndex = -5
FM_NotOwner = -4
FM_NotDirector = -3
FM_RoomFull = -2
FM_HouseFull = -1
FM_MovedItem = 1
FM_SwappedItem = 2
FM_DeletedItem = 3
FM_RecoveredItem = 4
FriendChat = 1
CommonChat = 1
SuperChat = 2
MaxCustomMessages = 15
SPHidden = 0
SPRender = 1
SPDonaldsBoat = 2
SPMinniesPiano = 3
SPDynamic = 4
CENormal = 0
CEBigHead = 1
CESmallHead = 2
CEBigLegs = 3
CESmallLegs = 4
CEBigToon = 5
CESmallToon = 6
CEFlatPortrait = 7
CEFlatProfile = 8
CETransparent = 9
CENoColor = 10
CEInvisible = 11
CEGhost = 'g'
BigToonScale = 1.5
SmallToonScale = 0.5
DisconnectUnknown = 0
DisconnectBookExit = 1
DisconnectCloseWindow = 2
DisconnectPythonError = 3
DisconnectSwitchShards = 4
DisconnectGraphicsError = 5
DatabaseDialogTimeout = 20.0
DatabaseGiveupTimeout = 45.0
PeriodTimerWarningTime = (600, 300, 60)
MaxHpLimit = 100
MaxCarryLimit = 80
MaxQuestCarryLimit = 4
MaxClothes = 20
WalkCutOff = 0.5
RunCutOff = 8.0
FloorOffset = 0.025000000000000001
ToonFont = None
InterfaceFont = None
SignFont = None
MinnieFont = None
SuitFont = None

def getInterfaceFont():
    global InterfaceFont
    if InterfaceFont == None:
        InterfaceFont = loader.loadFont(Localizer.InterfaceFont, lineHeight = 1.0)
    
    return InterfaceFont


def getToonFont():
    return getInterfaceFont()


def getSignFont():
    global SignFont
    if SignFont == None:
        SignFont = loader.loadFont('phase_3/models/fonts/MickeyFont')
    
    return SignFont


def getMinnieFont():
    global MinnieFont
    if MinnieFont == None:
        MinnieFont = loader.loadFont('phase_3/models/fonts/MinnieFont')
    
    return MinnieFont


def getSuitFont():
    global SuitFont
    if SuitFont == None:
        SuitFont = loader.loadFont('phase_3/models/fonts/vtRemingtonPortable.ttf', pixelsPerUnit = 40, spaceAdvance = 0.25, lineHeight = 1.0)
    
    return SuitFont


def getAspectRatio():
    return 4.0 / 3.0

QuietZone = 1
UberZone = 2
DonaldsDock = 1000
ToontownCentral = 2000
TheBrrrgh = 3000
MinniesMelodyland = 4000
DaisyGardens = 5000
ConstructionZone = 6000
FunnyFarm = 7000
GoofyStadium = 8000
DonaldsDreamland = 9000
WelcomeValleyToken = 0
BossbotHQ = 10000
BossbotLobby = 10100
BossbotBasement = 10200
SellbotHQ = 11000
SellbotLobby = 11100
SellbotBasement = 11200
CashbotHQ = 12000
CashbotLobby = 12100
CashbotBasement = 12200
LawbotHQ = 13000
LawbotLobby = 13100
LawbotBasement = 13200
Tutorial = 15000
MyEstate = 16000
WelcomeValleyBegin = 20000
WelcomeValleyEnd = 61000
DynamicZonesBegin = 61000
DynamicZonesEnd = 1 << 20
StreetNames = Localizer.GlobalStreetNames
StreetBranchZones = StreetNames.keys()
Hoods = (DonaldsDock, ToontownCentral, TheBrrrgh, MinniesMelodyland, DaisyGardens, DonaldsDreamland)
NoPreviousGameId = 0
RaceGameId = 1
CannonGameId = 2
TagGameId = 3
PatternGameId = 4
RingGameId = 5
MazeGameId = 6
TugOfWarGameId = 7
CatchGameId = 8
MinigameNames = {
    'race': RaceGameId,
    'cannon': CannonGameId,
    'tag': TagGameId,
    'pattern': PatternGameId,
    'ring': RingGameId,
    'maze': MazeGameId,
    'tug': TugOfWarGameId,
    'catch': CatchGameId }
MinigameTemplateId = -1
MinigameIDs = (RaceGameId, CannonGameId, TagGameId, PatternGameId, RingGameId, MazeGameId, TugOfWarGameId, CatchGameId)
MinigamePlayerMatrix = {
    1: (CannonGameId, RingGameId, MazeGameId, TugOfWarGameId, CatchGameId),
    2: (CannonGameId, PatternGameId, RingGameId, TagGameId, MazeGameId, TugOfWarGameId, CatchGameId),
    3: (CannonGameId, PatternGameId, RingGameId, TagGameId, RaceGameId, MazeGameId, TugOfWarGameId, CatchGameId),
    4: (CannonGameId, PatternGameId, RingGameId, TagGameId, RaceGameId, MazeGameId, TugOfWarGameId, CatchGameId) }
NetworkLatency = 1.0
maxLoginWidth = 9.0999999999999996
ThinkPosHotkey = 'f1-up'
PlaceMarkerHotkey = 'f2-up'
FriendsListHotkey = 'f7-up'
StickerBookHotkey = 'f8-up'
OptionsPageHotkey = 'escape-up'
ScreenshotHotkey = 'f9-up'
SynchronizeHotkey = 'f6-up'
QuestsHotkeyOn = 'end'
QuestsHotkeyOff = 'end-up'
InventoryHotkeyOn = 'home'
InventoryHotkeyOff = 'home-up'
PrintCamPosHotkey = 'f12-up'
phaseMap = {
    Tutorial: 4,
    ToontownCentral: 4,
    MyEstate: 5.5,
    DonaldsDock: 6,
    MinniesMelodyland: 6,
    GoofyStadium: 6,
    TheBrrrgh: 8,
    DaisyGardens: 8,
    FunnyFarm: 8,
    DonaldsDreamland: 8,
    ConstructionZone: 8 }
streetPhaseMap = {
    ToontownCentral: 5,
    DonaldsDock: 6,
    MinniesMelodyland: 6,
    GoofyStadium: 6,
    TheBrrrgh: 8,
    DaisyGardens: 8,
    FunnyFarm: 8,
    DonaldsDreamland: 8,
    ConstructionZone: 8 }
dnaMap = {
    Tutorial: 'toontown_central',
    ToontownCentral: 'toontown_central',
    DonaldsDock: 'donalds_dock',
    MinniesMelodyland: 'minnies_melody_land',
    GoofyStadium: 'not done yet',
    TheBrrrgh: 'the_burrrgh',
    DaisyGardens: 'daisys_garden',
    FunnyFarm: 'not done yet',
    DonaldsDreamland: 'donalds_dreamland',
    ConstructionZone: 'not done yet' }
hoodNameMap = {
    DonaldsDock: Localizer.DonaldsDock,
    ToontownCentral: Localizer.ToontownCentral,
    TheBrrrgh: Localizer.TheBrrrgh,
    MinniesMelodyland: Localizer.MinniesMelodyland,
    DaisyGardens: Localizer.DaisyGardens,
    ConstructionZone: Localizer.ConstructionZone,
    FunnyFarm: Localizer.FunnyFarm,
    GoofyStadium: Localizer.GoofyStadium,
    DonaldsDreamland: Localizer.DonaldsDreamland,
    BossbotHQ: Localizer.BossbotHQ,
    SellbotHQ: Localizer.SellbotHQ,
    CashbotHQ: Localizer.CashbotHQ,
    LawbotHQ: Localizer.LawbotHQ,
    Tutorial: Localizer.Tutorial,
    MyEstate: Localizer.MyEstate }
safeZoneCountMap = {
    MyEstate: 8,
    Tutorial: 6,
    ToontownCentral: 6,
    DonaldsDock: 10,
    MinniesMelodyland: 5,
    GoofyStadium: 500,
    TheBrrrgh: 8,
    DaisyGardens: 9,
    FunnyFarm: 500,
    DonaldsDreamland: 5,
    ConstructionZone: 500 }
townCountMap = {
    MyEstate: 8,
    Tutorial: 40,
    ToontownCentral: 37,
    DonaldsDock: 40,
    MinniesMelodyland: 40,
    GoofyStadium: 40,
    TheBrrrgh: 40,
    DaisyGardens: 40,
    FunnyFarm: 40,
    DonaldsDreamland: 40,
    ConstructionZone: 40 }
hoodCountMap = {
    MyEstate: 2,
    Tutorial: 2,
    ToontownCentral: 2,
    DonaldsDock: 2,
    MinniesMelodyland: 2,
    GoofyStadium: 2,
    TheBrrrgh: 2,
    DaisyGardens: 2,
    FunnyFarm: 2,
    DonaldsDreamland: 2,
    ConstructionZone: 2 }
TrophyStarLevels = (10, 20, 30, 50, 75, 100)
TrophyStarColors = (Vec4(0.90000000000000002, 0.59999999999999998, 0.20000000000000001, 1), Vec4(0.90000000000000002, 0.59999999999999998, 0.20000000000000001, 1), Vec4(0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 1), Vec4(0.80000000000000004, 0.80000000000000004, 0.80000000000000004, 1), Vec4(1, 1, 0, 1), Vec4(1, 1, 0, 1))
ToonStandableGround = 0.70699999999999996
ToonForwardSpeed = 16.0
ToonJumpForce = 16.0
ToonReverseSpeed = 8.0
ToonRotateSpeed = 80.0
ToonForwardSlowSpeed = 6.0
ToonJumpSlowForce = 4.0
ToonReverseSlowSpeed = 2.5
ToonRotateSlowSpeed = 33.0
MickeySpeed = 5.0
MinnieSpeed = 3.2000000000000002
DonaldSpeed = 3.6800000000000002
GoofySpeed = 5.2000000000000002
PlutoSpeed = 5.5
SuitWalkSpeed = 4.7999999999999998
GlobalDialogColor = (1, 1, 0.75, 1)
DefaultBackgroundColor = (0.29999999999999999, 0.29999999999999999, 0.29999999999999999, 1)
TTWakeWaterHeight = -4.79
DDWakeWaterHeight = 1.669
EstateWakeWaterHeight = -0.29999999999999999
WakeRunDelta = 0.10000000000000001
WakeWalkDelta = 0.20000000000000001
NoItems = 0
NewItems = 1
OldItems = 2
SuitInvasionBegin = 0
SuitInvasionUpdate = 1
SuitInvasionEnd = 2
SuitInvasionBulletin = 3
toonBodyScales = {
    'mouse': 0.59999999999999998,
    'cat': 0.72999999999999998,
    'fowl': 0.66000000000000003,
    'rabbit': 0.73999999999999999,
    'horse': 0.84999999999999998,
    'dog': 0.84999999999999998 }
toonHeadScales = {
    'mouse': Point3(1.3078000000000001, 1.1274, 1.1274),
    'cat': Point3(1.125),
    'fowl': Point3(1.345, 1.1297999999999999, 1.3291999999999999),
    'rabbit': Point3(1.0),
    'horse': Point3(1.0),
    'dog': Point3(1.0857000000000001) }
legHeightDict = {
    's': 1.5,
    'm': 2.0,
    'l': 2.75 }
torsoHeightDict = {
    's': 1.5,
    'm': 1.75,
    'l': 2.25,
    'ss': 1.5,
    'ms': 1.75,
    'ls': 2.25,
    'sd': 1.5,
    'md': 1.75,
    'ld': 2.25 }
headHeightDict = {
    'dls': 0.75,
    'dss': 0.5,
    'dsl': 0.5,
    'dll': 0.75,
    'cls': 0.75,
    'css': 0.5,
    'csl': 0.5,
    'cll': 0.75,
    'hls': 0.75,
    'hss': 0.5,
    'hsl': 0.5,
    'hll': 0.75,
    'mls': 0.75,
    'mss': 0.5,
    'rls': 0.75,
    'rss': 0.5,
    'rsl': 0.5,
    'rll': 0.75,
    'fls': 0.75,
    'fss': 0.5,
    'fsl': 0.5,
    'fll': 0.75 }
