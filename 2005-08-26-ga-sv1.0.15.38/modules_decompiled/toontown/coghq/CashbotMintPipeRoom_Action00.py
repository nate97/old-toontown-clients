# File: C (Python 2.2)

from toontown.coghq.SpecImports import *
GlobalEntities = {
    1000: {
        'type': 'levelMgr',
        'name': 'LevelMgr',
        'comment': '',
        'parentEntId': 0,
        'cogLevel': 0,
        'farPlaneDistance': 1500,
        'modelFilename': 'phase_10/models/cashbotHQ/ZONE13a',
        'wantDoors': 1 },
    1001: {
        'type': 'editMgr',
        'name': 'EditMgr',
        'parentEntId': 0,
        'insertEntity': None,
        'removeEntity': None,
        'requestNewEntity': None,
        'requestSave': None },
    0: {
        'type': 'zone',
        'name': 'UberZone',
        'comment': '',
        'parentEntId': 0,
        'scale': 1,
        'description': '',
        'visibility': [] },
    10025: {
        'type': 'attribModifier',
        'name': 'strength',
        'comment': '',
        'parentEntId': 10002,
        'attribName': 'strength',
        'recursive': 1,
        'typeName': 'goon',
        'value': '10' },
    10001: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10000,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1.5,
        'attackRadius': 15,
        'crushCellId': None,
        'goonType': 'pg',
        'gridId': None,
        'hFov': 70,
        'strength': 10,
        'velocity': 4 },
    10005: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10003,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1.5,
        'attackRadius': 15,
        'crushCellId': None,
        'goonType': 'pg',
        'gridId': None,
        'hFov': 70,
        'strength': 10,
        'velocity': 4 },
    10006: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10004,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1.5,
        'attackRadius': 15,
        'crushCellId': None,
        'goonType': 'pg',
        'gridId': None,
        'hFov': 70,
        'strength': 10,
        'velocity': 4 },
    10014: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10013,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1.5,
        'attackRadius': 15,
        'crushCellId': None,
        'goonType': 'pg',
        'gridId': None,
        'hFov': 70,
        'strength': 10,
        'velocity': 4 },
    10016: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10015,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1.5,
        'attackRadius': 15,
        'crushCellId': None,
        'goonType': 'pg',
        'gridId': None,
        'hFov': 70,
        'strength': 10,
        'velocity': 4 },
    10018: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10017,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1.5,
        'attackRadius': 15,
        'crushCellId': None,
        'goonType': 'pg',
        'gridId': None,
        'hFov': 70,
        'strength': 10,
        'velocity': 4 },
    10021: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10020,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1.5,
        'attackRadius': 15,
        'crushCellId': None,
        'goonType': 'pg',
        'gridId': None,
        'hFov': 70,
        'strength': 10,
        'velocity': 4 },
    10024: {
        'type': 'goon',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10023,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1.5,
        'attackRadius': 15,
        'crushCellId': None,
        'goonType': 'pg',
        'gridId': None,
        'hFov': 70,
        'strength': 10,
        'velocity': 4 },
    10035: {
        'type': 'healBarrel',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10037,
        'pos': Point3(-56.3795814514, 0.0, 0.0),
        'hpr': Vec3(106.821411133, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'rewardPerGrab': 7,
        'rewardPerGrabMax': 8 },
    10036: {
        'type': 'healBarrel',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 10037,
        'pos': Point3(15.385247230499999, 21.035751342800001, 0.0),
        'hpr': Vec3(52.431407928500001, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'rewardPerGrab': 7,
        'rewardPerGrabMax': 8 },
    10029: {
        'type': 'model',
        'name': 'rightPillar',
        'comment': '',
        'parentEntId': 10032,
        'pos': Point3(0.0, -22.344186782800001, 0.0),
        'hpr': Point3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/pipes_A1' },
    10030: {
        'type': 'model',
        'name': 'leftPillar',
        'comment': '',
        'parentEntId': 10032,
        'pos': Point3(0.0, 21.945150375400001, 0.0),
        'hpr': Point3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/pipes_A1' },
    10033: {
        'type': 'model',
        'name': 'backPillar',
        'comment': '',
        'parentEntId': 10032,
        'pos': Point3(41.443279266399998, 0.0, 0.0),
        'hpr': Point3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/pipes_A1' },
    10034: {
        'type': 'model',
        'name': 'frontPillar',
        'comment': '',
        'parentEntId': 10032,
        'pos': Point3(-41.084846496600001, 0.0, 0.0),
        'hpr': Point3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/pipes_A1' },
    10039: {
        'type': 'model',
        'name': 'rightPillar',
        'comment': '',
        'parentEntId': 10038,
        'pos': Point3(0.0, -66.861587524399994, 0.0),
        'hpr': Point3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/pipes_A1' },
    10040: {
        'type': 'model',
        'name': 'leftPillar',
        'comment': '',
        'parentEntId': 10038,
        'pos': Point3(0.0, 67.096603393600006, 0.0),
        'hpr': Point3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/pipes_A1' },
    10042: {
        'type': 'model',
        'name': 'frontRightPillar',
        'comment': '',
        'parentEntId': 10043,
        'pos': Point3(0.0, -22.571107864399998, 0.0),
        'hpr': Point3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/pipes_A1' },
    10044: {
        'type': 'model',
        'name': 'frontLeftPillar',
        'comment': '',
        'parentEntId': 10043,
        'pos': Point3(0.0, 22.168663024899999, 0.0),
        'hpr': Point3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/pipes_A1' },
    10046: {
        'type': 'model',
        'name': 'frontRightPillar',
        'comment': '',
        'parentEntId': 10045,
        'pos': Point3(0.0, -22.571107864399998, 0.0),
        'hpr': Point3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/pipes_A1' },
    10047: {
        'type': 'model',
        'name': 'frontLeftPillar',
        'comment': '',
        'parentEntId': 10045,
        'pos': Point3(0.0, 22.168663024899999, 0.0),
        'hpr': Point3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/pipes_A1' },
    10049: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10048,
        'pos': Point3(0.94989842176399997, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.2906093597399999, 1.2906093597399999, 1.2906093597399999),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/crates_F1.bam' },
    10050: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10048,
        'pos': Point3(-13.1818971634, -7.1713824272200002, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/crates_E.bam' },
    10051: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10048,
        'pos': Point3(0.96833425760299996, -13.378503799400001, 0.0),
        'hpr': Vec3(180.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/crates_C1.bam' },
    10053: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10052,
        'pos': Point3(0.60636216402099996, -12.135335922199999, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/crates_G1.bam' },
    10054: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10052,
        'pos': Point3(7.85215950012, 20.0426883698, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.1665921211200001, 1.1665921211200001, 1.1665921211200001),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/crates_E.bam' },
    10055: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10052,
        'pos': Point3(13.5166940689, -0.81913888454399997, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.5191447734800001, 1.5191447734800001, 1.5191447734800001),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/crates_D.bam' },
    10056: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10052,
        'pos': Point3(10.8745326996, 4.6170301437400001, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/crates_C1.bam' },
    10057: {
        'type': 'model',
        'name': '<unnamed>',
        'comment': '',
        'parentEntId': 10052,
        'pos': Point3(31.847000122099999, -14.564583778399999, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.1728117466000001, 1.1728117466000001, 1.1728117466000001),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/crates_A.bam' },
    10058: {
        'type': 'model',
        'name': 'copy of <unnamed>',
        'comment': '',
        'parentEntId': 10052,
        'pos': Point3(31.936925888099999, 14.303739547699999, 0.0),
        'hpr': Point3(90.0, 0.0, 0.0),
        'scale': Vec3(1.1728117466000001, 1.1728117466000001, 1.1728117466000001),
        'collisionsOnly': 0,
        'flattenType': 'light',
        'loadType': 'loadModelCopy',
        'modelPath': 'phase_10/models/cashbotHQ/crates_A.bam' },
    10002: {
        'type': 'nodepath',
        'name': 'goons',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Point3(270.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0) },
    10007: {
        'type': 'nodepath',
        'name': 'rightElbow',
        'comment': '',
        'parentEntId': 10027,
        'pos': Point3(43.3083152771, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0) },
    10008: {
        'type': 'nodepath',
        'name': 'leftElbow',
        'comment': '',
        'parentEntId': 10026,
        'pos': Point3(-38.578956603999998, -2.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0) },
    10009: {
        'type': 'nodepath',
        'name': 'nearRight',
        'comment': '',
        'parentEntId': 10027,
        'pos': Point3(25.604152679399999, -41.375358581500002, 0.0),
        'hpr': Vec3(320.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0) },
    10010: {
        'type': 'nodepath',
        'name': 'nearLeft',
        'comment': '',
        'parentEntId': 10026,
        'pos': Point3(-25.600000381499999, -41.3800010681, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1 },
    10011: {
        'type': 'nodepath',
        'name': 'farRight',
        'comment': '',
        'parentEntId': 10027,
        'pos': Point3(25.600000381499999, 41.3800010681, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1 },
    10012: {
        'type': 'nodepath',
        'name': 'farLeft',
        'comment': '',
        'parentEntId': 10026,
        'pos': Point3(-25.600000381499999, 41.3800010681, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1 },
    10019: {
        'type': 'nodepath',
        'name': 'entrance',
        'comment': '',
        'parentEntId': 10002,
        'pos': Point3(0.0, -82.502098083500002, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0) },
    10022: {
        'type': 'nodepath',
        'name': 'exit',
        'comment': '',
        'parentEntId': 10002,
        'pos': Point3(0.0, 88.447875976600002, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0) },
    10026: {
        'type': 'nodepath',
        'name': 'left',
        'comment': '',
        'parentEntId': 10002,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1 },
    10027: {
        'type': 'nodepath',
        'name': 'right',
        'comment': '',
        'parentEntId': 10002,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1 },
    10028: {
        'type': 'nodepath',
        'name': 'props',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(0.0, -1.80477809906, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0) },
    10031: {
        'type': 'nodepath',
        'name': 'pillars',
        'comment': '',
        'parentEntId': 10028,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1 },
    10032: {
        'type': 'nodepath',
        'name': 'centerPillars',
        'comment': '',
        'parentEntId': 10031,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1 },
    10037: {
        'type': 'nodepath',
        'name': 'barrels',
        'comment': '',
        'parentEntId': 0,
        'pos': Point3(102.779998779, -1.2400000095399999, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1 },
    10038: {
        'type': 'nodepath',
        'name': 'outerPillars',
        'comment': '',
        'parentEntId': 10031,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1 },
    10043: {
        'type': 'nodepath',
        'name': 'frontPillars',
        'comment': '',
        'parentEntId': 10031,
        'pos': Point3(-89.966552734399997, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0) },
    10045: {
        'type': 'nodepath',
        'name': 'backPillars',
        'comment': '',
        'parentEntId': 10031,
        'pos': Point3(89.970001220699999, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': Vec3(1.0, 1.0, 1.0) },
    10048: {
        'type': 'nodepath',
        'name': 'frontProps',
        'comment': '',
        'parentEntId': 10028,
        'pos': Point3(-100.412567139, -10.883513450600001, 0.0),
        'hpr': Vec3(270.0, 0.0, 0.0),
        'scale': Vec3(1.66847121716, 1.66847121716, 1.66847121716) },
    10052: {
        'type': 'nodepath',
        'name': 'backProps',
        'comment': '',
        'parentEntId': 10028,
        'pos': Point3(100.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1 },
    10000: {
        'type': 'path',
        'name': 'triangle',
        'comment': '',
        'parentEntId': 10008,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1,
        'pathIndex': 1,
        'pathScale': 1.5 },
    10003: {
        'type': 'path',
        'name': 'square',
        'comment': '',
        'parentEntId': 10007,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1,
        'pathIndex': 0,
        'pathScale': 1.0 },
    10004: {
        'type': 'path',
        'name': 'bowtie',
        'comment': '',
        'parentEntId': 10009,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1,
        'pathIndex': 2,
        'pathScale': 1.0 },
    10013: {
        'type': 'path',
        'name': 'square',
        'comment': '',
        'parentEntId': 10010,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1,
        'pathIndex': 0,
        'pathScale': 1.0 },
    10015: {
        'type': 'path',
        'name': 'square',
        'comment': '',
        'parentEntId': 10011,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1,
        'pathIndex': 0,
        'pathScale': 1.0 },
    10017: {
        'type': 'path',
        'name': 'square',
        'comment': '',
        'parentEntId': 10012,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1,
        'pathIndex': 0,
        'pathScale': 1.0 },
    10020: {
        'type': 'path',
        'name': 'pace',
        'comment': '',
        'parentEntId': 10019,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1,
        'pathIndex': 3,
        'pathScale': 1.0 },
    10023: {
        'type': 'path',
        'name': 'pace',
        'comment': '',
        'parentEntId': 10022,
        'pos': Point3(0.0, 0.0, 0.0),
        'hpr': Vec3(0.0, 0.0, 0.0),
        'scale': 1,
        'pathIndex': 3,
        'pathScale': 1.0 } }
Scenario0 = { }
levelSpec = {
    'globalEntities': GlobalEntities,
    'scenarios': [
        Scenario0] }