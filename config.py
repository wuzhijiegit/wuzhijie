# coding:utf-8
"""
自动化脚本配置模块，用来存放脚本运行过程中的各类配置参数
执行机相关的配置参数
"""
import os

#######################################与测试环境有关的配置（需要根据自己环境更改）#############################################
"""======================================================公共参数====================================================="""
# 项目
PROJECT = 'X2'
# PROJECT = 'F2'
# 车辆环境 0:台架，1：实车
CAR_ENV_FLAG = 1
# 0:预生产环境，1:商用环境
Env_Flag = 0
# 测试环境
TEST_ENV_FLAG = 'wwx1275683'
# TEST_ENV_FLAG = 'wwx1275683'
# TEST_ENV_FLAG = 'l30034136'
# 是否有canoe
CANOE_FLAG = 0
# 是否有手机     1:有       0:没有
app_flag = 1
# app_flag = 0

# 环境ECU配置（华为部件）
ECU_LIST = {
    'X2': {
        's00566695': {
            'TMS_flag': 0,
            'MDC_flag': 1,
            'CDC_flag': 1,
            'TBOX_flag': 1,
            'VDC_flag': 1,
            'VIU1_flag': 1,
            'VIU2_flag': 1,
            'VIU3_flag': 1,
            'VIU4_flag': 0,
            'EAS_flag': 0,
            'WTC_flag': 0,
        },
        'wwx1275683': {
            'TMS_flag': 0,
            'MDC_flag': 0,
            'CDC_flag': 1,
            'TBOX_flag': 1,
            'VDC_flag': 1,
            'VIU1_flag': 1,
            'VIU2_flag': 1,
            'VIU3_flag': 1,
            'VIU4_flag': 1,
            'EAS_flag': 0,
            'WTC_flag': 0,
        },
    },
    'F2': {
        'l30034136': {
            'TMS_flag': 0,
            'MDC_flag': 0,
            'CDC_flag': 1,
            'TBOX_flag': 1,
            'VDC_flag': 1,
            'VIU1_flag': 1,
            'VIU2_flag': 1,
            'VIU3_flag': 1,
            'VIU4_flag': 0,
            'EAS_flag': 0,
            'WTC_flag': 0,
        },
    },
    'X1': {},
}
ECU_EXIXT_LIST = ECU_LIST.get(PROJECT).get(TEST_ENV_FLAG)
cdc_flag = ECU_LIST.get(PROJECT).get(TEST_ENV_FLAG).get('CDC_flag')
tbox_flag = ECU_LIST.get(PROJECT).get(TEST_ENV_FLAG).get('TBOX_flag')
mdc_flag = ECU_LIST.get(PROJECT).get(TEST_ENV_FLAG).get('MDC_flag')
mcuf_flag = ECU_LIST.get(PROJECT).get(TEST_ENV_FLAG).get('MCUF_flag')
mcur_flag = ECU_LIST.get(PROJECT).get(TEST_ENV_FLAG).get('MCUR_flag')

# 零部件号及对应升级时长预期
ECU_ID_TIMES = {
    'X2': {'703001184AA': 3, '702000176AA': 20, '809000086AA': 5, '703001183AA': 10, '809000087AA': 2, '809000088AA': 2,
           '704001037AA': 2},
    'F2': {}
}
# 零部件与零部件号
ECU_NAME_ID = {
    'X2': {'703001184AA': 'TBOX', '702000176AA': 'MDC', '809000086AA': 'VDC', '703001183AA': 'CDC',
           '809000087AA': 'VIU1', '809000088AA': 'VIU2', '704001037AA': 'VIU3'},
    'F2': {}
}
ecu_id_times = ECU_ID_TIMES.get(PROJECT)
ecu_name_id = ECU_NAME_ID.get(PROJECT)
# Devices_ID
Devices_ID_DATA = {
    'X2': {
        's00566695': {
            'CDC': '0123456789ABCDEF',
            # 'APP': 'Q7PDU19A18002230',
            'APP': 'Q7PDU19A18003624',
            # "APP": '52a74d34',
            # 'TBOX': 'TKR0223428000018'
            'TBOX': 'TKR0223428000018'
        },
        'wwx1275683': {
            'CDC': '102375397117',
            'APP': 'RFCMA0010TA',
            'TBOX': 'TKR0223428000018'
        },

    },
    'F2': {
        'l30034136': {
            # 'CDC': '0123456789ABCDEF',
            'CDC': 'CDCX100Y1000',
            # 'APP': 'Q7PDU19A18002230',
            'APP': '5ENDU19C04002600',
            # "APP": '52a74d34',
            # 'TBOX': 'TKR0223428000018'
            'TBOX': '6JK0223223000123'
        },
    },
    'X1': {},
}

# adb device id
CDC_Devices_ID = Devices_ID_DATA.get(PROJECT).get(TEST_ENV_FLAG).get('CDC')
APP_Devices_ID = Devices_ID_DATA.get(PROJECT).get(TEST_ENV_FLAG).get('APP')
TBOX_Devices_ID = Devices_ID_DATA.get(PROJECT).get(TEST_ENV_FLAG).get('TBOX')
ADB_DEVICE_ID = {'CDC': CDC_Devices_ID, 'APP': APP_Devices_ID, 'TBOX': TBOX_Devices_ID, 'VDC': TBOX_Devices_ID}
"""===============================================vehicle_operation参数==============================================="""
is_canoe_way = 0  # 继电器控制：0,CANoe控制：1
# is_canoe_way = 0  # 继电器控制：0,CANoe控制：1

"""====================================================OTA_CTRL参数==================================================="""
# 生产/预生产判断
if Env_Flag:
    # 生产车云账号
    CLOUD_ACCOUNT = {
        'X2': {
            'USER_NAME': "sunjun00566695",
            'PASSWORD': "",
            'IP': 'chssatsp.icvcs.com'
        },
        'X1': {}
    }
    CAR_PROJECT_DATA = {
        "X2": {
            's00566695': {
                'CAR_TYPE_NAME': '智界 S7',
                'CAR_NUM': '',
                # 'CAR_VIN': 'X2JJFAVHR20230630',
                # 'CAR_VIN': 'JJFAEH3SECTEST001',
                'CAR_VIN': '',
            },
            'm00613464': {
                'CAR_TYPE_NAME': 'N50OTAM部署CDC联调',
                'CAR_NUM': 'JJFAEH3SECTEST001',
                # 'CAR_VIN': 'X2JJFAVHR20230530',
                'CAR_VIN': 'JJFAEH3SECTEST001',
            },
        },
        "X1": {},
    }
else:
    # 预生产车云账号
    CLOUD_ACCOUNT = {
        'X2': {
            'USER_NAME': "sunjun00566695",
            'PASSWORD': "Ota.123456",
            'IP': 'portal.x2pre.icvcs.com'
        },
        'X1': {
            'USER_NAME': "",
            'PASSWORD': "",
            'IP': 'webtest.fgaiservice.com'
        },
        'F2': {
            'USER_NAME': "lihuifeng30034136",
            'PASSWORD': "",
            'IP': 'webtest.fgaiservice.com'
        },
    }
    CAR_PROJECT_DATA = {
        'X2': {
            's00566695': {
                'CAR_TYPE_NAME': 'VHR测试',
                'CAR_NUM': 'test202304141016',
                # 'CAR_VIN': 'X2JJFAVHR20230630',
                # 'CAR_VIN': 'JJFAEH3SECTEST001',
                'CAR_VIN': 'JJFAOTATEST000001',
            },
            'wwx1275683': {
                'CAR_TYPE_NAME': 'EH3',
                'CAR_NUM': 'MATERIAL00001',
                'CAR_VIN': 'LNNAJDDU6PD490748',
                'CAR_asset': '10_703001183AA_11_9MB_12_23071100013300002'
            }
        },
        'F2': {
            'l30034136': {
                'CAR_TYPE_NAME': '问界M9EV',
                'CAR_NUM': 'B28FEF9LA4L01',
                # 'CAR_VIN': 'X2JJFAVHR20230630',
                # 'CAR_VIN': 'JJFAEH3SECTEST001',
                'CAR_VIN': 'F2JJFAOTALABCAR01',
            }
        },
        "X1": {},
    }

# 车云账号
USER_NAME = CLOUD_ACCOUNT.get(PROJECT).get('USER_NAME')
PASSWORD = CLOUD_ACCOUNT.get(PROJECT).get('PASSWORD')
IP = CLOUD_ACCOUNT.get(PROJECT).get('IP')

# 车型项目名称
CAR_TYPE_NAME = CAR_PROJECT_DATA.get(PROJECT).get(TEST_ENV_FLAG).get("CAR_TYPE_NAME")
# 整车物料号
CAR_NUM = CAR_PROJECT_DATA.get(PROJECT).get(TEST_ENV_FLAG).get("CAR_NUM")
# 车辆VIN
CAR_VIN = CAR_PROJECT_DATA.get(PROJECT).get(TEST_ENV_FLAG).get("CAR_VIN")

"""====================================================CANOE_CTRL参数================================================"""
# canoe工程路径 X2
CanoeCfgPath = {
    'X2': {
        's00566695': r'D:\sunjun\X2_CANOE_PROJECT\CANoe_V14_20230725\FOTA_Python_202102091141-14-0801.cfg',
        'wwx1275683': r'D:\sunjun\X2_CANOE_PROJECT\CANoe_V14_20230725\FOTA_Python_202102091141-14-0801.cfg'
    },
    'F2': {
        'l30034136': r'D:\01_auto_test\F2_CANoe_Project\CANoe_Project.cfg'
    },
    'X1': ''
}
CFG_PATH = CanoeCfgPath.get(PROJECT).get(TEST_ENV_FLAG)
# canoe控制
CANOE_CONFIG = {
    "X2": {
        "PDCU_Resp": 'PDCU_Resp', "PDCU_RemWakeUpFlag": "PDCU_RemWakeUpFlag",
        "PDCU_RemKL15PwrOnReq": "PDCU_RemKL15PwrOnReq",
        "PDCU_FbRDUgrdModDwndProgEndFlg": "PDCU_FbRDUgrdModDwndProgEndFlg",
        "PDCU_VehAllwRefrshFlg": "PDCU_VehAllwRefrshFlg",
        "PDCU_BatSOCStaisfyOTA": "PDCU_BatSOCStaisfyOTA",
        "PDCU_RdyStaisfyOTA": "PDCU_RdyStaisfyOTA",
        "PDCU_BJEVChrg": "PDCU_BJEVChrg",
        "PDCU_StorgBatSOCStaisfyOTA": "PDCU_StorgBatSOCStaisfyOTA",
        "PDCU_VelSpdStaisfyOTA": "PDCU_VelSpdStaisfyOTA",
        "PDCU_ShiftStaisfyOTA": "PDCU_ShiftStaisfyOTA",
        "PDCU_FCStaisfyOTA": "PDCU_FCStaisfyOTA",
        "PDCU_OutPwrStaisfyOTA": "PDCU_OutPwrStaisfyOTA",
        "PDCU_RemRefrshStrtFlg": "PDCU_RemRefrshStrtFlg",
        "PEPS_SIG": "PEPS_SIG", "IG_STATE": "IG_STATE",
        "PDCU_Sig": "PDCU_Sig", "OTA_State": "OTA_State",
        "PDCU_INIT": "PDCU_INIT", "PDCU_VehSt": "PDCU_VehSt",
        "REFRESH_Sig": "REFRESH_Sig", "NW_Flag": "NW_Flag",
        "TBOX_Req": "TBOX_Req", "TBOX_RemRefrshReqCmd": "TBOX_RemRefrshReqCmd",
        "TBOX_RefrshFlg": "TBOX_RefrshFlg",
        "TBOX_RDUgrdModDwnloadProgHVReq": "TBOX_RDUgrdModDwnloadProgHVReq",
        "TBOX_TerminalRemWakeupSig": "TBOX_TerminalRemWakeupSig",
        "TBOX_RemKL15PwrOnReq": "TBOX_RemKL15PwrOnReq", "EPB": "VDC_epbRequest",
        "sleep_flag": "sleep_flag", "Initial_Value": "Vehicle_State",
        "Initial_Req_Value": "Vehicle_Req",
        "Speed": "Speed", "Power_SOC": "Power_SOC", "battery_soc": "Battery_SOC",
        "DriverSelfBelt": "DriverSelfBelt", "Lock_Status": "Lock_Status",
        "Crash_Sig": "Crash_Sig", "Gear_Set": "Gear_Set", "LFDoor": "LFDoor",
        "Ready": "Ready", "Fault_Ctrl": "Fault_Ctrl", "Cool_Fault": "Cool_Fault",
        "UpHV_Fault": "UpHV_Fault", "HV_mode": "HV_mode", "ECU_Flag": "ECU_Flag", "MCUR_Flag": "MCUR_Flag",
        "TMS_Flag": "TMS_Flag", "BMS_Flag": "BMS_Flag", "PDU_Flag": "PDU_Flag", "PDCU_Flag": "PDCU_Flag",
        'Key_Press': 'Key_Press', 'veh_mode': 'veh_mode', 'Brake_State': 'Brake_State'
    },
    "F2": {
        "PDCU_Resp": 'PDCU_Resp', "PDCU_RemWakeUpFlag": "PDCU_RemWakeUpFlag",
        "PDCU_RemKL15PwrOnReq": "PDCU_RemKL15PwrOnReq",
        "PDCU_FbRDUgrdModDwndProgEndFlg": "PDCU_FbRDUgrdModDwndProgEndFlg",
        "PDCU_VehAllwRefrshFlg": "PDCU_VehAllwRefrshFlg",
        "PDCU_BatSOCStaisfyOTA": "PDCU_BatSOCStaisfyOTA",
        "PDCU_RdyStaisfyOTA": "PDCU_RdyStaisfyOTA",
        "PDCU_BJEVChrg": "PDCU_BJEVChrg",
        "PDCU_StorgBatSOCStaisfyOTA": "PDCU_StorgBatSOCStaisfyOTA",
        "PDCU_VelSpdStaisfyOTA": "PDCU_VelSpdStaisfyOTA",
        "PDCU_ShiftStaisfyOTA": "PDCU_ShiftStaisfyOTA",
        "PDCU_FCStaisfyOTA": "PDCU_FCStaisfyOTA",
        "PDCU_OutPwrStaisfyOTA": "PDCU_OutPwrStaisfyOTA",
        "PDCU_RemRefrshStrtFlg": "PDCU_RemRefrshStrtFlg",
        "PEPS_SIG": "PEPS_SIG", "IG_STATE": "IG_STATE",
        "PDCU_Sig": "PDCU_Sig", "OTA_State": "OTA_State",
        "PDCU_INIT": "PDCU_INIT", "PDCU_VehSt": "PDCU_VehSt",
        "REFRESH_Sig": "REFRESH_Sig", "NW_Flag": "NW_Flag",
        "TBOX_Req": "TBOX_Req", "TBOX_RemRefrshReqCmd": "TBOX_RemRefrshReqCmd",
        "TBOX_RefrshFlg": "TBOX_RefrshFlg",
        "TBOX_RDUgrdModDwnloadProgHVReq": "TBOX_RDUgrdModDwnloadProgHVReq",
        "TBOX_TerminalRemWakeupSig": "TBOX_TerminalRemWakeupSig",
        "TBOX_RemKL15PwrOnReq": "TBOX_RemKL15PwrOnReq", "EPB": "VDC_epbRequest",
        "sleep_flag": "sleep_flag", "Initial_Value": "Vehicle_State",
        "Initial_Req_Value": "Vehicle_Req",
        "Speed": "Speed", "Power_SOC": "Power_SOC", "battery_soc": "Battery_SOC",
        "DriverSelfBelt": "DriverSelfBelt", "Lock_Status": "Lock_Status",
        "Crash_Sig": "Crash_Sig", "Gear_Set": "Gear_Set", "LFDoor": "LFDoor",
        "Ready": "Ready", "Fault_Ctrl": "Fault_Ctrl", "Cool_Fault": "Cool_Fault",
        "UpHV_Fault": "UpHV_Fault", "ECU_Flag": "ECU_Flag", "MCUR_Flag": "MCUR_Flag",
        "TMS_Flag": "TMS_Flag", "BMS_Flag": "BMS_Flag", "PDU_Flag": "PDU_Flag", "PDCU_Flag": "PDCU_Flag",
        'Key_Press': 'Key_Press', 'veh_mode': 'veh_mode', 'Brake_State': 'Brake_State',
        'VIU_VehAntithftSt': 'VIU_VehAntithftSt', 'Lock_Req': 'Lock_Req', 'VIU_PowerMode': 'VIU_PowerMode'
    },
    'X1': {}
}

# 关闭canoe
CLOSE_CANOE = r"taskkill /im CANoe64.exe -f"
PDCU_Resp = CANOE_CONFIG.get(PROJECT).get('PDCU_Resp')
# 设置PDCU远程唤醒响应控制标志位 0:初始值（默认肯定响应），1-》不响应
PDCU_RemWakeUpFlag = CANOE_CONFIG.get(PROJECT).get('PDCU_RemWakeUpFlag')
# 设置PDCU远程KL15响应控制标志位 0:初始值（默认肯定响应），1-》不响应
PDCU_RemKL15PwrOnReq = CANOE_CONFIG.get(PROJECT).get('PDCU_RemKL15PwrOnReq')
# PDCU静默下载响应控制标志位 0:初始值（默认肯定响应），1：允许下载，2：禁止下载
PDCU_FbRDUgrdModDwndProgEndFlg = CANOE_CONFIG.get(PROJECT).get('PDCU_FbRDUgrdModDwndProgEndFlg')
PDCU_VehAllwRefrshFlg = CANOE_CONFIG.get(PROJECT).get('PDCU_VehAllwRefrshFlg')
PDCU_BatSOCStaisfyOTA = CANOE_CONFIG.get(PROJECT).get('PDCU_BatSOCStaisfyOTA')
PDCU_RdyStaisfyOTA = CANOE_CONFIG.get(PROJECT).get('PDCU_RdyStaisfyOTA')
PDCU_BJEVChrg = CANOE_CONFIG.get(PROJECT).get('PDCU_BJEVChrg')
PDCU_StorgBatSOCStaisfyOTA = CANOE_CONFIG.get(PROJECT).get('PDCU_StorgBatSOCStaisfyOTA')
PDCU_VelSpdStaisfyOTA = CANOE_CONFIG.get(PROJECT).get('PDCU_VelSpdStaisfyOTA')
PDCU_ShiftStaisfyOTA = CANOE_CONFIG.get(PROJECT).get('PDCU_ShiftStaisfyOTA')
PDCU_FCStaisfyOTA = CANOE_CONFIG.get(PROJECT).get('PDCU_FCStaisfyOTA')
PDCU_OutPwrStaisfyOTA = CANOE_CONFIG.get(PROJECT).get('PDCU_OutPwrStaisfyOTA')
# PDCU OTA模式响应控制标志位 0:初始值（默认肯定响应），1：不响应
PDCU_RemRefrshStrtFlg = CANOE_CONFIG.get(PROJECT).get('PDCU_RemRefrshStrtFlg')
veh_mode = CANOE_CONFIG.get(PROJECT).get('veh_mode')
# IG 状态
PEPS_SIG = CANOE_CONFIG.get(PROJECT).get('PEPS_SIG')
# 获取IG 状态  1->igon  0->igoff
IG_STATE = CANOE_CONFIG.get(PROJECT).get('IG_STATE')
PDCU_Sig = CANOE_CONFIG.get(PROJECT).get('PDCU_Sig')
# 请求环境变量
Initial_Req_Value = CANOE_CONFIG.get(PROJECT).get('Initial_Req_Value')
# Key_Press 智能钥匙  1：按下  0：松开
Key_Press = CANOE_CONFIG.get(PROJECT).get('Key_Press')
# PDCU OTA模式标志位 1->OTA模式  0->非OTA模式
OTA_State = CANOE_CONFIG.get(PROJECT).get('OTA_State')
PDCU_INIT = CANOE_CONFIG.get(PROJECT).get('PDCU_INIT')
# PDCU 电源模式状态  30->高压  49->低压
PDCU_VehSt = CANOE_CONFIG.get(PROJECT).get('PDCU_VehSt')
# PDCU 条件检查响应标志位 0->初始值 1->允许刷写 2->禁止刷写
REFRESH_Sig = CANOE_CONFIG.get(PROJECT).get('REFRESH_Sig')
NW_Flag = CANOE_CONFIG.get(PROJECT).get('NW_Flag')
TBOX_Req = CANOE_CONFIG.get(PROJECT).get('TBOX_Req')
# TBOX请求刷写标志位  1->有请求  0->无请求
TBOX_RemRefrshReqCmd = CANOE_CONFIG.get(PROJECT).get('TBOX_RemRefrshReqCmd')
# TBOX进入ota模式标志位  0->初始值 1->有请求  2->无请求
TBOX_RefrshFlg = CANOE_CONFIG.get(PROJECT).get('TBOX_RefrshFlg')
# TBOX请求下载标志位  1->有请求  0->无请求
TBOX_RDUgrdModDwnloadProgHVReq = CANOE_CONFIG.get(PROJECT).get('TBOX_RDUgrdModDwnloadProgHVReq')
# TBOX远程请求唤醒标志位 1->有请求  0->无请求
TBOX_TerminalRemWakeupSig = CANOE_CONFIG.get(PROJECT).get('TBOX_TerminalRemWakeupSig')
# TBOX远程KL15请求标志位 1->有请求  2->无请求 0->初始值
TBOX_RemKL15PwrOnReq = CANOE_CONFIG.get(PROJECT).get('TBOX_RemKL15PwrOnReq')
# 监测总线休眠状态 1->唤醒  0->休眠
sleep_flag = CANOE_CONFIG.get(PROJECT).get('sleep_flag')
Initial_Value = CANOE_CONFIG.get(PROJECT).get('Initial_Value')
# 车速 车速 km/h （0-200）
Speed = CANOE_CONFIG.get(PROJECT).get('Speed')
# 动力电池SOC 动力电池SOC （0-100）
Power_SOC = CANOE_CONFIG.get(PROJECT).get('Power_SOC')
# 蓄电池SOC 0 ：不满足，1：满足
battery_soc = CANOE_CONFIG.get(PROJECT).get('battery_soc')
# 主驾安全带状态 0:系上 ；2：解开
DriverSelfBelt = CANOE_CONFIG.get(PROJECT).get('DriverSelfBelt')
# EPB状态 0:未定义 ；1：释放；2：夹紧；3：释放中；4：夹紧中
EPB = CANOE_CONFIG.get(PROJECT).get('EPB')
# Brake_State 智能踏板 1：踩  0：松
Brake_State = CANOE_CONFIG.get(PROJECT).get('Brake_State')
# 锁车状态 解防 0,设防：1
Lock_Status = CANOE_CONFIG.get(PROJECT).get('Lock_Status')
# 车辆防盗状态 解防 0,设防：1
VIU_VehAntithftSt = CANOE_CONFIG.get(PROJECT).get('VIU_VehAntithftSt')
# 车辆设防请求 解防 0,设防：1
Lock_Req = CANOE_CONFIG.get(PROJECT).get('Lock_Req')
# 碰撞信号 0：无碰撞 ,1：有碰撞
Crash_Sig = CANOE_CONFIG.get(PROJECT).get('Crash_Sig')
# 档位信息  0:初始值 ；1：P档；2：N档；3：R档；4：D档
Gear_Set = CANOE_CONFIG.get(PROJECT).get('Gear_Set')
# 设置主驾车门 0:closed,1:open
LFDoor = CANOE_CONFIG.get(PROJECT).get('LFDoor')
# 设置整车ready状态 0:非ready,1:ready
Ready = CANOE_CONFIG.get(PROJECT).get('Ready')
Fault_Ctrl = CANOE_CONFIG.get(PROJECT).get('Fault_Ctrl')
# 设置液冷状态 0->液冷正常，1->液冷异常
Cool_Fault = CANOE_CONFIG.get(PROJECT).get('Cool_Fault')
# PDCU高软上高压异常控制 0->正常，1->异常
UpHV_Fault = CANOE_CONFIG.get(PROJECT).get('UpHV_Fault')
# 高压模式 0->低压，1->高压
HV_mode = CANOE_CONFIG.get(PROJECT).get('HV_mode')
# 整车电源模式 0->OFF，1->ON
VIU_PowerMode = CANOE_CONFIG.get(PROJECT).get('VIU_PowerMode')
# 测试环境ecu标志位
ECU_Flag = CANOE_CONFIG.get(PROJECT).get('ECU_Flag')
MCUR_Flag = CANOE_CONFIG.get(PROJECT).get('MCUR_Flag')
TMS_Flag = CANOE_CONFIG.get(PROJECT).get('TMS_Flag')
BMS_Flag = CANOE_CONFIG.get(PROJECT).get('BMS_Flag')
PDU_Flag = CANOE_CONFIG.get(PROJECT).get('PDU_Flag')
PDCU_Flag = CANOE_CONFIG.get(PROJECT).get('PDCU_Flag')

# PDCU刷写响应控制
PDCU_REFRESH_FLAG = {
    0: [
        PDCU_VehAllwRefrshFlg, PDCU_OutPwrStaisfyOTA, PDCU_FCStaisfyOTA, PDCU_ShiftStaisfyOTA, PDCU_VelSpdStaisfyOTA,
        PDCU_StorgBatSOCStaisfyOTA, PDCU_BJEVChrg, PDCU_RdyStaisfyOTA, PDCU_BatSOCStaisfyOTA
    ],
    1: [PDCU_VehAllwRefrshFlg],
    2: [PDCU_RdyStaisfyOTA],
    3: [PDCU_BJEVChrg],
    4: [PDCU_StorgBatSOCStaisfyOTA],
    5: [PDCU_VelSpdStaisfyOTA],
    6: [PDCU_ShiftStaisfyOTA],
    7: [PDCU_FCStaisfyOTA],
    8: [PDCU_OutPwrStaisfyOTA],
    9: [
        PDCU_OutPwrStaisfyOTA, PDCU_FCStaisfyOTA, PDCU_ShiftStaisfyOTA, PDCU_VelSpdStaisfyOTA,
        PDCU_StorgBatSOCStaisfyOTA, PDCU_RdyStaisfyOTA, PDCU_BatSOCStaisfyOTA
    ],
}

"""====================================================APP_CTRL参数==================================================="""
# App各操作项对应接口值
APP_CONFIG = {
    'X2': {
        's00566695': {
            'APP_LatestVersion': '已是最新版本',  # App提示无升级任务
            'APP_MainButton': '//*[@resource-id="app.huawei.motor:id/app_hw_bottom_main"]/android.widget.LinearLayout[3]/android.widget.ImageView[1]',
            # 主界面
            'APP_UpdatePage': '当前版本',
            'APP_AppointmentUpgrade': '预约更新',
            'APP_SureButton': '确定',
            'APP_UpdatePageButton': '车辆软件版本',
            'APP_ClickBlank': [0.977, 0.011],
            'APP_CheckUpdates': '检查更新',
            'APP_KnowButton': '知道了',
            'APP_CancelOrderUpgrade': '取消预约',
            'APP_NotUpdateButton': "暂不更新",
            'APP_DropDownMenu': [0.957, 0.014, 0.514, 0.248],
            'APP_WifiReRule': r'content-desc="WLAN,(.*?)。"',
            'APP_WifiSwitch': [594, 348],
            'APP_DropUpMenu': [0.316, 0.83, 0.614, 0.498],
            'APP_UpdateButton': "立即更新",
            'APP_CountdownContent': 'app.huawei.motor:id/ota_countdown_text_end',  # 倒计时提示内容
            'APP_CancelCountdownButton': 'app.huawei.motor:id/ota_column_cancel_install',  # 取消倒计时按钮
            'APP_PackageName': 'app.huawei.motor',  # app包名
            'APP_ClearNotification': 'com.android.systemui:id/delete',  # app包名
            'APP_ScheduleInfo': 'app.huawei.motor:id/ota_upper_appointment_time_user',
            'APP_ScheduleMinute': [-2, ''],  # app定时时间分钟位置区域
            'APP_Schedule12Hour': [-5, -3],  # app定时时间小时-12制式位置区域
            'APP_Schedule24Hour': [2, 4],  # app定时时间小时-24制式位置区域
            'APP_NowTimingRE': r'resource-id="app.huawei.motor:id/hwadvancednumberpicker_textview.*?content-desc="(.*)"'
                               r' checkable="false"',
            'APP_12HourUp': [650, 1650],
            'APP_12HourDown': [650, 1950],
            'APP_12MinuteUp': [900, 1650],
            'APP_12MinuteDown': [900, 1550],
            'APP_24HourUp': [888, 388],
            'APP_24HourDown': [888, 580],
            'APP_24MinuteUp': [1064, 388],
            'APP_24MinuteDown': [1064, 580],
            'APP_DropDownWindow': [0, 2000, 0, 1000],
            'APP_Notification': '车辆升级提醒',
            'APP_DownloadProgress': 'app.huawei.motor:id/ota_upper_process_text_num',
            'APP_Countdown_Time': 'app.huawei.motor:id/ota_upper_countdown_text_num',
            'APP_Update_Exit': 'app.huawei.motor:id/hwappbarpattern_navigation_icon',
            'APP_Open_AirCondition': "app.huawei.motor:id/ac_card_switch",
            'APP_airCycle': 'app.huawei.motor:id/air_img',
            'APP_airPurifying': 'app.huawei.motor:id/purifier_img',
            'APP_XPATHhot': '//*[@resource-id="app.huawei.motor:id/master_hot_vent_btn"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView[1]',
            'APP_XPATHair': '//*[@resource-id="app.huawei.motor:id/master_hot_vent_btn"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView[2]',
            'APP_Download_Now': 'app.huawei.motor:id/ota_btn_download_now',
            'APP_Ota_Check_Cancel': 'app.huawei.motor:id/ota_check_cancel',
            'APP_Car_Lock': '//*[@resource-id="app.huawei.motor:id/layout_car_ctrl_btn_list_view"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]',
            'APP_hw_bottom_main': '//*[@resource-id="app.huawei.motor:id/app_hw_bottom_main"]/android.widget.LinearLayout[5]/android.widget.ImageView[1]',
            'APP_mine_top_scan': '//*[@resource-id="app.huawei.motor:id/mine_top_scan"]',
            'APP_hwappbarpattern_third_icon': '//*[@resource-id="app.huawei.motor:id/hwappbarpattern_third_icon"]',
            'APP_RelativeLayout': '//androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]',
            'APP_head_select_right': '//*[@resource-id="com.android.gallery3d:id/head_select_right"]',
            'APP_auth_login': '//*[@resource-id="app.huawei.motor:id/auth_login"]',
            'APP_btn_login': '//*[@resource-id="com.huawei.hms.account:id/btn_login"]',
            'path_mobile_phone': '/storage/emulated/0/Pictures/Screenshots/',
            'APP_mounting_name': '-a Intent.ACTION_MEDIA_MOUNTED -d "file:///sdcard"',
            "APP_filemanager": 'com.huawei.filemanager'

        },
        'wwx1275683': {
            'APP_LatestVersion': '已是最新版本',  # App提示无升级任务
            'APP_MainButton': '//*[@resource-id="app.huawei.motor:id/app_hw_bottom_main"]/android.widget.LinearLayout[3]/android.widget.ImageView[1]',
            # 主界面
            'APP_UpdatePage': '当前版本',
            'APP_AppointmentUpgrade': '预约更新',
            'APP_SureButton': '确定',
            'APP_UpdatePageButton': '车辆软件版本',
            'APP_ClickBlank': [0.977, 0.011],
            'APP_CheckUpdates': '检查更新',
            'APP_KnowButton': '知道了',
            'APP_CancelOrderUpgrade': '取消预约',
            'APP_NotUpdateButton': "暂不更新",
            'APP_DropDownMenu': [0.957, 0.014, 0.514, 0.248],
            'APP_WifiReRule': r'content-desc="WLAN,(.*?)。"',
            'APP_WifiSwitch': [594, 348],
            'APP_DropUpMenu': [0.316, 0.83, 0.614, 0.498],
            'APP_UpdateButton': "立即更新",
            'APP_CountdownContent': 'app.huawei.motor:id/ota_countdown_text_end',  # 倒计时提示内容
            'APP_CancelCountdownButton': 'app.huawei.motor:id/ota_column_cancel_install',  # 取消倒计时按钮
            'APP_PackageName': 'app.huawei.motor',  # app包名
            'APP_ClearNotification': 'com.android.systemui:id/delete',  # app包名
            'APP_ScheduleInfo': 'app.huawei.motor:id/ota_upper_appointment_time_user',
            'APP_ScheduleMinute': [-2, ''],  # app定时时间分钟位置区域
            'APP_Schedule12Hour': [-5, -3],  # app定时时间小时-12制式位置区域
            'APP_Schedule24Hour': [2, 4],  # app定时时间小时-24制式位置区域
            'APP_NowTimingRE': r'resource-id="app.huawei.motor:id/hwadvancednumberpicker_textview.*?content-desc="(.*)"'
                               r' checkable="false"',
            'APP_12HourUp': [650, 1650],
            'APP_12HourDown': [650, 1950],
            'APP_12MinuteUp': [900, 1650],
            'APP_12MinuteDown': [900, 1550],
            'APP_24HourUp': [888, 388],
            'APP_24HourDown': [888, 580],
            'APP_24MinuteUp': [1064, 388],
            'APP_24MinuteDown': [1064, 580],
            'APP_DropDownWindow': [0, 2000, 0, 1000],
            'APP_Notification': '车辆升级提醒',
            'APP_DownloadProgress': 'app.huawei.motor:id/ota_upper_process_text_num',
            'APP_Countdown_Time': 'app.huawei.motor:id/ota_upper_countdown_text_num',
            'APP_Update_Exit': 'app.huawei.motor:id/hwappbarpattern_navigation_icon',
            'APP_Open_AirCondition': "app.huawei.motor:id/ac_card_switch",
            'APP_airCycle': 'app.huawei.motor:id/air_img',
            'APP_airPurifying': 'app.huawei.motor:id/purifier_img',
            'APP_XPATHhot': '//*[@resource-id="app.huawei.motor:id/master_hot_vent_btn"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView[1]',
            'APP_XPATHair': '//*[@resource-id="app.huawei.motor:id/master_hot_vent_btn"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.ImageView[2]',
            'APP_Download_Now': 'app.huawei.motor:id/ota_btn_download_now',
            'APP_Ota_Check_Cancel': 'app.huawei.motor:id/ota_check_cancel',
            'APP_Car_Lock': '//*[@resource-id="app.huawei.motor:id/layout_car_ctrl_btn_list_view"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]',
            'APP_hw_bottom_main': '//*[@resource-id="app.huawei.motor:id/app_hw_bottom_main"]/android.widget.LinearLayout[5]/android.widget.ImageView[1]',
            'APP_mine_top_scan': '//*[@resource-id="app.huawei.motor:id/mine_top_scan"]',
            'APP_hwappbarpattern_third_icon': '//*[@resource-id="app.huawei.motor:id/hwappbarpattern_third_icon"]',
            'APP_RelativeLayout': '//*[@resource-id="com.sec.android.gallery3d:id/my_recycler_view"]/android.widget.FrameLayout[1]/android.widget.FrameLayout[1]',
            'APP_head_select_right': '//*[@resource-id="com.android.gallery3d:id/head_select_right"]',
            'APP_auth_login': '//*[@resource-id="app.huawei.motor:id/auth_login"]',
            'APP_btn_login': '//*[@resource-id="com.huawei.hms.account:id/btn_login"]',
            'path_mobile_phone': '/storage/self/primary/DCIM/Screenshots/',
            'APP_mounting_name': '-a android.intent.action.MEDIA_SCANNER_SCAN_FILE -d "file:///sdcard"',
            "APP_filemanager": 'com.sec.android.app.launcher'
        },
    },
    'F2': {
        'l30034136': {
            'APP_LatestVersion': '已是最新版本',  # App提示无升级任务
            'APP_MainButton': '//*[@resource-id="app.huawei.motor:id/app_hw_bottom_main"]/android.widget.LinearLayout[3]/android.widget.ImageView[1]',
            # 主界面
            'APP_UpdatePage': '当前版本',
            'APP_AppointmentUpgrade': '预约更新',
            'APP_SureButton': '确定',
            'APP_UpdatePageButton': '车辆软件版本',
            'APP_ClickBlank': [0.977, 0.011],
            'APP_CheckUpdates': '检查更新',
            'APP_KnowButton': '知道了',
            'APP_CancelOrderUpgrade': '取消预约',
            'APP_NotUpdateButton': "暂不更新",
            'APP_DropDownMenu': [0.957, 0.014, 0.514, 0.248],
            'APP_WifiReRule': r'content-desc="WLAN,(.*?)。"',
            'APP_WifiSwitch': [594, 348],
            'APP_DropUpMenu': [0.316, 0.83, 0.614, 0.498],
            'APP_UpdateButton': "立即更新",
            'APP_CountdownContent': 'app.huawei.auto:id/ota_countdown_text_end',  # 倒计时提示内容
            'APP_CancelCountdownButton': 'app.huawei.auto:id/ota_column_cancel_install',  # 取消倒计时按钮
            'APP_PackageName': 'app.huawei.auto',  # app包名
            'APP_ClearNotification': 'com.android.systemui:id/delete',  # app包名
            'APP_ScheduleInfo': 'app.huawei.auto:id/ota_upper_appointment_time_user',
            'APP_ScheduleMinute': [-2, ''],  # app定时时间分钟位置区域
            'APP_Schedule12Hour': [-5, -3],  # app定时时间小时-12制式位置区域
            'APP_Schedule24Hour': [2, 4],  # app定时时间小时-24制式位置区域
            'APP_NowTimingRE': r'resource-id="app.huawei.auto:id/hwadvancednumberpicker_textview.*?content-desc="(.*)"'
                               r' checkable="false"',
            'APP_12HourUp': [540, 1380],
            'APP_12HourDown': [540, 1752],
            'APP_12MinuteUp': [786, 1380],
            'APP_12MinuteDown': [786, 1752],
            'APP_24HourUp': [888, 388],
            'APP_24HourDown': [888, 580],
            'APP_24MinuteUp': [1064, 388],
            'APP_24MinuteDown': [1064, 580],
            'APP_DropDownWindow': [0, 2000, 0, 1000],
            'APP_Notification': '车辆升级提醒',
            'APP_DownloadProgress': 'app.huawei.motor:id/ota_upper_process_text_num',
            'APP_Countdown_Time': 'app.huawei.auto:id/ota_upper_countdown_text_num',
            'APP_Update_Exit': 'app.huawei.auto:id/hwappbarpattern_navigation_icon',
            'APP_Download_Now': 'app.huawei.motor:id/ota_btn_download_now',
            'APP_Ota_Check_Cancel': 'app.huawei.motor:id/ota_check_cancel',
            'APP_Car_Lock': '//*[@resource-id="app.huawei.motor:id/layout_car_ctrl_btn_list_view"]/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.RelativeLayout[1]',
            'APP_hw_bottom_main': '//*[@resource-id="app.huawei.motor:id/app_hw_bottom_main"]/android.widget.LinearLayout[5]/android.widget.ImageView[1]',
            'APP_mine_top_scan': '//*[@resource-id="app.huawei.motor:id/mine_top_scan"]',
            'APP_hwappbarpattern_third_icon': '//*[@resource-id="app.huawei.motor:id/hwappbarpattern_third_icon"]',
            'APP_RelativeLayout': '//androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]',
            'APP_head_select_right': '//*[@resource-id="com.android.gallery3d:id/head_select_right"]',
            'APP_auth_login': '//*[@resource-id="app.huawei.motor:id/auth_login"]',
            'APP_btn_login': '//*[@resource-id="com.huawei.hms.account:id/btn_login"]',
            'path_mobile_phone': '/storage/emulated/0/Pictures/Screenshots/',
            'APP_mounting_name': '-a Intent.ACTION_MEDIA_MOUNTED -d "file:///sdcard"',
            "APP_filemanager": 'com.huawei.filemanager'

        },

    },
}
ac = APP_CONFIG.get(PROJECT).get(TEST_ENV_FLAG)
# 接口值提取变量
APP_MainButton = ac.get('APP_MainButton')
# 判断是否在车辆升级页面
APP_UpdatePage = ac.get('APP_UpdatePage')
# 设置定时时间按钮
APP_AppointmentUpgrade = ac.get('APP_AppointmentUpgrade')
# 确定按钮
APP_SureButton = ac.get('APP_SureButton')
# 检查更新-车辆软件版本
APP_UpdatePageButton = ac.get('APP_UpdatePageButton')
# 点击空白处
APP_ClickBlank = ac.get('APP_ClickBlank')
# 检查更新
APP_CheckUpdates = ac.get('APP_CheckUpdates')
# 点击知道了按钮
APP_KnowButton = ac.get('APP_KnowButton')
# 取消预约按钮
APP_CancelOrderUpgrade = ac.get('APP_CancelOrderUpgrade')
# 最新版本
APP_LatestVersion = ac.get('APP_LatestVersion')
# 上拉菜单
APP_DropUpMenu = ac.get('APP_DropUpMenu')
# 下拉菜单
APP_DropDownMenu = ac.get('APP_DropDownMenu')
# wifi正则
APP_WifiReRule = ac.get('APP_WifiReRule')
# wifi开关坐标
APP_WifiSwitch = ac.get('APP_WifiSwitch')
# 暂不更新按钮
APP_NotUpdateButton = ac.get('APP_NotUpdateButton')
# 立即更新按钮
APP_UpdateButton = ac.get('APP_UpdateButton')
# 倒计时提示内容
APP_CountdownContent = ac.get('APP_CountdownContent')
# 取消倒计时按钮
APP_CancelCountdownButton = ac.get('APP_CancelCountdownButton')
# app包名
APP_PackageName = ac.get('APP_PackageName')
# 清除通知
APP_ClearNotification = ac.get('APP_ClearNotification')
# App预约升级时间信息
APP_ScheduleInfo = ac.get('APP_ScheduleInfo')
# app定时时间分钟位置区域
APP_ScheduleMinute = ac.get('APP_ScheduleMinute')
# app定时时间小时-12制式位置区域
APP_Schedule12Hour = ac.get('APP_Schedule12Hour')
# app定时时间小时-24制式位置区域
APP_Schedule24Hour = ac.get('APP_Schedule24Hour')
# app获取界面初始化时间正则
APP_NowTimingRE = ac.get('APP_NowTimingRE')
# 12制小时上方坐标
APP_12HourUp = ac.get('APP_12HourUp')
# 12制小时下方坐标
APP_12HourDown = ac.get('APP_12HourDown')
# 12制分钟上方坐标
APP_12MinuteUp = ac.get('APP_12MinuteUp')
# 12制分钟下方坐标
APP_12MinuteDown = ac.get('APP_12MinuteDown')
# 24制小时上方坐标
APP_24HourUp = ac.get('APP_24HourUp')
# 24制小时下方坐标
APP_24HourDown = ac.get('APP_24HourDown')
# 24制分钟上方坐标
APP_24MinuteUp = ac.get('APP_24MinuteUp')
# 24制分钟下方坐标
APP_24MinuteDown = ac.get('APP_24MinuteDown')
# 关闭下拉窗口坐标
APP_DropDownWindow = ac.get('APP_DropDownWindow')
# 关闭下拉窗口坐标
APP_Notification = ac.get('APP_Notification')
# 倒计时使时间
APP_Countdown_Time = ac.get('APP_Countdown_Time')
# 升级界面退出按钮
APP_Update_Exit = ac.get('APP_Update_Exit')
# APP下载进度
APP_DownloadProgress = ac.get('APP_DownloadProgress')
# 条件检查失败界面暂不更新
APP_Ota_Check_Cancel = ac.get('APP_Ota_Check_Cancel')
# APP立即下载
APP_Download_Now = ac.get('APP_Download_Now')
# APP远控空调
APP_Open_AirCondition = ac.get('APP_Open_AirCondition')
# 车锁按钮（XPath）
APP_Car_Lock = ac.get('APP_Car_Lock')
# 点击空气循环
APP_airCycle = ac.get('APP_airCycle')
# 点击空气净化
APP_airPurifying = ac.get('APP_airPurifying')
# 点击主驾座椅加热
APP_XPATHhot = ac.get('APP_XPATHhot')
# 点击主驾座椅通风
APP_XPATHair = ac.get('APP_XPATHair')
# 我的
APP_hw_bottom_main = ac.get('APP_hw_bottom_main')
# 扫一扫图标
APP_mine_top_scan = ac.get('APP_mine_top_scan')
# 图片图标
APP_hwappbarpattern_third_icon = ac.get('APP_hwappbarpattern_third_icon')
# 第一张图片
APP_RelativeLayout = ac.get('APP_RelativeLayout')
# 确认选择图片
APP_head_select_right = ac.get('APP_head_select_right')
# 确认登录
APP_auth_login = ac.get('APP_auth_login')
# 确认使用当前登录华为账号
APP_btn_login = ac.get('APP_btn_login')
# 获取手机图片路径地址
APP_mobile_phone = ac.get('path_mobile_phone')
# 截图导入手机后重新挂载
APP_mounting_name = ac.get('APP_mounting_name')
# 打开app文件管理
APP_filemanager = ac.get('APP_filemanager')

"""====================================================HMI_CTRL参数=================================================="""
# HMI接口
HMI_CONFIG = {
    'X2': {
        'HMI_MenuButton': 'com.android.systemui:id/toolbar_home_icon',  # 菜单栏resource-id
        'HMI_MenuPage': "应用与服务",
        'HMI_CountDown': [960, 750],
        'HMI_MenuUp': [136, 750, 136, 250],
        'HMI_ScreenPop': '将本机屏幕有线连接至其他设备',
        'HMI_QueryNewVersion': '系统更新',
        'HMI_AgreeButton': '同意',
        'HMI_KnowButton': '知道了',
        'HMI_SureButton': '确定',
        'HMI_UpdatePage': '更新与重置',
        'HMI_UpdatePageButton': '系统',
        'HMI_CTLCPop': 'CTLC纯电续航',
        'HMI_CTLCRight': [300, 600, 1800, 600],
        'HMI_SystemSetting': [295, 800],  # 系统设置
        'HMI_TouchPop': '碰一碰功能需要开启蓝牙',
        'HMI_TouchStartButton': '开启',
        'HMI_MenuConnectButton': '连接',
        'HMI_WifiState': (1370, 130, 1485, 210),
        'HMI_WifiClonePng': 'X2_wifi_close.png',
        'HMI_WifiButton': [1293, 174],
        'HMI_NotUpdateButton': "暂不更新",
        'HMI_UpdateButton': "立即更新",
        'HMI_WeakReminderButton': [423, 45],
        'HMI_TimeTypeButton': '语言和时间',
        'HMI_ExitingDownload': [544, 96],
        'HMI_DownloadProgress': 'com.huawei.android.hwouc:id/progress_tv',
        'HMI_AppointmentUpgrade': '预约更新',  # 设置定时时间按钮
        'HMI_ArvoButton': [830, 425],  # 下午按钮
        'HMI_NowTimingRE': 'resource-id="com.huawei.android.hwouc:id/hwadvancednumberpicker_textview.*?'
                           'content-desc="(.*)" checkable="false"',
        'HMI_DayButton': [712, 388],  # 今天按钮
        'HMI_HourUp': [888, 388],  # 小时上方坐标
        'HMI_HourDown': [888, 580],  # 小时下方坐标
        'HMI_MinuteUp': [1064, 388],  # 分钟上方坐标
        'HMI_MinuteDown': [1064, 580],  # 分钟下方坐标
        'HMI_NoticeButton': [164, 16],
        'HMI_Blank_Point': [136, 850],
        'HMI_UpdatePlan': '点击设置更新计划',
        'HMI_UpdateInfoButton': '查看新版本功能介绍、 系统更新服务条款',
        'HMI_UpdateInfo': '//*[@resource-id="com.huawei.android.hwouc:id/changelog_tv"]',
        'HMI_UpdateVersion': '//*[@resource-id="com.huawei.android.hwouc:id/version_tv"]',
        'HMI_CancelOrderUpgrade': '取消预约',  # 取消定时预约
        'HMI_CancelCurrentOrderUpgrade': 'com.huawei.android.hwouc:id/hw_btn_negative',  # 取消当前预约界面的预约定时
        'HMI_ClickCountDown': 'com.huawei.android.hwouc:id/count_down_tv',  # 点击倒计时
        'HMI_ScheduleTime': '//*[@resource-id="com.huawei.android.hwouc:id/appointment_info_tv"]',  # 获取定时时间
        'HMI_UpdateNoticeText': 'com.huawei.android.hwouc:id/update_notice_text',  # 自动更新更新时间
        'HMI_QueryNewVersionSet': '系统更新设置',  # 系统更新设置
        'HMI_Guest_Mode': 'com.huawei.ivi.usercenter:id/cancel_hos4',  # 访客模式
        'HMI_Auto_Download_Switch': '//*[@resource-id="com.huawei.android.hwouc:id/auto_download_switch"]',  # 自动下载按钮
        'HMI_iv_qr_finish_hos4': '//*[@resource-id="com.huawei.ivi.usercenter:id/iv_qr_finish_hos4"]',  # 刷写二维码
        'HMI_qr_image_hos4': '//*[@resource-id="com.huawei.ivi.usercenter:id/qr_image_hos4"]',  # 二维码
        'HMI_hw_btn_positive': '//*[@resource-id="com.huawei.android.hwouc:id/hw_btn_positive"]',  # 点击立即下载
    },
    'F2': {
        'HMI_MenuButton': 'com.android.systemui:id/toolbar_home_icon',  # 菜单栏resource-id
        'HMI_MenuPage': "应用与服务",
        'HMI_CountDown': [700, 692],
        'HMI_MenuUp': [136, 750, 136, 250],
        'HMI_ScreenPop': '将本机屏幕有线连接至其他设备',
        'HMI_QueryNewVersion': '系统更新',
        'HMI_AgreeButton': '同意',
        'HMI_KnowButton': '知道了',
        'HMI_SureButton': '确定',
        'HMI_UpdatePage': '更新与重置',
        'HMI_UpdatePageButton': '系统',
        'HMI_CTLCPop': 'CTLC纯电续航',
        'HMI_CTLCRight': [300, 600, 1800, 600],
        'HMI_SystemSetting': [295, 800],  # 系统设置
        'HMI_TouchPop': '碰一碰功能需要开启蓝牙',
        'HMI_TouchStartButton': '开启',
        'HMI_MenuConnectButton': '连接',
        'HMI_WifiState': (1370, 130, 1485, 210),
        'HMI_WifiClonePng': 'X2_wifi_close.png',
        'HMI_WifiButton': [1293, 174],
        'HMI_NotUpdateButton': "暂不更新",
        'HMI_UpdateButton': "立即更新",
        'HMI_WeakReminderButton': [423, 45],
        'HMI_TimeTypeButton': '语言和时间',
        'HMI_ExitingDownload': [544, 96],
        'HMI_DownloadProgress': 'com.huawei.android.hwouc:id/progress_tv',
        'HMI_AppointmentUpgrade': '预约更新',  # 设置定时时间按钮
        'HMI_ArvoButton': [830, 425],  # 下午按钮
        'HMI_NowTimingRE': 'resource-id="com.huawei.android.hwouc:id/hwadvancednumberpicker_textview.*?'
                           'content-desc="(.*)" checkable="false"',
        'HMI_DayButton': [712, 388],  # 今天按钮
        'HMI_HourUp': [888, 388],  # 小时上方坐标
        'HMI_HourDown': [888, 580],  # 小时下方坐标
        'HMI_MinuteUp': [1064, 388],  # 分钟上方坐标
        'HMI_MinuteDown': [1064, 580],  # 分钟下方坐标
        'HMI_NoticeButton': [164, 16],
        'HMI_Blank_Point': [136, 850],
        'HMI_UpdatePlan': '点击设置更新计划',
        'HMI_UpdateInfoButton': '查看新版本功能介绍、 系统更新服务条款',
        'HMI_UpdateInfo': '//*[@resource-id="com.huawei.android.hwouc:id/changelog_tv"]',
        'HMI_UpdateVersion': '//*[@resource-id="com.huawei.android.hwouc:id/version_tv"]',
        'HMI_CancelOrderUpgrade': '取消预约',  # 取消定时预约
        'HMI_CancelCurrentOrderUpgrade': 'com.huawei.android.hwouc:id/hw_btn_negative',  # 取消当前预约界面的预约定时
        'HMI_ClickCountDown': 'com.huawei.android.hwouc:id/count_down_tv',  # 点击倒计时
        'HMI_ScheduleTime': '//*[@resource-id="com.huawei.android.hwouc:id/appointment_info_tv"]',  # 获取定时时间
        'HMI_UpdateNoticeText': 'com.huawei.android.hwouc:id/update_notice_text',  # 自动更新更新时间
        'HMI_QueryNewVersionSet': '系统更新设置',  # 系统更新设置
        'HMI_Guest_Mode': 'com.huawei.ivi.usercenter:id/cancel_hos4',  # 访客模式
        'HMI_Auto_Download_Switch': '//*[@resource-id="com.huawei.android.hwouc:id/auto_download_switch"]',  # 自动下载按钮
        'HMI_iv_qr_finish_hos4': '//*[@resource-id="com.huawei.ivi.usercenter:id/iv_qr_finish_hos4"]',  # 刷写二维码
        'HMI_qr_image_hos4': '//*[@resource-id="com.huawei.ivi.usercenter:id/qr_image_hos4"]',  # 二维码
        'HMI_hw_btn_positive': '//*[@resource-id="com.huawei.android.hwouc:id/hw_btn_positive"]',  # 点击立即下载
    },
    'X1': {
        'HMI_UpdateVersion': '//*[@resource-id="com.huawei.android.hwouc:id/version_tv"]',
        'HMI_CancelOrderUpgrade': '取消预约',  # 取消定时预约
        'HMI_ClickCountDown': 'com.huawei.android.hwouc:id/count_down_tv',  # 点击倒计时
    }
}

# HMI菜单按钮
HMI_MenuButton = HMI_CONFIG.get(PROJECT).get('HMI_MenuButton')
# HMI菜单页面
HMI_MenuPage = HMI_CONFIG.get(PROJECT).get('HMI_MenuPage')
# 倒计时按钮
HMI_CountDown = HMI_CONFIG.get(PROJECT).get('HMI_CountDown')
# 检查更新
HMI_QueryNewVersion = HMI_CONFIG.get(PROJECT).get('HMI_QueryNewVersion')
# 系统设置
HMI_SystemSetting = HMI_CONFIG.get(PROJECT).get('HMI_SystemSetting')
# 更新页面
HMI_UpdatePage = HMI_CONFIG.get(PROJECT).get('HMI_UpdatePage')
# 更新页面按钮
HMI_UpdatePageButton = HMI_CONFIG.get(PROJECT).get('HMI_UpdatePageButton')
# 获取定时时间
HMI_ScheduleTime = HMI_CONFIG.get(PROJECT).get('HMI_ScheduleTime')
# HMI同意按钮
HMI_AgreeButton = HMI_CONFIG.get(PROJECT).get('HMI_AgreeButton')
# HMI菜单栏上滑
HMI_MenuUp = HMI_CONFIG.get(PROJECT).get('HMI_MenuUp')
# HMI投屏弹窗
HMI_ScreenPop = HMI_CONFIG.get(PROJECT).get('HMI_ScreenPop')
# HMI知道了按钮
HMI_KnowButton = HMI_CONFIG.get(PROJECT).get('HMI_KnowButton')
# HMI CTLC弹窗
HMI_CTLCPop = HMI_CONFIG.get(PROJECT).get('HMI_CTLCPop')
# HMI CTLC弹窗右移
HMI_CTLCRight = HMI_CONFIG.get(PROJECT).get('HMI_CTLCRight')
# HMI 碰一碰开启弹窗
HMI_TouchPop = HMI_CONFIG.get(PROJECT).get('HMI_TouchPop')
# HMI 碰一碰开启弹窗开启按钮
HMI_TouchStartButton = HMI_CONFIG.get(PROJECT).get('HMI_TouchStartButton')
# HMI 连接菜单按钮
HMI_MenuConnectButton = HMI_CONFIG.get(PROJECT).get('HMI_MenuConnectButton')
# HMI wifi状态
HMI_WifiState = HMI_CONFIG.get(PROJECT).get('HMI_WifiState')
# HMI wifi关闭图片
HMI_WifiClonePng = HMI_CONFIG.get(PROJECT).get('HMI_WifiClonePng')
# HMI 暂不更新按钮
HMI_NotUpdateButton = HMI_CONFIG.get(PROJECT).get('HMI_NotUpdateButton')
# HMI 立即更新按钮
HMI_UpdateButton = HMI_CONFIG.get(PROJECT).get('HMI_UpdateButton')
# HMI 弱提示按钮
HMI_WeakReminderButton = HMI_CONFIG.get(PROJECT).get('HMI_WeakReminderButton')
# HMI 24小时制按钮
HMI_TimeTypeButton = HMI_CONFIG.get(PROJECT).get('HMI_TimeTypeButton')
# HMI 退出下载页面
HMI_ExitingDownload = HMI_CONFIG.get(PROJECT).get('HMI_ExitingDownload')
# HMI 退出下载页面
HMI_DownloadProgress = HMI_CONFIG.get(PROJECT).get('HMI_DownloadProgress')
# HMI 预约升级按钮
HMI_AppointmentUpgrade = HMI_CONFIG.get(PROJECT).get('HMI_AppointmentUpgrade')
# HMI wifi按钮
HMI_WifiButton = HMI_CONFIG.get(PROJECT).get('HMI_WifiButton')
# HMI 下午定时按钮
HMI_ArvoButton = HMI_CONFIG.get(PROJECT).get('HMI_ArvoButton')
# HMI 当前定时页面时间
HMI_NowTimingRE = HMI_CONFIG.get(PROJECT).get('HMI_NowTimingRE')
# HMI 当前定时页面天选择
HMI_DayButton = HMI_CONFIG.get(PROJECT).get('HMI_DayButton')
# HMI 当前定时页面小时向上选择
HMI_HourUp = HMI_CONFIG.get(PROJECT).get('HMI_HourUp')
# HMI 当前定时页面小时向下选择
HMI_HourDown = HMI_CONFIG.get(PROJECT).get('HMI_HourDown')
# HMI 当前定时页面分钟向上选择
HMI_MinuteUp = HMI_CONFIG.get(PROJECT).get('HMI_MinuteUp')
# HMI 当前定时页面分钟向下选择
HMI_MinuteDown = HMI_CONFIG.get(PROJECT).get('HMI_MinuteDown')
# HMI 当前定时页面确定按钮
HMI_SureButton = HMI_CONFIG.get(PROJECT).get('HMI_SureButton')
# HMI 通知按钮
HMI_NoticeButton = HMI_CONFIG.get(PROJECT).get('HMI_NoticeButton')
# HMI 更新通知
HMI_UpdatePlan = HMI_CONFIG.get(PROJECT).get('HMI_UpdatePlan')
# HMI 升级内容按钮
HMI_UpdateInfoButton = HMI_CONFIG.get(PROJECT).get('HMI_UpdateInfoButton')
# HMI 升级内容xpath
HMI_UpdateInfo = HMI_CONFIG.get(PROJECT).get('HMI_UpdateInfo')
# HMI 升级版本xpath
HMI_UpdateVersion = HMI_CONFIG.get(PROJECT).get('HMI_UpdateVersion')
# HMI 取消预约升级按钮
HMI_CancelOrderUpgrade = HMI_CONFIG.get(PROJECT).get('HMI_CancelOrderUpgrade')
# HMI 取消当前预约界面的预约定时按钮
HMI_CancelCurrentOrderUpgrade = HMI_CONFIG.get(PROJECT).get('HMI_CancelCurrentOrderUpgrade')
# HMI 点击倒计时
HMI_ClickCountDown = HMI_CONFIG.get(PROJECT).get('HMI_ClickCountDown')
# HMI 空白处退出弹窗坐标
HMI_Blank_Point = HMI_CONFIG.get(PROJECT).get('HMI_Blank_Point')
# 自动更新时间
HMI_UpdateNoticeText = HMI_CONFIG.get(PROJECT).get('HMI_UpdateNoticeText')
# 系统更新设置
HMI_QueryNewVersionSet = HMI_CONFIG.get(PROJECT).get('HMI_QueryNewVersionSet')
# 访客模式
HMI_Guest_Mode = HMI_CONFIG.get(PROJECT).get('HMI_Guest_Mode')
# 自动下载按钮
HMI_Auto_Download_Switch = HMI_CONFIG.get(PROJECT).get('HMI_Auto_Download_Switch')
# 刷新二维码
HMI_iv_qr_finish_hos4 = HMI_CONFIG.get(PROJECT).get('HMI_iv_qr_finish_hos4')
# 二维码
HMI_qr_image_hos4 = HMI_CONFIG.get(PROJECT).get('HMI_qr_image_hos4')
# 立即下载
HMI_hw_btn_positive = HMI_CONFIG.get(PROJECT).get('HMI_hw_btn_positive')
"""======================================================部件版本====================================================="""
# !!!!!!!!!!!!!!!!ATTENTION:如果下面的零部件软件有变更，需执行Functions/PART_VERSION.py重新创建自定义版本!!!!
# 零部件版本信息
PART_VERSION = {
    'X2': {
        's00566695': {
            'UPDATE_VERSION': 'SW', 'Vehicle_CHONGQIN_PRUSESS_ID': 'demo1',
            'Vehicle_CHONGQIN_0135_PRUSESS_ID': 'demo', 'UPDATE_CONTENT': 'X2',
            'UPDATE_DURATION': 11, 'Vehicle_CHONGQIN_0177_PRUSESS_ID': 'TBOX_BDC电源管理新版本',
            'TBOX_SW': 'TBOX_703001184AA_SW67.14.01_240126_HW8.1.2.zip',
            'TBOX_WRONG_SW': 'TBOX_703001184AA_SW67.14.01_240126_HW8.1.2.zip',
            'TBOX_BIGFILE': 'TBOX_703001184AA_SW67.14.01_240126_HW8.1.2.zip',
            'CDC_SW': 'CDC_703001183AA_SW01.05.71_240203_HW0.0.2_All.zip',
            'EPA_SW': 'EPA_703001175AA_SW00.01.25_231110_HW0.0.3.zip',
            'CDC_SMALL_SW': 'CDC_703001183AA_SW01.05.71_240203_HW0.0.2_All.zip',
            'CDC_DIFF_SW': 'CDC_703001183AA_SW01.05.71_240203_HW0.0.2_All.zip',
            'CDC_DIFF_WRONG_SW': 'CDC_703001183AA_SW01.05.71_240203_HW0.0.2_All.zip',
            'CDC_WRONG_SW': 'CDC_703001183AA_SW01.05.71_240203_HW0.0.2_All.zip',
            'MDC_SW': 'MDC_702000176AA_SW02.03.27_240203_All.zip',
            'MDC_Jump_SW': '跳转包MDC_702000176AA_SW99.99.03_231110_All.zip',
            'MDC_DIFF_SW': 'MDC_702000176AA_SW02.03.27_240203_All.zip',
            'MDC_DIFF_WRONG_SW': 'MDC_702000176AA_SW02.03.27_240203_All.zip',
            'MDC_WRONG_SW': 'MDC_702000176AA_SW02.03.27_240203_All.zip',
            'MDC_HOST_WRONG_ROLLBACK_SW': 'MDC_702000176AA_SW02.03.27_240203_All.zip',
            'MDC_INS_WRONG_ROLLBACK_SW': 'MDC_702000176AA_SW02.03.27_240203_All.zip',
            'MDC_RADAR_WRONG_ROLLBACK_SW': 'MDC_702000176AA_SW02.03.27_240203_All.zip',
            'VIU1_SW': 'VIU1_809000087AA_SW00.08.32_240202.zip',
            'VIU1_WRONG_SW': 'VIU1_809000087AA_SW00.08.32_240202.zip',
            'VIU2_SW': 'VIU2_809000088AA_SW00.08.32_240202.zip',
            'VIU2_WRONG_SW': 'VIU2_809000088AA_SW00.08.32_240202.zip',
            'VIU3_SW': 'VIU3_809000089AA_SW00.08.32_240202.zip',
            'VIU3_WRONG_SW': 'VIU3_809000089AA_SW00.08.32_240202.zip',
            'VDC_SW': 'VDC_809000086AA_SW00.05.04_240202_HW0.2.0.zip',
            'VDC_WRONG_SW': 'VDC_809000086AA_SW00.05.04_240202_HW0.2.0.zip',
            'TBOX_SW_LOW': '',
            'CDC_SW_LOW': '',
            'EPA_SW_LOW': '',
            'VIU1_SW_LOW': '',
            'VIU2_SW_LOW': '',
            'VIU3_SW_LOW': '',
            'VDC_SW_LOW': '',
        },
        'wwx1275683': {
            'UPDATE_VERSION': 'SW', 'Vehicle_CHONGQIN_PRUSESS_ID': 'demo1',
            'Vehicle_CHONGQIN_0135_PRUSESS_ID': 'demo', 'UPDATE_CONTENT': 'X2',
            'UPDATE_DURATION': 11, 'Vehicle_CHONGQIN_0177_PRUSESS_ID': 'TBOX_BDC电源管理新版本',
            'TBOX_SW': 'TEST_TBOX_703001184AA_SW67.14.01_240126.zip',
            'TBOX_SW_LOW': '【CI Testing】【1230】【debug】TBOX_703001184AA_SW67.13.02_231227.zip',
            'TBOX_ROLLBACK_SW': '【勿用，TBOX专用测试，篡改版本号】TBOX_703001184AA_SW67.12.03_231106_HW8.1.2.zip',
            'TBOX_WRONG_SW': '【勿用，TBOX专用测试，篡改版本号】TBOX_703001184AA_SW67.12.03_231106_HW8.1.2.zip',
            'TBOX_BIGFILE': 'DEVELOP_TBOX_703001184AA_SW67.13.01_231206_HW8.1.2.zip',
            'CDC_SW': '【2.B120】【odex】CDC_703001183AA_SW01.05.71_240203_HW0.0.2_All.zip',
            'CDC_SW_LOW': '【CI Testing】【1230】【odex】【11.B115】CDC_703001183AA_SW01.04.05_240124_HW0.0.2_All.zip',
            'CDC_SMALL_SW': '【CI Testing】【1230】【odex】【11.B115】CDC_703001183AA_SW01.04.05_240124_HW0.0.2_All.zip',
            'CDC_DIFF_SW': '【CI Testing】【1230】【odex】【11.B115】CDC_703001183AA_SW01.04.05_240124_HW0.0.2_All.zip',
            'CDC_DIFF_WRONG_SW': '【CI Testing】【1230】【odex】【11.B115】CDC_703001183AA_SW01.04.05_240124_HW0.0.2_All.zip',
            'CDC_ROLLBACK_SW': '【CI Testing】【1230】【odex】【11.B115】CDC_703001183AA_SW01.04.05_240124_HW0.0.2_All.zip',
            'CDC_Inside_DIFF_SW': '【CI Testing】【1230】【odex】【11.B115】CDC_703001183AA_SW01.04.05_240124_HW0.0.2_All.zip',
            'CDC_ALL_DIFF_SW': '【CI Testing】【1230】【odex】【11.B115】CDC_703001183AA_SW01.04.05_240124_HW0.0.2_All.zip',
            'CDC_WRONG_SW': '【CI Testing】【1230】【odex】【11.B115】CDC_703001183AA_SW01.04.05_240124_HW0.0.2_All.zip',
            'MDC_SW': '【CI Testing】【0130】【B040】【release】MDC_702000176AA_SW00.07.02_240203_All.zip',
            'MDC_SW_LOW': '【专用跳转包】MDC_702000176AA_SW99.99.04_231207_All.zip',
            'MDC_ROLLBACK_SW': '【CI Testing】【1230】【2.B060】【release】MDC_702000176AA_SW00.07.01_240122_All.zip',
            'MDC_DIFF_SW': '【CI Testing】【1230】【release】MDC_702000176AA_SW00.06.01_231228_All.zip',
            'MDC_DIFF_WRONG_SW': '【CI Testing】【1230】【release】MDC_702000176AA_SW00.06.01_231228_All.zip',
            'MDC_WRONG_SW': '【CI Testing】【1230】【2.B060】【release】MDC_702000176AA_SW00.07.01_240122_All.zip',
            'MDC_HOST_WRONG_ROLLBACK_SW': '【CI Testing】【1230】【release】MDC_702000176AA_SW00.06.01_231228_All.zip',
            'MDC_INS_WRONG_ROLLBACK_SW': '【CI Testing】【1230】【release】MDC_702000176AA_SW00.06.01_231228_All.zip',
            'MDC_RADAR_WRONG_ROLLBACK_SW': '【CI Testing】【1230】【release】MDC_702000176AA_SW00.06.01_231228_All.zip',
            'VIU1_SW': '【CI Testing】【0130】【1.B008】【develop】VIU1_809000087AA_SW00.08.32_240202.zip',
            'VIU1_SW_LOW': '【CI Testing】【1230】【1.B009】【develop】VIU1_809000087AA_SW00.08.30_240109.zip',
            'VIU1_WRONG_SW': '错误版本号VIU1_809000087AA_SW99.08.30_240109.zip',
            'VIU2_SW': '【CI Testing】【0130】【1.B008】【develop】VIU2_809000088AA_SW00.08.32_240202.zip',
            'VIU2_SW_LOW': '【CI Testing】【1230】【1.B009】【develop】VIU2_809000088AA_SW00.08.30_240109.zip',
            'VIU2_WRONG_SW': 'VIU2_809000088AA_SW00.08.26_231219.zip',
            'VIU3_SW': '【CI Testing】【0130】【1.B008】【develop】VIU3_809000089AA_SW00.08.32_240202.zip',
            'VIU3_SW_LOW': '【CI Testing】【1230】【1.B009】【develop】VIU3_809000089AA_SW00.08.30_240109.zip',
            'VIU3_WRONG_SW': 'VIU3_809000089AA_SW00.08.26_231219.zip',
            'VDC_SW': '【CI Testing】【0130】【1.B008】【develop】VDC_809000086AA_SW00.05.04_240202.zip',
            'VDC_SW_LOW': '【CI Testing】【1230】【2.B010】【develop】VDC_809000086AA_SW00.05.04_240124.zip',
            'VDC_WRONG_SW': '【CI Testing】【1230】【2.B010】【develop】VDC_809000086AA_SW00.05.04_240124.zip',
            'VDC_ROLLBACK': '【CI Testing】【1230】【2.B010】【develop】VDC_809000086AA_SW00.05.04_240124.zip',
            'ABM_SW': '【CI Tested】ABM_407000471AA_SW00.02.00_231031_HW0.1.1.zip',
            'BMS_SW': '【CI Testing】【0130】BMS_113000102AA_SW06.05.02_240205.zip',
            'BMS_SW_LOW': '【CI Testing】【1230】BMS_113000102AA_SW06.04.12_240103.zip',
            'BMS_SW_ERROR': 'ERROR_BMS_113000102AA_SW06.04.02_231216.zip',
            'BMS_SW_WRONG_VERSION': 'WrongVersion_BMS_113000102AA_SW06.04.02_231216',
            'CCU_SW': '【CI Testing】【1130】CCU_301001869AA_SW00.01.08_231205_HW0.1.2.zip',
            'CCU_SW_LOW': '【CI Testing】【1130】CCU_301001869AA_SW00.01.08_231205_HW0.1.2.zip',
            'CDS_SW': '【CI Tested】【1115】CDS_703001182AA_SW00.02.05_231110_HW0.0.2.zip',
            'CDS_SW_LOW': '【CI Tested】【1115】CDS_703001182AA_SW00.02.05_231110_HW0.0.2.zip',
            'CDU_SW': '【CI Testing】【1230】CDU_807000819AA_SW01.00.04_240125.zip',
            'CDU_SW_LOW': '【CI Testing】【1230】CDU_807000819AA_SW01.00.04_240125.zip',
            'CS_SW': '【CI Tested】CS_808001217AA_SW00.01.00_230804_HW0.0.1.zip',
            'CS_SW_LOW': '【CI Tested】CS_808001217AA_SW00.01.00_230804_HW0.0.1.zip',
            'ECAS_SW': '【CI Testing】【0130】ECAS_202001995AA_SW01.00.04_240202.zip',
            'ECAS_SW_LOW': '【CI Testing】【1230】ECAS_202001995AA_SW01.00.03_240101.zip',
            'EPA_SW': '【CI Testing】【1215】EPA_703001175AA_SW00.01.27_231216.zip',
            'EPA_SW_LOW': '【CI Testing】【1215】EPA_703001175AA_SW00.01.27_231216.zip',
            'EPB1_SW': '【CI Testing】【1230】EPB1_204002632AA_SW01.00.04_240104.zip',
            'EPB2_SW': '【CI Testing】【1230】EPB2_204002632AA_SW01.00.04_240104.zip',
            'EPB1_SW_LOW': '【CI Testing】【1230】EPB1_204002632AA_SW01.00.04_240104.zip',
            'EPB2_SW_LOW': '【CI Testing】【1230】EPB2_204002632AA_SW01.00.04_240104.zip',
            'EPS_SW': '【CI Testing】【1130】EPS_S0000001809_SW00.02.00_00.02.03_231116.zip',
            'EPS_SW_LOW': '【CI Testing】【1130】EPS_S0000001809_SW00.02.00_00.02.03_231116.zip',
            'FLML_SW': '【CI Testing】【1230】FLML_605000930AA_SW00.01.07_231226.zip',
            'FLML_SW_LOW': '【CI Testing】【1230】FLML_605000930AA_SW00.01.07_231226.zip',
            'FLMR_SW': '【CI Testing】【1230】FLMR_605000931AA_SW00.01.07_231226.zip',
            'FLMR_SW_LOW': '【CI Testing】【1230】FLMR_605000931AA_SW00.01.07_231226.zip',
            'IC_SW': 'IC_701000267AA_SW00.02.07_231120.zip',
            'IC_SW_LOW': 'IC_701000267AA_SW00.02.07_231120.zip',
            'IKM_SW': '【CI Testing】【0130】IKM_804000294AA_SW01.10.38_240201.zip',
            'IKM_SW_LOW': '【CI Testing】【1230】IKM_804000294AA_SW01.10.34_240118.zip',
            'IPB_SW': '【CI Testing】【1130】IPB_207000310AA_SW01.00.01_231202_HW0.0.1.zip',
            'IPB_SW_LOW': '【CI Testing】【1130】IPB_207000310AA_SW01.00.01_231202_HW0.0.1.zip',
            'LBMS_SW': '【CI Testing】【0130】LBMS_807000836AA_SW00.11.00_240204.zip',
            'LBMS_SW_LOW': '【CI Testing】【1130】LBMS_807000836AA_SW00.10.00_231204_HW0.4.0.zip',
            'MCUF_SW': '【CI Testing】【0130】MCUF_112000230AA_SW00.03.05_00.03.05_240131.zip',
            'MCUF_SW_LOW': '【CI Tested】【1115】MCUF_112000230AA_SW00.03.02_00.03.02_231116_HW0.2.0.zip',
            'MCUR_SW': '【CI Testing】【0130】MCUR_112000229AA_SW00.03.05_00.03.05_240131.zip',
            'MCUR_SW_LOW': '【CI Tested】【1115】MCUR_112000229AA_SW00.03.02_00.03.02_231116_HW0.2.0.zip',
            'PTC_SW': '【CI Testing】【1130】PTC_302001523AA_SW00.02.02_231206_HW0.1.1.zip',
            'PTC_SW_LOW': '【CI Testing】【1130】PTC_302001523AA_SW00.02.02_231206_HW0.1.1.zip',
            'TDU_SW': '【CI Testing】【0130】TDU_301001866AA_SW00.02.11_00.01.00_240129.zip',
            'TDU_SW_LOW': '【CI Testing】【1230】TDU_301001866AA_SW00.02.09_00.01.00_240103.zip',
            'TDU_SW_ERROR': '【ERROR】TDU_301001866AA_SW00.02.09_00.01.00_240103.zip',
            'TDU_SW_WRONG_VERSION': '【WrongVersion】TDU_301001866AA_SW00.02.09_00.01.00_240103.zip',
            'TPMS_SW': '【CI Testing】【1215】TPMS_802000395AA_SW00.01.14_231219_HW0.0.1.zip',
            'TPMS_SW_LOW': '【CI Testing】【1215】TPMS_802000395AA_SW00.01.14_231219_HW0.0.1.zip',
            'VAP_SW': '【CI Tested】【1215】VAP_301002287AA_SW00.01.00_231219_HW0.1.0.zip',
            'VAP_SW_LOW': '【CI Tested】【1215】VAP_301002287AA_SW00.01.00_231219_HW0.1.0.zip',
            'WCM_SW': '【CI Testing】【1230】WCM_802000313AA_SW00.01.10_240123.zip',
            'WCM_SW_LOW': '【CI Testing】【1230】WCM_802000313AA_SW00.01.10_240123.zip',
        },
    },
    'F2': {
        'l30034136': {
            'UPDATE_VERSION': 'SW', 'Vehicle_CHONGQIN_PRUSESS_ID': 'demo1',
            'Vehicle_CHONGQIN_0135_PRUSESS_ID': 'demo', 'UPDATE_CONTENT': 'F2',
            'UPDATE_DURATION': 11, 'Vehicle_CHONGQIN_0177_PRUSESS_ID': 'TBOX_BDC电源管理新版本',
            'TBOX_SW': 'TBOX_7900010-RL01_SW1.14.B_230915_8224_01.zip',
            'TBOX_WRONG_SW': 'TBOX_7900010-RL01_SW1.14.B_230915_8224_01.zip',
            'TBOX_BIGFILE': 'TBOX_7900010-RL01_SW1.14.B_230915_8224_01.zip',
            'CDC_SW': 'TBOX_7900010-RL01_SW1.14.B_230915_8224_01.zip',
            'CDC_SMALL_SW': 'TBOX_7900010-RL01_SW1.14.B_230915_8224_01.zip',
            'CDC_DIFF_SW': 'TBOX_7900010-RL01_SW1.14.B_230915_8224_01.zip',
            'CDC_DIFF_WRONG_SW': 'TBOX_7900010-RL01_SW1.14.B_230915_8224_01.zip',
            'CDC_WRONG_SW': 'TBOX_7900010-RL01_SW1.14.B_230915_8224_01.zip',
            'MDC_SW': 'TBOX_7900010-RL01_SW1.14.B_230915_8224_01.zip',
            'MDC_DIFF_SW': 'TBOX_7900010-RL01_SW1.14.B_230915_8224_01.zip',
            'MDC_DIFF_WRONG_SW': 'TBOX_7900010-RL01_SW1.14.B_230915_8224_01.zip',
            'MDC_WRONG_SW': 'TBOX_7900010-RL01_SW1.14.B_230915_8224_01.zip',
            'MDC_HOST_WRONG_ROLLBACK_SW': 'TBOX_7900010-RL01_SW1.14.B_230915_8224_01.zip',
            'MDC_INS_WRONG_ROLLBACK_SW': 'TBOX_7900010-RL01_SW1.14.B_230915_8224_01.zip',
            'MDC_RADAR_WRONG_ROLLBACK_SW': 'TBOX_7900010-RL01_SW1.14.B_230915_8224_01.zip',
            # 'VIU1_SW': 'VIU1_2108101-RN01_SW2.40.B_230914_8224_00.zip',
            'VIU1_SW': 'TBOX_7900010-RL01_SW1.14.B_230915_8224_01.zip',
            'VIU1_WRONG_SW': '',
            # 'VIU2_SW': 'VIU2_2108102-RN01_SW2.40.B_230914_8224_00.zip',
            'VIU2_SW': 'TBOX_7900010-RL01_SW1.14.B_230915_8224_01.zip',
            'VIU2_WRONG_SW': '',
            # 'VIU3_SW': 'VIU3_2108104-RN01_SW2.40.B_230914_8224_00.zip',
            'VIU3_SW': 'TBOX_7900010-RL01_SW1.14.B_230915_8224_01.zip',
            'VIU3_WRONG_SW': '',
            # 'VDC_SW': 'VDC_2108001-RN01_SW2.10.C_230921_8224_51.zip',
            'VDC_SW': 'TBOX_7900010-RL01_SW1.14.B_230915_8224_01.zip',
            'VDC_WRONG_SW': '',
        },
    },
}

pv = PART_VERSION.get(PROJECT).get(TEST_ENV_FLAG)
# 升级版本
UPDATE_VERSION = pv.get('UPDATE_VERSION')
# 升级版本
Vehicle_CHONGQIN_PRUSESS_ID = pv.get('Vehicle_CHONGQIN_PRUSESS_ID')
# 升级版本
Vehicle_CHONGQIN_0135_PRUSESS_ID = pv.get('Vehicle_CHONGQIN_0135_PRUSESS_ID')
# 升级说明
UPDATE_CONTENT = pv.get('UPDATE_CONTENT')
# 升级时长
UPDATE_DURATION = pv.get('UPDATE_DURATION')
Vehicle_yace_SW_ID = pv.get('Vehicle_yace_SW_ID')

"""======================================================版本包参数====================================================="""
# 自定义版本包
CUSTOM_VERSION = {
    'X2': {
        's00566695': {
            'Vehicle_VDC_SW_ID': f'Vehicle_VDC_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_VDC_ROLLBACK_SW_ID': f'Vehicle_VDC_ROLLBACK_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_VDC_DOMAIN_SW_ID': f'Vehicle_VDC_DOMAIN_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_VDC_DOMAIN_ROLLBACK_SW_ID': f'Vehicle_VDC_DOMAIN_ROLLBACK_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_VIU1_SW_ID': f'Vehicle_VIU1_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_VIU2_SW_ID': f'Vehicle_VIU2_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_VIU3_SW_ID': f'Vehicle_VIU3_SW_ID_{TEST_ENV_FLAG}',

            'Vehicle_TBOX_SW_ID': f'Vehicle_TBOX_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_TBOX_ROLLBACK_SW_ID': f'Vehicle_TBOX_ROLLBACK_SW_ID_{TEST_ENV_FLAG}',

            'Vehicle_CDC_SW_ID': f'Vehicle_CDC_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_CDC_ROLLBACK_SW_ID': f'Vehicle_CDC_ROLLBACK_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_CDC_All_SW_ID': f'Vehicle_CDC_All_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_CDC_Inside_DIFF_SW_ID': f'Vehicle_CDC_Inside_DIFF_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_CDC_All_DIFF_SW_ID': f'Vehicle_CDC_All_DIFF_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_CDC_All_DIFF_ERROR_SW_ID': f'Vehicle_CDC_All_DIFF_ERROR_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_CDC_BJ_SW_ID': f'Vehicle_CDC_BJ_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_CDC_IVI_FAULT_SW_ID': f'Vehicle_CDC_IVI_FAULT_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_CDC_Inside_FAULT_SW_ID': f'Vehicle_CDC_Inside_FAULT_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_CDC_Inside_FAULT_SW_ID': f'Vehicle_CDC_Inside_FAULT_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_EPA_SW_ID': f'Vehicle_EPA_SW_ID_{TEST_ENV_FLAG}',

            'Vehicle_MDC_SW_ID': f'Vehicle_MDC_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_MDC_Jump_SW_ID': f'Vehicle_MDC_Jump_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_MDC_ROLLBACK_SW_ID': f'Vehicle_MDC_ROLLBACK_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_MDC_All_SW_ID': f'Vehicle_MDC_All_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_MDC_DIFF_SW_ID': f'Vehicle_MDC_DIFF_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_MDC_DIFF_All_SW_ID': f'Vehicle_MDC_DIFF_All_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_MDC_All_DIFF_ERROR_SW_ID': f'Vehicle_MDC_All_DIFF_ERROR_SW_ID_{TEST_ENV_FLAG}',

            'Vehicle_HW_SW_ID': f'Vehicle_HW_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_All_SW_ID': f'Vehicle_All_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_TBOX_VDC_SW_ID': f'Vehicle_TBOX_VDC_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_ALL_Download_SW_ID': f'Vehicle_ALL_Download_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_ALL_Downgraded_SW_ID': f'Vehicle_ALL_Downgraded_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_LV_SW_ID': f'Vehicle_LV_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_HV_SW_ID': f'Vehicle_HV_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_HW_NO_CDC_SW_ID': f'Vehicle_HW_NO_CDC_SW_ID_{TEST_ENV_FLAG}',
        },
        'wwx1275683': {
            'Vehicle_VDC_SW_ID': f'Vehicle_VDC_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_VDC_ROLLBACK_SW_ID': f'Vehicle_VDC_ROLLBACK_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_VDC_DOMAIN_SW_ID': f'Vehicle_VDC_DOMAIN_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_VDC_DOMAIN_ROLLBACK_SW_ID': f'Vehicle_VDC_DOMAIN_ROLLBACK_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_VIU1_SW_ID': f'Vehicle_VIU1_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_VIU2_SW_ID': f'Vehicle_VIU2_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_VIU3_SW_ID': f'Vehicle_VIU3_SW_ID_{TEST_ENV_FLAG}',

            'Vehicle_TBOX_SW_ID': f'Vehicle_TBOX_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_TBOX_ROLLBACK_SW_ID': f'Vehicle_TBOX_ROLLBACK_SW_ID_{TEST_ENV_FLAG}',

            'Vehicle_CDC_SW_ID': f'Vehicle_CDC_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_CDC_ROLLBACK_SW_ID': f'Vehicle_CDC_ROLLBACK_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_CDC_All_SW_ID': f'Vehicle_CDC_All_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_CDC_Inside_DIFF_SW_ID': f'Vehicle_CDC_Inside_DIFF_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_CDC_All_DIFF_SW_ID': f'Vehicle_CDC_All_DIFF_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_CDC_All_DIFF_ERROR_SW_ID': f'Vehicle_CDC_All_DIFF_ERROR_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_CDC_BJ_SW_ID': f'Vehicle_CDC_BJ_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_CDC_IVI_FAULT_SW_ID': f'Vehicle_CDC_IVI_FAULT_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_CDC_Inside_FAULT_SW_ID': f'Vehicle_CDC_Inside_FAULT_SW_ID_{TEST_ENV_FLAG}',

            'Vehicle_MDC_SW_ID': f'Vehicle_MDC_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_MDC_Jump_SW_ID': f'Vehicle_MDC_Jump_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_MDC_ROLLBACK_SW_ID': f'Vehicle_MDC_ROLLBACK_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_MDC_All_SW_ID': f'Vehicle_MDC_All_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_MDC_DIFF_SW_ID': f'Vehicle_MDC_DIFF_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_MDC_DIFF_All_SW_ID': f'Vehicle_MDC_DIFF_All_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_MDC_All_DIFF_ERROR_SW_ID': f'Vehicle_MDC_All_DIFF_ERROR_SW_ID_{TEST_ENV_FLAG}',

            'Vehicle_HW_SW_ID': f'Vehicle_HW_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_All_SW_ID': f'Vehicle_All_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_TBOX_VDC_SW_ID': f'Vehicle_TBOX_VDC_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_ALL_Download_SW_ID': f'Vehicle_ALL_Download_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_ALL_Downgraded_SW_ID': f'Vehicle_ALL_Downgraded_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_ALL_downLOW_SW_ID': f'Vehicle_ALL_downLOW_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_LV_SW_ID': f'Vehicle_LV_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_HV_SW_ID': f'Vehicle_HV_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_HW_NO_CDC_SW_ID': f'Vehicle_HW_NO_CDC_SW_ID_{TEST_ENV_FLAG}',
            'Vericle_BMS_SW_WrongVersion_ID': f'Vehicle_BMS_SW_WrongVersion_ID_{TEST_ENV_FLAG}',
        }
    },
    'F2': {
        'l30034136': {
            'Vehicle_VDC_SW_ID': f'Vehicle_VDC_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_VDC_ROLLBACK_SW_ID': f'Vehicle_VDC_ROLLBACK_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_VDC_DOMAIN_SW_ID': f'Vehicle_VDC_DOMAIN_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_VDC_DOMAIN_ROLLBACK_SW_ID': f'Vehicle_VDC_DOMAIN_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_VIU1_SW_ID': f'Vehicle_VIU1_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_VIU2_SW_ID': f'Vehicle_VIU2_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_VIU3_SW_ID': f'Vehicle_VIU3_SW_ID_{TEST_ENV_FLAG}',

            'Vehicle_TBOX_SW_ID': f'Vehicle_TBOX_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_TBOX_ROLLBACK_SW_ID': f'Vehicle_TBOX_ROLLBACK_SW_ID_{TEST_ENV_FLAG}',

            'Vehicle_CDC_SW_ID': f'Vehicle_CDC_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_CDC_ROLLBACK_SW_ID': f'Vehicle_CDC_ROLLBACK_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_CDC_All_SW_ID': f'Vehicle_CDC_All_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_CDC_Inside_DIFF_SW_ID': f'Vehicle_CDC_Inside_DIFF_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_CDC_All_DIFF_SW_ID': f'Vehicle_CDC_All_DIFF_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_CDC_All_DIFF_ERROR_SW_ID': f'Vehicle_CDC_All_DIFF_ERROR_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_CDC_BJ_SW_ID': f'Vehicle_CDC_BJ_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_CDC_IVI_FAULT_SW_ID': f'Vehicle_CDC_IVI_FAULT_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_CDC_Inside_FAULT_SW_ID': f'Vehicle_CDC_Inside_FAULT_SW_ID_{TEST_ENV_FLAG}',

            'Vehicle_MDC_SW_ID': f'Vehicle_MDC_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_MDC_Jump_SW_ID': f'Vehicle_MDC_Jump_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_MDC_ROLLBACK_SW_ID': f'Vehicle_MDC_ROLLBACK_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_MDC_All_SW_ID': f'Vehicle_MDC_All_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_MDC_DIFF_SW_ID': f'Vehicle_MDC_DIFF_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_MDC_DIFF_All_SW_ID': f'Vehicle_MDC_DIFF_All_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_MDC_All_DIFF_ERROR_SW_ID': f'Vehicle_MDC_All_DIFF_ERROR_SW_ID_{TEST_ENV_FLAG}',

            'Vehicle_HW_SW_ID': f'Vehicle_HW_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_All_SW_ID': f'Vehicle_All_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_All_ROLLBACK_SW_ID': f'Vehicle_All_ROLLBACK_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_TBOX_VDC_SW_ID': f'Vehicle_TBOX_VDC_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_ALL_Download_SW_ID': f'Vehicle_ALL_Download_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_ALL_Downgraded_SW_ID': f'Vehicle_ALL_Downgraded_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_LV_SW_ID': f'Vehicle_LV_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_HV_SW_ID': f'Vehicle_HV_SW_ID_{TEST_ENV_FLAG}',
            'Vehicle_HW_NO_CDC_SW_ID': f'Vehicle_HW_NO_CDC_SW_ID_{TEST_ENV_FLAG}',
        },
    },
    'X1': {}
}

versions = CUSTOM_VERSION.get(PROJECT).get(TEST_ENV_FLAG)
# VDC
Vehicle_VDC_SW_ID = versions.get('Vehicle_VDC_SW_ID')  # VDC软件包
Vehicle_VDC_ROLLBACK_SW_ID = versions.get('Vehicle_VDC_ROLLBACK_SW_ID')  # VDC升级失败触发回退
Vehicle_VDC_DOMAIN_SW_ID = versions.get('Vehicle_VDC_DOMAIN_SW_ID')  # VDC域软件包
Vehicle_VDC_DOMAIN_ROLLBACK_SW_ID = versions.get('Vehicle_VDC_DOMAIN_ROLLBACK_SW_ID')  # VDC域整体升级，最后一个部件升级失败触发回退
Vehicle_VIU1_SW_ID = versions.get('Vehicle_VIU1_SW_ID')  # VIU1软件包
Vehicle_VIU2_SW_ID = versions.get('Vehicle_VIU2_SW_ID')  # VIU2软件包
Vehicle_VIU3_SW_ID = versions.get('Vehicle_VIU3_SW_ID')  # VIU3软件包

# TBOX
Vehicle_TBOX_SW_ID = versions.get('Vehicle_TBOX_SW_ID')  # TBOX软件包
Vehicle_TBOX_ROLLBACK_SW_ID = versions.get('Vehicle_TBOX_ROLLBACK_SW_ID')  # TBOX版本号错误触发回滚

# CDC
Vehicle_CDC_SW_ID = versions.get('Vehicle_CDC_SW_ID')  # CDC全量包升级能力，不含下挂节点
Vehicle_CDC_All_SW_ID = versions.get('Vehicle_CDC_All_SW_ID')  # CDC全量包升级能力，含下挂节点
Vehicle_CDC_ROLLBACK_SW_ID = versions.get('Vehicle_CDC_ROLLBACK_SW_ID')  # CDC版本号错误触发回滚
Vehicle_CDC_Inside_DIFF_SW_ID = versions.get('Vehicle_CDC_Inside_DIFF_SW_ID')  # CDC差分包升级能力，不含下挂节点
Vehicle_CDC_All_DIFF_SW_ID = versions.get('Vehicle_CDC_All_DIFF_SW_ID')  # CDC差分包升级能力，含下挂节点
Vehicle_CDC_All_DIFF_ERROR_SW_ID = versions.get('Vehicle_CDC_All_DIFF_ERROR_SW_ID')  # CDC原版本号错误差分包
Vehicle_CDC_BJ_SW_ID = versions.get('Vehicle_CDC_BJ_SW_ID')  # CDC下挂节点
Vehicle_CDC_IVI_FAULT_SW_ID = versions.get('Vehicle_CDC_IVI_FAULT_SW_ID')  # CDC域IVI升级失败触发回滚下挂节点
Vehicle_CDC_Inside_FAULT_SW_ID = versions.get('Vehicle_CDC_Inside_FAULT_SW_ID')  # CDC域AMP升级失败触发回滚下挂节点
Vehicle_EPA_SW_ID = versions.get('Vehicle_EPA_SW_ID')  # EPA软件包

# MDC
Vehicle_MDC_SW_ID = versions.get('Vehicle_MDC_SW_ID')  # MDC全量软件包不含下挂节点
Vehicle_MDC_Jump_SW_ID = versions.get('Vehicle_MDC_Jump_SW_ID')  # MDC跳转版本
Vehicle_MDC_ROLLBACK_SW_ID = versions.get('Vehicle_MDC_ROLLBACK_SW_ID')  # MDC错误包
Vehicle_MDC_All_SW_ID = versions.get('Vehicle_MDC_All_SW_ID')  # MDC全量软件包含下挂节点
Vehicle_MDC_DIFF_SW_ID = versions.get('Vehicle_MDC_DIFF_SW_ID')  # MDC差分包不含下挂节点
Vehicle_MDC_DIFF_All_SW_ID = versions.get('Vehicle_MDC_DIFF_All_SW_ID')  # MDC差分包含下挂节点
Vehicle_MDC_All_DIFF_ERROR_SW_ID = versions.get('Vehicle_MDC_All_DIFF_ERROR_SW_ID')  # MDC异常差分包升级能力，含下挂节点

# 整车
Vehicle_All_SW_ID = versions.get('Vehicle_All_SW_ID')  # 整车软件版本包含非华为件
Vehicle_All_Jump_SW_ID = versions.get('Vehicle_All_Jump_SW_ID')  # 整车软件版本为降版本
Vehicle_All_DIFF_SW_ID = versions.get('Vehicle_All_DIFF_SW_ID')  # 整车软件版本包含非华为件，CDC和MDC为差分包
Vehicle_HW_SW_ID = versions.get('Vehicle_HW_SW_ID')  # 整车软件版本不包含非华为件
Vehicle_HW_NO_CDC_SW_ID = versions.get('Vehicle_HW_NO_CDC_SW_ID')  # 整车软件版本不包含非华为件,无CDC
Vehicle_HW_MDC_Jump_SW_ID = versions.get('Vehicle_HW_MDC_Jump_SW_ID')  # 整车软件版本不包含非华为件,MDC为跳转版本
Vehicle_All_ROLLBACK_SW_ID = versions.get('Vehicle_All_ROLLBACK_SW_ID')  # 整车错误包
Vehicle_TBOX_VDC_SW_ID = versions.get('Vehicle_TBOX_VDC_SW_ID')  # TBOX + VDC域升級
Vehicle_ALL_Download_SW_ID = versions.get('Vehicle_ALL_Download_SW_ID')  # 整车全量用于下载测试的自定义版本
Vehicle_ALL_Downgraded_SW_ID = versions.get('Vehicle_ALL_Downgraded_SW_ID')  # 整车降版本
Vehicle_LV_SW_ID = versions.get('Vehicle_LV_SW_ID')  # 整车低压部件
Vehicle_HV_SW_ID = versions.get('Vehicle_HV_SW_ID')  # 整车高压部件
Vehicle_ALL_downLOW_SW_ID = versions.get('Vehicle_ALL_downLOW_SW_ID')  # 下挂件降版本
# 下挂件
Vericle_BMS_SW_WrongVersion_ID = versions.get('Vericle_BMS_SW_WrongVersion_ID')  # BMS错误版本包

# 自定义版本软件包组合
CUSTOM_VERSION_ADD = {
    'X2': {
        's00566695': {
            'Vehicle_VDC_SW_ID': [pv.get('VDC_SW')],
            'Vehicle_VDC_ROLLBACK_SW_ID': [pv.get('VDC_WRONG_SW')],
            'Vehicle_VDC_DOMAIN_SW_ID': [pv.get('VDC_SW'), pv.get('VIU1_SW'), pv.get('VIU2_SW'), pv.get('VIU3_SW')],
            'Vehicle_VDC_DOMAIN_ROLLBACK_SW_ID': [pv.get('VDC_SW'), pv.get('VIU1_WRONG_SW'), pv.get('VIU2_WRONG_SW'),
                                                  pv.get('VIU3_WRONG_SW')],
            'Vehicle_VIU1_SW_ID': [pv.get('VIU1_SW')],
            'Vehicle_VIU2_SW_ID': [pv.get('VIU2_SW')],
            'Vehicle_VIU3_SW_ID': [pv.get('VIU3_SW')],

            'Vehicle_TBOX_SW_ID': [pv.get('TBOX_SW')],
            'Vehicle_TBOX_ROLLBACK_SW_ID': [pv.get('TBOX_WRONG_SW')],

            'Vehicle_CDC_SW_ID': [pv.get('CDC_SW')],
            'Vehicle_CDC_ROLLBACK_SW_ID': [pv.get('CDC_WRONG_SW')],
            'Vehicle_CDC_All_SW_ID': [pv.get('CDC_SW'), pv.get('EPA_SW')],
            'Vehicle_CDC_Inside_DIFF_SW_ID': [pv.get('CDC_DIFF_SW')],
            'Vehicle_CDC_All_DIFF_SW_ID': [pv.get('CDC_DIFF_SW')],

            'Vehicle_MDC_SW_ID': [pv.get('MDC_SW')],
            'Vehicle_MDC_ROLLBACK_SW_ID': [pv.get('MDC_WRONG_SW')],
            'Vehicle_MDC_All_SW_ID': [pv.get('MDC_SW')],
            'Vehicle_MDC_DIFF_SW_ID': [pv.get('MDC_DIFF_SW')],
            'Vehicle_MDC_DIFF_All_SW_ID': [pv.get('MDC_DIFF_SW')],
            'Vehicle_MDC_Jump_SW_ID': [pv.get('MDC_Jump_SW')],

            'Vehicle_All_SW_ID': [pv.get('VDC_SW'), pv.get('TBOX_SW'), pv.get('CDC_SW'), pv.get('MDC_SW'),
                                  pv.get('VIU1_SW'), pv.get('VIU2_SW'), pv.get('VIU3_SW'), pv.get('EPA_SW')],
            'Vehicle_HW_SW_ID': [pv.get('VDC_SW'), pv.get('TBOX_SW'), pv.get('CDC_SW'), pv.get('MDC_SW'),
                                 pv.get('VIU1_SW'), pv.get('VIU2_SW'), pv.get('VIU3_SW')],
            'Vehicle_TBOX_VDC_SW_ID': [pv.get('VDC_SW'), pv.get('TBOX_SW'), pv.get('VIU1_SW'), pv.get('VIU2_SW'),
                                       pv.get('VIU3_SW')],
            'Vehicle_ALL_Download_SW_ID': [pv.get('VDC_SW'), pv.get('TBOX_SW'), pv.get('CDC_SW'), pv.get('MDC_SW'),
                                           pv.get('VIU1_SW'), pv.get('VIU2_SW'), pv.get('VIU3_SW')],
            'Vehicle_ALL_Downgraded_SW_ID': [pv.get('VDC_SW_LOW'), pv.get('TBOX_SW_LOW'), pv.get('CDC_SW_LOW'),
                                             pv.get('MDC_SW_LOW'), pv.get('VIU1_SW_LOW'), pv.get('VIU2_SW_LOW'),
                                             pv.get('VIU3_SW_LOW')],
            'Vehicle_HW_NO_CDC_SW_ID': [pv.get('VDC_SW'), pv.get('TBOX_SW'), pv.get('MDC_SW'), pv.get('VIU1_SW'),
                                        pv.get('VIU2_SW'), pv.get('VIU3_SW')],
            'Vehicle_HV_SW_ID': [pv.get('VDC_SW'), pv.get('TBOX_SW'), pv.get('CDC_SW'), pv.get('MDC_SW'),
                                 pv.get('VIU1_SW'), pv.get('VIU2_SW'), pv.get('VIU3_SW'), pv.get('EPA_SW')],
            'Vehicle_LV_SW_ID': [pv.get('EPA_SW')],
        },
        'wwx1275683': {
            'Vehicle_VDC_SW_ID': [pv.get('VDC_SW')],
            'Vehicle_VDC_ROLLBACK_SW_ID': [pv.get('VDC_WRONG_SW')],
            'Vehicle_VDC_DOMAIN_SW_ID': [pv.get('VDC_SW'), pv.get('VIU1_SW'), pv.get('VIU2_SW'), pv.get('VIU3_SW')],
            'Vehicle_VDC_DOMAIN_ROLLBACK_SW_ID': [pv.get('VDC_SW'), pv.get('VIU1_WRONG_SW'), pv.get('VIU2_WRONG_SW'),
                                                  pv.get('VIU3_WRONG_SW')],
            'Vehicle_VIU1_SW_ID': [pv.get('VIU1_SW')],
            'Vehicle_VIU2_SW_ID': [pv.get('VIU2_SW')],
            'Vehicle_VIU3_SW_ID': [pv.get('VIU3_SW')],

            'Vehicle_TBOX_SW_ID': [pv.get('TBOX_SW')],
            'Vehicle_TBOX_ROLLBACK_SW_ID': [pv.get('TBOX_WRONG_SW')],

            'Vehicle_CDC_SW_ID': [pv.get('CDC_SW')],
            'Vehicle_CDC_ROLLBACK_SW_ID': [pv.get('CDC_WRONG_SW')],
            'Vehicle_CDC_All_SW_ID': [pv.get('CDC_SW'), pv.get('EPA_SW'), pv.get('IC_SW'), pv.get('CDS_SW')],
            'Vehicle_CDC_Inside_DIFF_SW_ID': [pv.get('CDC_DIFF_SW')],
            'Vehicle_CDC_All_DIFF_SW_ID': [pv.get('CDC_DIFF_SW')],

            'Vehicle_MDC_SW_ID': [pv.get('MDC_SW')],
            'Vehicle_MDC_ROLLBACK_SW_ID': [pv.get('MDC_WRONG_SW')],
            'Vehicle_MDC_All_SW_ID': [pv.get('MDC_SW')],
            'Vehicle_MDC_DIFF_SW_ID': [pv.get('MDC_DIFF_SW')],
            'Vehicle_MDC_DIFF_All_SW_ID': [pv.get('MDC_DIFF_SW')],
            'Vehicle_MDC_Jump_SW_ID': [pv.get('MDC_Jump_SW')],

            'Vehicle_All_SW_ID': [pv.get('VDC_SW'), pv.get('TBOX_SW'), pv.get('CDC_SW'), pv.get('MDC_SW'),
                                  pv.get('VIU1_SW'), pv.get('VIU2_SW'), pv.get('VIU3_SW'),
                                  pv.get('BMS_SW'), pv.get('CDU_SW'), pv.get('CS_SW'), pv.get('CCU_SW'),
                                  pv.get('ECAS_SW'), pv.get('EPA_SW'), pv.get('EPB1_SW'), pv.get('EPB2_SW'),
                                  pv.get('EPS_SW'), pv.get('FLML_SW'), pv.get('FLMR_SW'), pv.get('IC_SW'),
                                  pv.get('IKM_SW'), pv.get('LBMS_SW'), pv.get('MCUF_SW'), pv.get('MCUR_SW'),
                                  pv.get('PTC_SW'), pv.get('TDU_SW'), pv.get('TPMS_SW'), pv.get('VPA_SW'),
                                  pv.get('WCM_SW')],

            'Vehicle_HW_SW_ID': [pv.get('VDC_SW'), pv.get('TBOX_SW'), pv.get('CDC_SW'), pv.get('MDC_SW'),
                                 pv.get('VIU1_SW'), pv.get('VIU2_SW'), pv.get('VIU3_SW'), pv.get('CDU_SW'),
                                 pv.get('MCUF_SW'), pv.get('MCUR_SW'), pv.get('TDU_SW'), pv.get('CCU_SW'),
                                 pv.get('PTC_SW'), pv.get('IC_SW'), pv.get('EPA_SW')],
            'Vehicle_TBOX_VDC_SW_ID': [pv.get('VDC_SW'), pv.get('TBOX_SW'), pv.get('VIU1_SW'), pv.get('VIU2_SW'),
                                       pv.get('VIU3_SW')],
            'Vehicle_ALL_Download_SW_ID': [pv.get('VDC_SW'), pv.get('TBOX_SW'), pv.get('CDC_SW'), pv.get('MDC_SW'),
                                           pv.get('VIU1_SW'), pv.get('VIU2_SW'), pv.get('VIU3_SW'),
                                           pv.get('BMS_SW'), pv.get('CDU_SW'), pv.get('CS_SW'), pv.get('CCU_SW'),
                                           pv.get('ECAS_SW'), pv.get('EPA_SW'), pv.get('EPB1_SW'), pv.get('EPB2_SW'),
                                           pv.get('EPS_SW'), pv.get('FLML_SW'), pv.get('FLMR_SW'), pv.get('IC_SW'),
                                           pv.get('IKM_SW'), pv.get('LBMS_SW'), pv.get('MCUF_SW'), pv.get('MCUR_SW'),
                                           pv.get('PTC_SW'), pv.get('TDU_SW'), pv.get('TPMS_SW'), pv.get('VPA_SW'),
                                           pv.get('WCM_SW')],
            'Vehicle_ALL_Downgraded_SW_ID': [pv.get('VDC_SW_LOW'), pv.get('VIU1_SW_LOW'), pv.get('VIU2_SW_LOW'),
                                             pv.get('VIU3_SW_LOW'),
                                             pv.get('BMS_SW_LOW'), pv.get('CDU_SW_LOW'), pv.get('MDC_SW_LOW'),
                                             pv.get('CCU_SW_LOW'),
                                             pv.get('CS_SW_LOW'), pv.get('ECAS_SW_LOW'), pv.get('EPA_SW_LOW'),
                                             pv.get('EPB1_SW_LOW'),
                                             pv.get('EPB2_SW_LOW'), pv.get('EPS_SW_LOW'), pv.get('FLML_SW_LOW'),
                                             pv.get('FLMR_SW_LOW'),
                                             pv.get('IC_SW_LOW'), pv.get('IKM_SW_LOW'), pv.get('LBMS_SW_LOW'),
                                             pv.get('MCUF_SW_LOW'),
                                             pv.get('MCUR_SW_LOW'), pv.get('PTC_SW_LOW'), pv.get('TDU_SW_LOW'),
                                             pv.get('TPMS_SW_LOW'),
                                             pv.get('VPA_SW_LOW'), pv.get('WCM_SW_LOW'),
                                             ],
            'Vehicle_ALL_downLOW_SW_ID': [pv.get('BMS_SW_LOW'), pv.get('CDU_SW_LOW'),
                                             pv.get('CCU_SW_LOW'),
                                             pv.get('CS_SW_LOW'), pv.get('ECAS_SW_LOW'), pv.get('EPA_SW_LOW'),
                                             pv.get('EPB1_SW_LOW'),
                                             pv.get('EPB2_SW_LOW'), pv.get('EPS_SW_LOW'), pv.get('FLML_SW_LOW'),
                                             pv.get('FLMR_SW_LOW'),
                                             pv.get('IKM_SW_LOW'), pv.get('LBMS_SW_LOW'),
                                             pv.get('MCUF_SW_LOW'),
                                             pv.get('MCUR_SW_LOW'), pv.get('PTC_SW_LOW'), pv.get('TDU_SW_LOW'),
                                             pv.get('TPMS_SW_LOW'),
                                             pv.get('VPA_SW_LOW'), pv.get('WCM_SW_LOW'),
                                             ],


            'Vericle_BMS_SW_WrongVersion_ID': [pv.get('BMS_SW_WRONG_VERSION')]
        },
    },
    'F2': {
        'l30034136': {
            'Vehicle_VDC_SW_ID': [pv.get('VDC_SW')],
            'Vehicle_VDC_ROLLBACK_SW_ID': [pv.get('VDC_WRONG_SW')],
            'Vehicle_VDC_DOMAIN_SW_ID': [pv.get('VDC_SW'), pv.get('VIU1_SW'), pv.get('VIU2_SW'), pv.get('VIU3_SW')],
            'Vehicle_VDC_DOMAIN_ROLLBACK_SW_ID': [pv.get('VDC_SW'), pv.get('VIU1_WRONG_SW'), pv.get('VIU2_WRONG_SW'),
                                                  pv.get('VIU3_WRONG_SW')],
            'Vehicle_VIU1_SW_ID': [pv.get('VIU1_SW')],
            'Vehicle_VIU2_SW_ID': [pv.get('VIU2_SW')],
            'Vehicle_VIU3_SW_ID': [pv.get('VIU3_SW')],

            'Vehicle_TBOX_SW_ID': [pv.get('TBOX_SW')],
            'Vehicle_TBOX_ROLLBACK_SW_ID': [pv.get('TBOX_WRONG_SW')],

            'Vehicle_CDC_SW_ID': [pv.get('CDC_SW')],
            'Vehicle_CDC_ROLLBACK_SW_ID': [pv.get('CDC_WRONG_SW')],
            'Vehicle_CDC_All_SW_ID': [pv.get('CDC_SW'), pv.get('EPA_SW')],
            'Vehicle_CDC_Inside_DIFF_SW_ID': [pv.get('CDC_DIFF_SW')],
            'Vehicle_CDC_All_DIFF_SW_ID': [pv.get('CDC_DIFF_SW')],

            'Vehicle_MDC_SW_ID': [pv.get('MDC_SW')],
            'Vehicle_MDC_ROLLBACK_SW_ID': [pv.get('MDC_WRONG_SW')],
            'Vehicle_MDC_All_SW_ID': [pv.get('MDC_SW')],
            'Vehicle_MDC_DIFF_SW_ID': [pv.get('MDC_DIFF_SW')],
            'Vehicle_MDC_DIFF_All_SW_ID': [pv.get('MDC_DIFF_SW')],

            'Vehicle_All_SW_ID': [pv.get('VDC_SW'), pv.get('TBOX_SW'), pv.get('CDC_SW'), pv.get('MDC_SW'),
                                  pv.get('VIU1_SW'), pv.get('VIU2_SW'), pv.get('VIU3_SW'), pv.get('EPA_SW')],
            'Vehicle_HW_SW_ID': [pv.get('VDC_SW'), pv.get('TBOX_SW'), pv.get('CDC_SW'), pv.get('MDC_SW'),
                                 pv.get('VIU1_SW'), pv.get('VIU2_SW'), pv.get('VIU3_SW')],
            'Vehicle_TBOX_VDC_SW_ID': [pv.get('VDC_SW'), pv.get('TBOX_SW'), pv.get('VIU1_SW'), pv.get('VIU2_SW'),
                                       pv.get('VIU3_SW')],
            'Vehicle_ALL_Download_SW_ID': [pv.get('VDC_SW'), pv.get('TBOX_SW'), pv.get('CDC_SW'), pv.get('MDC_SW'),
                                           pv.get('VIU1_SW'), pv.get('VIU2_SW'), pv.get('VIU3_SW')],
            'Vehicle_ALL_Downgraded_SW_ID': [pv.get('VDC_SW_LOW'), pv.get('TBOX_SW_LOW'), pv.get('CDC_SW_LOW'),
                                             pv.get('MDC_SW_LOW'), pv.get('VIU1_SW_LOW'), pv.get('VIU2_SW_LOW'),
                                             pv.get('VIU3_SW_LOW')],
        },
    },
}

versions_add = CUSTOM_VERSION_ADD.get(PROJECT).get(TEST_ENV_FLAG)
"""===================================================RELAY_CTRL参数================================================="""
# 继电器参数配置
if CAR_ENV_FLAG:
    # 实车用到的继电器控制端口
    relay_port = {
        'X2': {
            's00566695': {
                'RELAY_COM': 'COM4', 'TMS_KL30_Port': 16, 'VCU_KL30_Port': 7, 'VCU_KL15_Port': 8, 'GW_KL15_Port': 10,
                'GW_KL30_Port': 9, 'GW_OBD_ACTIVE': 11, 'TBOX_KL15_Port': 13, 'TBOX_KL30_Port': 12, 'DOOR_PORT': 0,
                'UNLOCK_PORT': 0, 'LOCK_PORT': 0
            },
            'wwx1275683': {
                'RELAY_COM': 'COM9', 'TMS_KL30_Port': 16, 'VCU_KL30_Port': 7, 'VCU_KL15_Port': 8, 'GW_KL15_Port': 10,
                'GW_KL30_Port': 9, 'GW_OBD_ACTIVE': 11, 'TBOX_KL15_Port': 13, 'TBOX_KL30_Port': 12, 'DOOR_PORT': 16,
                'UNLOCK_PORT': 0, 'LOCK_PORT': 0
            },
        },
        'F2': {
            'l30034136': {
                'RELAY_COM': 'COM4', 'TMS_KL30_Port': 16, 'VCU_KL30_Port': 7, 'VCU_KL15_Port': 8, 'GW_KL15_Port': 10,
                'GW_KL30_Port': 9, 'GW_OBD_ACTIVE': 11, 'TBOX_KL15_Port': 13, 'TBOX_KL30_Port': 12, 'DOOR_PORT': 0,
                'UNLOCK_PORT': 0, 'LOCK_PORT': 0
            },
        },
        'X1': {'m00613464': {}}
    }
else:
    # 台架
    relay_port = {
        'X2': {
            's00566695': {
                'RELAY_COM': 'COM4', 'TBOX_KL30_Port': 6, 'TBOX_KL15_Port': 5, 'CDC_KL30_Port': 2, 'CDC_KL15_Port': 1,
                'VDC_KL30_Port': 13, 'VDC_KL15_Port': 12, 'VIU1_KL30_Port': 14, 'VIU2_KL30_Port': 15,
                'VIU1_ETH_Port': 0,
                'VIU2_KL15_Port': 16, 'VIU3_KL30_Port': 11, 'MDC_GW_ETH': 17, 'CDC_GW_ETH': 18, 'TBOX_GW_ETH': 22,
            },
        },
        'F2': {
            'l30034136': {
                'RELAY_COM': 'COM30', 'TBOX_KL30_Port': 8, 'TBOX_KL15_Port': 11, 'CDC_KL30_Port': 27,
                'CDC_KL15_Port': 26,
                'VDC_KL30_Port': 13, 'VDC_KL15_Port': 12, 'VIU1_KL30_Port': 16, 'VIU2_KL30_Port': 15,
                'VIU1_ETH_Port': 0,
                'VIU2_KL15_Port': 10, 'VIU3_KL30_Port': 14, 'VIU3_KL15_Port': 9, 'LFDOORLOCK_Port': 4, 'LFDOOR_Port': 3,
                'VDC_DrvrSeatBltSt_Port': 5, 'BRAKEPEDAL_Port': 1, 'CDC_GW_ETH': 17, 'MDC_GW_ETH': 18, 'TBOX_GW_ETH': 19
            },  # 'CDC_KL30_Port': 7, 'CDC_KL15_Port': 6,
        },
        'X1': {'m00613464': {}}
    }

# 台架继电器
relay_ports = relay_port.get(PROJECT).get(TEST_ENV_FLAG)
RELAY_COM = relay_ports.get('RELAY_COM')
PCU_KL30_Port = relay_ports.get('PCU_KL30_Port')
PCU_KL15_Port = relay_ports.get('PCU_KL15_Port')
PDU_KL30_Port = relay_ports.get('PDU_KL30_Port')
PDU_KL15_Port = relay_ports.get('PDU_KL15_Port')
PEPS_KL30_Port = relay_ports.get('PEPS_KL30_Port')
VDC_KL15_Port = relay_ports.get('VDC_KL15_Port')
VDC_KL30_Port = relay_ports.get('VDC_KL30_Port')
VCU_KL15_Port = relay_ports.get('VCU_KL15_Port')
VCU_KL30_Port = relay_ports.get('VCU_KL30_Port')
GW_OBD_ACTIVE = relay_ports.get('GW_OBD_ACTIVE')
GW_KL15_Port = relay_ports.get('GW_KL15_Port')
GW_KL30_Port = relay_ports.get('GW_KL30_Port')
TMS_KL30_Port = relay_ports.get('TMS_KL30_Port')
TMS_KL15_Port = relay_ports.get('TMS_KL15_Port')
BMS_KL30_Port = relay_ports.get('BMS_KL30_Port')
BMS_KL15_Port = relay_ports.get('BMS_KL15_Port')
TBOX_KL15_Port = relay_ports.get('TBOX_KL15_Port')
TBOX_KL30_Port = relay_ports.get('TBOX_KL30_Port')
CDC_KL15_Port = relay_ports.get('CDC_KL15_Port')
CDC_KL30_Port = relay_ports.get('CDC_KL30_Port')
MDC_KL15_Port = relay_ports.get('MDC_KL15_Port')
MCUR_KL15_Port = relay_ports.get('MCUR_KL15_Port')
MCUR_KL30_Port = relay_ports.get('MCUR_KL30_Port')
VIU1_KL30_Port = relay_ports.get('VIU1_KL30_Port')
VIU2_KL30_Port = relay_ports.get('VIU2_KL30_Port')
VIU2_KL15_Port = relay_ports.get('VIU2_KL15_Port')
VIU3_KL30_Port = relay_ports.get('VIU3_KL30_Port')
VIU3_KL15_Port = relay_ports.get('VIU3_KL15_Port')
TBOX_GW_ETH1 = relay_ports.get('TBOX_GW_ETH1')
TBOX_GW_ETH2 = relay_ports.get('TBOX_GW_ETH2')
CDC_GW_ETH1 = relay_ports.get('CDC_GW_ETH1')
CDC_GW_ETH2 = relay_ports.get('CDC_GW_ETH2')
MDC_GW_ETH1 = relay_ports.get('MDC_GW_ETH1')
MDC_GW_ETH2 = relay_ports.get('MDC_GW_ETH2')
VCU_GW_ETH1 = relay_ports.get('VCU_GW_ETH1')
VCU_GW_ETH2 = relay_ports.get('VCU_GW_ETH2')
CDC_ETH = relay_ports.get('CDC_ETH')
VIUR_KL30_Port = relay_ports.get('VIUR_KL30_Port')
VIUR_KL15_Port = relay_ports.get('VIUR_KL15_Port')
VIUF_KL30_Port = relay_ports.get('VIUF_KL30_Port')
VIUF_KL15_Port = relay_ports.get('VIUF_KL15_Port')
VIUML_KL30_Port = relay_ports.get('VIUML_KL30_Port')
VIUML_KL15_Port = relay_ports.get('VIUML_KL15_Port')
VIUMR_KL30_Port = relay_ports.get('VIUMR_KL30_Port')
VIUMR_KL15_Port = relay_ports.get('VIUMR_KL15_Port')
MCUF_KL30_Port = relay_ports.get('MCUF_KL30_Port')
MCUF_KL15_Port = relay_ports.get('MCUF_KL15_Port')
ECC_KL15_Port = relay_ports.get('ECC_KL15_Port')
ECC_KL30_Port = relay_ports.get('ECC_KL30_Port')
PDCU_KL15_Port = relay_ports.get('PDCU_KL15_Port')
PDCU_KL30_Port = relay_ports.get('PDCU_KL30_Port')
TBOX_GW_ETH = relay_ports.get('TBOX_GW_ETH')
CDC_GW_ETH = relay_ports.get('CDC_GW_ETH')
MDC_GW_ETH = relay_ports.get('MDC_GW_ETH')
VCU_GW_ETH = relay_ports.get('VCU_GW_ETH')
CDC_GW_CANFD = relay_ports.get('CDC_GW_CANFD')
TBOX_GW_CANFD = relay_ports.get('TBOX_GW_CANFD')
LFDOOR_CANFD = relay_ports.get('LFDOOR_Port')
LFDOORLOCK_CANFD = relay_ports.get('LFDOORLOCK_Port')
BRAKEPEDAL = relay_ports.get('BRAKEPEDAL_Port')

# 实车继电器
DOOR_PORT = relay_ports.get('DOOR_PORT')
UNLOCK_PORT = relay_ports.get('UNLOCK_PORT')
LOCK_PORT = relay_ports.get('LOCK_PORT')

"""===================================================ECU_CTRL参数================================================="""
# mdc参数
MDC_DATA = {
    'X2': {
        'MDC_VERSION': "/etc/mdc_version",
        'Pro610_path': "/home/mdc/ota",
        'pkg_path': "/opt/usr/upgrade",
        'core_dump_path': "/opt/log/npu/coredump/",
        'core_dump_610_path': "/home/mdc/var/log/npu/coredump/",
        'swm_json_path': '/opt/ota/conf/swm/swm_data.json',
        'swm_cfg_mdcpro610': '/etc/ads/service/mdc_conf/swm_cfg_mdcpro610.json',
        'hostwrong_path': r'E:\01_sunjun\01_tengwu\IASTest\Result\local_details\361456_Test_TC_HBTn61_OTA_BF_Download_'
                          r'WiFi_032\TC_HBTn61_OTA_BF_Download_WiFi_032183317\cdc_log\LogService\host_wrong',
        'version_dst_path': '/home/mdc/ota/package/',
        'adipwrong_path': r'E:\01_sunjun\01_tengwu\IASTest\Result\local_details\361456_Test_TC_HBTn61_OTA_BF_Download'
                          r'_WiFi_032\TC_HBTn61_OTA_BF_Download_WiFi_032183317\cdc_log\LogService\adip_wrong',
        'radarwrong_path': r'E:\01_sunjun\01_tengwu\IASTest\Result\local_details\361456_Test_TC_HBTn61_OTA_BF_Download'
                           r'_WiFi_032\TC_HBTn61_OTA_BF_Download_WiFi_032183317\cdc_log\LogService\radar_wrong',
    },
    'F2': {
        'MDC_VERSION': "/etc/mdc_version",
        'Pro610_path': "/home/mdc/ota",
        'pkg_path': "/opt/usr/upgrade",
        'core_dump_path': "/opt/log/npu/coredump/",
        'core_dump_610_path': "/home/mdc/var/log/npu/coredump/",
        'swm_json_path': '/opt/ota/conf/swm/swm_data.json',
        'swm_cfg_mdcpro610': '/etc/ads/service/mdc_conf/swm_cfg_mdcpro610.json',
        'hostwrong_path': r'E:\01_sunjun\01_tengwu\IASTest\Result\local_details\361456_Test_TC_HBTn61_OTA_BF_Download_'
                          r'WiFi_032\TC_HBTn61_OTA_BF_Download_WiFi_032183317\cdc_log\LogService\host_wrong',
        'version_dst_path': '/home/mdc/ota/package/',
        'adipwrong_path': r'E:\01_sunjun\01_tengwu\IASTest\Result\local_details\361456_Test_TC_HBTn61_OTA_BF_Download'
                          r'_WiFi_032\TC_HBTn61_OTA_BF_Download_WiFi_032183317\cdc_log\LogService\adip_wrong',
        'radarwrong_path': r'E:\01_sunjun\01_tengwu\IASTest\Result\local_details\361456_Test_TC_HBTn61_OTA_BF_Download'
                           r'_WiFi_032\TC_HBTn61_OTA_BF_Download_WiFi_032183317\cdc_log\LogService\radar_wrong',
    },
}

# mdc参数
MDC_VERSION = MDC_DATA.get(PROJECT).get('MDC_VERSION')
Pro610_path = MDC_DATA.get(PROJECT).get('Pro610_path')
pkg_path = MDC_DATA.get(PROJECT).get('pkg_path')
core_dump_path = MDC_DATA.get(PROJECT).get('core_dump_path')
core_dump_610_path = MDC_DATA.get(PROJECT).get('core_dump_610_path')
swm_json_path = MDC_DATA.get(PROJECT).get('swm_json_path')
swm_cfg_mdcpro610 = MDC_DATA.get(PROJECT).get('swm_cfg_mdcpro610')
hostwrong_path = MDC_DATA.get(PROJECT).get('hostwrong_path')
version_dst_path = MDC_DATA.get(PROJECT).get('version_dst_path')
adipwrong_path = MDC_DATA.get(PROJECT).get('adipwrong_path')
radarwrong_path = MDC_DATA.get(PROJECT).get('radarwrong_path')

"""===================================================MAIN_UDS_DOWNLOAD参数=========================================="""
# 近端参数
UDS_DATA = {
    's00566695': {
        'gw_file_path': r"",
        'gw_file_name': "",
        'gw_file_path_E11_GW': r"",
        'gw_file_name_E11_GW': "",
        'TBOX_file_path': r"",
        'TBOX_file_name': "",
        'TMS_file_path': r"",
        'TMS_file_name': "",
        'VCU_file_path': r"",
        'VCU_file_name': "",
        'MDC_file_path': r"D:\AUTO_TEST\X2\Reprogram\MDC",
        'MDC_file_name': "MDC_702000176AA_SW02.03.27_240203_All.zip",
        'VDC_file_path': r"D:\AUTO_TEST\X2\Reprogram\VDC\VDC_809000086AA_SW00.05.04_240124_HW0.2.0",
        'VDC_file_name': "VDC_809000086AA_SW00.05.04_240124_HW0.2.0.zip",
        'VIU1_file_path': r"D:\AUTO_TEST\X2\Reprogram\VIU\VIU1",
        'VIU1_file_name': "pkg-cfg.xml",
        'VIU2_file_path': r"D:\AUTO_TEST\X2\Reprogram\VIU\VIU2",
        'VIU2_file_name': "pkg-cfg.xml",
        'VIU3_file_path': r"D:\AUTO_TEST\X2\Reprogram\VIU\VIU3",
        'VIU3_file_name': "pkg-cfg.xml",
        'CDC_file_path': r"",
        'CDC_file_name': "",
        'MCU_file_path': r"",
        'MCU_file_path_mcuf': r"",
        'MCU_file_name_mcuf': "",
        'MCU_file_name': "",
        'PDU_file_path': r"",
        'PDU_file_name': "",
        'MCU_file_path_B': r"",
        'MCU_file_path_mcuf_B': r"",
        'MCU_file_name_mcuf_B': "",
        'MCU_file_name_B': "",
    },
    'wwx1275683': {
        'gw_file_path': r"",
        'gw_file_name': "",
        'gw_file_path_E11_GW': r"",
        'gw_file_name_E11_GW': "",
        'TBOX_file_path': r"",
        'TBOX_file_name': "",
        'TMS_file_path': r"",
        'TMS_file_name': "",
        'VCU_file_path': r"",
        'VCU_file_name': "",
        'MDC_file_path': r"",
        'MDC_file_name': "",
        'VDC_file_path': r"D:\AUTO_TEST\N50\Reprogram\VDC",
        'VDC_file_name': "VDC_809000086AA_SW00.08.09_00.08.09_231101_HW0.2.0.zip",
        'VIU1_file_path': r"",
        'VIU1_file_name': "",
        'VIU2_file_path': r"",
        'VIU2_file_name': "",
        'VIU3_file_path': r"",
        'VIU3_file_name': "",
        'CDC_file_path': r"",
        'CDC_file_name': "",
        'MCU_file_path': r"",
        'MCU_file_path_mcuf': r"",
        'MCU_file_name_mcuf': "",
        'MCU_file_name': "",
        'PDU_file_path': r"",
        'PDU_file_name': "",
        'MCU_file_path_B': r"",
        'MCU_file_path_mcuf_B': r"",
        'MCU_file_name_mcuf_B': "",
        'MCU_file_name_B': "",
    },
    'l30034136': {
        'gw_file_path': r"D:\00_北汽项目\ECU软件包\SOP版本\VGW\CGWE00111266S003050A01N61AB-C01",
        'gw_file_name': "5-CRC_CGW_V002.xml",
        'gw_file_path_E11_GW': r"D:\00_北汽项目\ECU软件包\E11\GW-9210401-EP50-SWC.1.0",
        'gw_file_name_E11_GW': "Pkg-Cfg.xml",
        'TBOX_file_path': r"D:\00_北汽项目\ECU软件包\SOP版本\TBOX\T-Box DA2501-01 10.0.2.0(SP22C00)-debug-sop2-0125\2-"
                          r"TBXE00111276S003050A01N61AB-C01(debug)",
        'TBOX_file_name': "5-CRC_TBOX_V002.xml",
        'TMS_file_path': r"D:\00_北汽项目\ECU软件包\SOP版本\TMS\TMSV 1.0.015-D0010000\s19",
        'TMS_file_name': "5-CRC_TMS_S003050.xml",
        'VCU_file_path': r"D:\00_北汽项目\ECU软件包\SOP版本\PDCU\SOP_VCU_S005045",
        'VCU_file_name': "5-CRC_VCU_V001.xml",
        'MDC_file_path': r"D:\3_ECU_softfile\ADAS\ADAS",
        'MDC_file_name': "5-CRC_ADS_V001.xml",
        'CDC_file_path': r"D:\00_北汽项目\ECU软件包\SOP版本\CDC\SOP脱B版本\ICSV 1.0.025-D0010000-odex_0211",
        'CDC_file_name': "5-CRC_ICC_S003052.xml",
        'VDC_file_path': r"",
        'VDC_file_name': "",
        'VIU1_file_path': r"",
        'VIU1_file_name': "",
        'VIU2_file_path': r"",
        'VIU2_file_name': "",
        'VIU3_file_path': r"",
        'VIU3_file_name': "",
        'MCU_file_path': r"D:\00_北汽项目\ECU软件包\SOP版本\MCU\MPT_V100R001C00SPC217T_0106\MCUE00120670S003050N61AB-C01",
        'MCU_file_path_mcuf': r"D:\00_北汽项目\ECU软件包\SOP版本\MCU\MPT_V100R001C00SPC217T_0106\MCUE00120669S003050"
                              r"N61AB-C01",
        'MCU_file_name_mcuf': "5-CRC_MCU_V001.xml",
        'MCU_file_name': "5-CRC_MCU_V001.xml",
        'PDU_file_path': r"D:\02-近端升级\01_EP2-2近端升级测试\02_测试软件包\06_PDU\MPCV100R002C00SPC106T\MPCV100R002C00SP"
                         r"C106T",
        'PDU_file_name': "5-CRC_OBC_V001.xml",
        'MCU_file_path_B': r"D:\00_北汽项目\ECU软件包\SOP版本\MCU\MPT_V100R001C00SPC217T_0106\MCUE00120670S003050N61AB-C01",
        'MCU_file_path_mcuf_B': r"D:\00_北汽项目\ECU软件包\SOP版本\MCU\MPT_V100R001C00SPC217T_0106\MCUE00120669S003050N61"
                                r"AB-C01",
        'MCU_file_name_mcuf_B': "5-CRC_MCU_V001.xml",
        'MCU_file_name_B': "5-CRC_MCU_V001.xml",
    }
}

# 近端参数
gw_file_path = UDS_DATA.get(TEST_ENV_FLAG).get('gw_file_path')
gw_file_name = UDS_DATA.get(TEST_ENV_FLAG).get('gw_file_name')
gw_file_name_DriverErr = f"{gw_file_name.split('.')[0]}_DriverErr.xml"
gw_file_name_AppErr = f"{gw_file_name.split('.')[0]}_AppErr.xml"
gw_file_name_CRCErr = f"{gw_file_name.split('.')[0]}_CRCErr.xml"
gw_file_name_FF01Err = f"{gw_file_name.split('.')[0]}_FF01Err.xml"

gw_file_path_E11_GW = UDS_DATA.get(TEST_ENV_FLAG).get('gw_file_path_E11_GW')
gw_file_name_E11_GW = UDS_DATA.get(TEST_ENV_FLAG).get('gw_file_name_E11_GW')

TBOX_file_path = UDS_DATA.get(TEST_ENV_FLAG).get('TBOX_file_path')
TBOX_file_name = UDS_DATA.get(TEST_ENV_FLAG).get('TBOX_file_name')
TBOX_file_name_DriverErr = f"{TBOX_file_name.split('.')[0]}_DriErr.xml"
TBOX_file_name_AppErr = f"{TBOX_file_name.split('.')[0]}_AppErr.xml"
TBOX_file_name_CRCErr = f"{TBOX_file_name.split('.')[0]}_CRCErr.xml"
TBOX_file_name_FF01Err = f"{TBOX_file_name.split('.')[0]}_FF01Err.xml"

# TMSV 1.0.006-B0010000.B003
TMS_file_path = UDS_DATA.get(TEST_ENV_FLAG).get('TMS_file_path')
TMS_file_name = UDS_DATA.get(TEST_ENV_FLAG).get('TMS_file_name')
TMS_file_name_app = f"{TMS_file_name.split('.')[0]}_App.xml"
TMS_file_name_Cal = f"{TMS_file_name.split('.')[0]}_Cal.xml"
TMS_file_name_DriverErr = f"{TMS_file_name.split('.')[0]}_DriErr.xml"
TMS_file_name_AppErr = f"{TMS_file_name.split('.')[0]}_AppErr.xml"
TMS_file_name_CRCErr = f"{TMS_file_name.split('.')[0]}_CalErr.xml"
TMS_file_name_FF01 = f"{TMS_file_name.split('.')[0]}_FF01.xml"

VCU_file_path = UDS_DATA.get(TEST_ENV_FLAG).get('VCU_file_path')
VCU_file_name = UDS_DATA.get(TEST_ENV_FLAG).get('VCU_file_name')
VCU_file_name_CRCErr = f"{VCU_file_name.split('.')[0]}_CRCErr.xml"
VCU_file_name_FF01Err = f"{VCU_file_name.split('.')[0]}_FF01Err.xml"
VCU_file_name_DErr = f"{VCU_file_name.split('.')[0]}_DErr.xml"
VCU_file_name_app = f"{VCU_file_name.split('.')[0]}_app.xml"
VCU_file_name_cal = f"{VCU_file_name.split('.')[0]}_cal.xml"

MDC_file_path = UDS_DATA.get(TEST_ENV_FLAG).get('MDC_file_path')
MDC_file_name = UDS_DATA.get(TEST_ENV_FLAG).get('MDC_file_name')
MDC_file_name_DriverErr = f"{MDC_file_name.split('.')[0]}_DriverErr.xml"
MDC_file_name_CRCErr = f"{MDC_file_name.split('.')[0]}_CRCErr.xml"
MDC_file_name_FF01Err = f"{MDC_file_name.split('.')[0]}_FF01Err.xml"

VDC_file_path = UDS_DATA.get(TEST_ENV_FLAG).get('VDC_file_path')
VDC_file_name = UDS_DATA.get(TEST_ENV_FLAG).get('VDC_file_name')
VDC_file_name_DriverErr = f"{VDC_file_name.split('.')[0]}_DriverErr.xml"
VDC_file_name_CRCErr = f"{VDC_file_name.split('.')[0]}_CRCErr.xml"
VDC_file_name_FF01Err = f"{VDC_file_name.split('.')[0]}_FF01Err.xml"

VIU1_file_path = UDS_DATA.get(TEST_ENV_FLAG).get('VIU1_file_path')
VIU1_file_name = UDS_DATA.get(TEST_ENV_FLAG).get('VIU1_file_name')
VIU1_file_name_DriverErr = f"{VIU1_file_name.split('.')[0]}_DriverErr.xml"
VIU1_file_name_CRCErr = f"{VIU1_file_name.split('.')[0]}_CRCErr.xml"
VIU1_file_name_FF01Err = f"{VIU1_file_name.split('.')[0]}_FF01Err.xml"

VIU2_file_path = UDS_DATA.get(TEST_ENV_FLAG).get('VIU2_file_path')
VIU2_file_name = UDS_DATA.get(TEST_ENV_FLAG).get('VIU2_file_name')
VIU2_file_name_DriverErr = f"{VIU2_file_name.split('.')[0]}_DriverErr.xml"
VIU2_file_name_CRCErr = f"{VIU2_file_name.split('.')[0]}_CRCErr.xml"
VIU2_file_name_FF01Err = f"{VIU2_file_name.split('.')[0]}_FF01Err.xml"

VIU3_file_path = UDS_DATA.get(TEST_ENV_FLAG).get('VIU3_file_path')
VIU3_file_name = UDS_DATA.get(TEST_ENV_FLAG).get('VIU3_file_name')
VIU3_file_name_DriverErr = f"{VIU3_file_name.split('.')[0]}_DriverErr.xml"
VIU3_file_name_CRCErr = f"{VIU3_file_name.split('.')[0]}_CRCErr.xml"
VIU3_file_name_FF01Err = f"{VIU3_file_name.split('.')[0]}_FF01Err.xml"

CDC_file_path = UDS_DATA.get(TEST_ENV_FLAG).get('CDC_file_path')
CDC_file_name = UDS_DATA.get(TEST_ENV_FLAG).get('CDC_file_name')
CDC_file_name_CRCErr = f"{CDC_file_name.split('.')[0]}_CRCErr.xml"
CDC_file_name_APPError = f"{CDC_file_name.split('.')[0]}_AppErr.xml"
CDC_file_name_DriverErr = f"{CDC_file_name.split('.')[0]}_DriverErr.xml"

MCU_file_path = UDS_DATA.get(TEST_ENV_FLAG).get('MCU_file_path')
MCU_file_path_mcuf = UDS_DATA.get(TEST_ENV_FLAG).get('MCU_file_path_mcuf')
MCU_file_name_mcuf = UDS_DATA.get(TEST_ENV_FLAG).get('MCU_file_name_mcuf')
MCU_file_name = UDS_DATA.get(TEST_ENV_FLAG).get('MCU_file_name')
MCU_file_name_CRCErr = f"{MCU_file_name.split('.')[0]}_CRCErr.xml"
MCU_file_name_App = f"{MCU_file_name.split('.')[0]}_app.xml"
MCU_file_name_FF01Err = f"{MCU_file_name.split('.')[0]}_FF01Err.xml"
MCU_file_name_DErr = f"{MCU_file_name.split('.')[0]}_DErr.xml"
MCU_file_name_Cal = f"{MCU_file_name.split('.')[0]}_cal.xml"

PDU_file_path = UDS_DATA.get(TEST_ENV_FLAG).get('PDU_file_path')
PDU_file_name = UDS_DATA.get(TEST_ENV_FLAG).get('PDU_file_name')
PDU_file_name_CRCErr = f"{PDU_file_name.split('.')[0]}_CRCErr.xml"
PDU_file_name_FF01Err = f"{PDU_file_name.split('.')[0]}_FF01Err.xml"
PDU_file_name_DriverErr = f"{PDU_file_name.split('.')[0]}_DriverErr.xml"
PDU_file_name_AppErr = f"{PDU_file_name.split('.')[0]}_AppErr.xml"

# SOP脱B版本
MCU_file_path_B = UDS_DATA.get(TEST_ENV_FLAG).get('MCU_file_path_B')
MCU_file_path_mcuf_B = UDS_DATA.get(TEST_ENV_FLAG).get('MCU_file_path_mcuf_B')
MCU_file_name_mcuf_B = UDS_DATA.get(TEST_ENV_FLAG).get('MCU_file_name_mcuf_B')
MCU_file_name_B = UDS_DATA.get(TEST_ENV_FLAG).get('MCU_file_name_B')
MCU_file_name_CRCErr_B = f"{MCU_file_name_B.split('.')[0]}_CRCErr.xml"
MCU_file_name_App_B = f"{MCU_file_name_B.split('.')[0]}_app.xml"
MCU_file_name_FF01Err_B = f"{MCU_file_name_B.split('.')[0]}_FF01Err.xml"
MCU_file_name_DErr_B = f"{MCU_file_name_B.split('.')[0]}_DErr.xml"
MCU_file_name_Cal_B = f"{MCU_file_name_B.split('.')[0]}_cal.xml"

"""===================================================UDS_CTRL参数================================================="""
# TLS接入认证开关
accessTLS = False

# 车辆ID
VEHICLE_ID_DICT = {"N61": 0, "E11": 1, "X2": 2, "E12": 3, "F2": 4}
VEHICLE_ID = VEHICLE_ID_DICT.get(PROJECT, '')

# ECU ID
ECU_ID_DICT = {
    "N61": {
        "TBOX": 1,
        "GW": 2,
        "CDC": 3,
        "MDC": 4,
        "VCU": 5,
        "PDU": 6,
        "TMS": 7,
        "MCU_F": 9,
        "MCU_R": 10
    },
    "E11": {
        "TBOX": 1,
        "GW": 2,
        "CDC": 3,
        "MDC": 4,
        "VCU": 5,
        "MCU_R": 6,
        "MCU_F": 7,
        "PDU": 9,
        "BMS": 10,
        "TMS": 12
    },
    "X2": {
        "TBOX": 1,
        "CDC": 3,
        "MDC": 4,
        "VIU_F": 37,
        "VIU_R": 38,
        "VIU_ML": 39,
        "VIU_MR": 40,
        "TMS": 7,
        "VDC": 41
    },
    "E12": {
        "TBOX": 1,
        "GW": 2,
        "CDC": 3,
        "MDC": 4,
        "VCU": 5,
        "MCU_R": 6,
        "MCU_F": 7,
        "PDU": 9,
        "TMS": 12
    },
    "F2": {
        "TBOX": 1,
        "CDC": 3,
        "MDC": 4,
        "VIU_F": 37,
        "VIU_R": 38,
        "VIU_ML": 39,
        "VIU_MR": 40,
        "TMS": 7,
        "VDC": 41
    },
    'X1': {}
}
ECU_ID = ECU_ID_DICT.get(PROJECT, '')

# 部件IP地址和逻辑寻址
ECU_ADDRESS_DICT = {
    "N61": {"TBOX": {"IP": "192.168.69.1", "PHYSICAL_ADDRESS": 0x0001, "TCPLINK_PHYSICAL_ADDRESS": 0x0001},
            "GW": {"IP": "192.168.69.21", "PHYSICAL_ADDRESS": 0x0002, "TCPLINK_PHYSICAL_ADDRESS": 0x0002},
            "CDC": {"IP": "192.168.69.6", "PHYSICAL_ADDRESS": 0x0300, "TCPLINK_PHYSICAL_ADDRESS": 0x0300},
            "MDC": {"IP": "192.168.69.41", "PHYSICAL_ADDRESS": 0x0400, "TCPLINK_PHYSICAL_ADDRESS": 0x0400},
            "VCU": {"IP": "192.168.69.36", "PHYSICAL_ADDRESS": 0x0100, "TCPLINK_PHYSICAL_ADDRESS": 0x0100},
            "PDU": {"IP": "192.168.69.36", "PHYSICAL_ADDRESS": 0x0102, "TCPLINK_PHYSICAL_ADDRESS": 0x0100},
            "TMS": {"IP": "192.168.69.36", "PHYSICAL_ADDRESS": 0x0105, "TCPLINK_PHYSICAL_ADDRESS": 0x0100},
            "MCU_F": {"IP": "192.168.69.36", "PHYSICAL_ADDRESS": 0x0103, "TCPLINK_PHYSICAL_ADDRESS": 0x0100},
            "MCU_R": {"IP": "192.168.69.36", "PHYSICAL_ADDRESS": 0x0104, "TCPLINK_PHYSICAL_ADDRESS": 0x0100}
            },
    "E11": {"TBOX": {"IP": "192.168.69.1", "PHYSICAL_ADDRESS": 0x0001, "TCPLINK_PHYSICAL_ADDRESS": 0x0001},
            "GW": {"IP": "192.168.69.21", "PHYSICAL_ADDRESS": 0x0002, "TCPLINK_PHYSICAL_ADDRESS": 0x0002},
            "CDC": {"IP": "192.168.69.6", "PHYSICAL_ADDRESS": 0x0300, "TCPLINK_PHYSICAL_ADDRESS": 0x0300},
            "MDC": {"IP": "192.168.69.41", "PHYSICAL_ADDRESS": 0x0400, "TCPLINK_PHYSICAL_ADDRESS": 0x0400},
            "VCU": {"IP": "192.168.69.36", "PHYSICAL_ADDRESS": 0x0100, "TCPLINK_PHYSICAL_ADDRESS": 0x0100},
            "MCU_R": {"IP": "192.168.69.36", "PHYSICAL_ADDRESS": 0x0104, "TCPLINK_PHYSICAL_ADDRESS": 0x0100},
            "MCU_F": {"IP": "192.168.69.36", "PHYSICAL_ADDRESS": 0x0103, "TCPLINK_PHYSICAL_ADDRESS": 0x0100},
            "PDU": {"IP": "192.168.69.36", "PHYSICAL_ADDRESS": 0x0102, "TCPLINK_PHYSICAL_ADDRESS": 0x0100},
            "BMS": {"IP": "192.168.69.36", "PHYSICAL_ADDRESS": 0x0101, "TCPLINK_PHYSICAL_ADDRESS": 0x0100},
            "TMS": {"IP": "192.168.69.36", "PHYSICAL_ADDRESS": 0x0105, "TCPLINK_PHYSICAL_ADDRESS": 0x0100},
            },
    "X2": {"TBOX": {"IP": "192.168.69.8", "PHYSICAL_ADDRESS": 0x0001, "TCPLINK_PHYSICAL_ADDRESS": 0x0006},
           "VDC_MCU": {"IP": "192.168.69.8", "PHYSICAL_ADDRESS": 0x0008,
                       "TCPLINK_PHYSICAL_ADDRESS": 0x0006},
           "CDC": {"IP": "192.168.69.8", "PHYSICAL_ADDRESS": 0x0300, "TCPLINK_PHYSICAL_ADDRESS": 0x0006},
           "MDC": {"IP": "192.168.69.11", "PHYSICAL_ADDRESS": 0x0400, "TCPLINK_PHYSICAL_ADDRESS": 0x0006},
           # VIU 挂靠在VDC下面，ip使用VDC_MPU的192.168.69.8, 逻辑地址使用自身的0x0004，但是TCPLINK_PHYSICAL_ADDRESS使用VDC的0x0006
           "VIU_F": {"IP": "192.168.69.8", "PHYSICAL_ADDRESS": 0x0004, "TCPLINK_PHYSICAL_ADDRESS": 0x0006},
           "VIU_R": {"IP": "192.168.69.8", "PHYSICAL_ADDRESS": 0x0003, "TCPLINK_PHYSICAL_ADDRESS": 0x0006},
           "VIU_ML": {"IP": "192.168.69.8", "PHYSICAL_ADDRESS": 0x0002, "TCPLINK_PHYSICAL_ADDRESS": 0x0006},
           "VIU_MR": {"IP": "192.168.69.8", "PHYSICAL_ADDRESS": 0x0005, "TCPLINK_PHYSICAL_ADDRESS": 0x0006},
           "VDC": {"IP": "192.168.69.8", "PHYSICAL_ADDRESS": 0x0006, "TCPLINK_PHYSICAL_ADDRESS": 0x0006},
           "TMS": {"IP": "192.168.69.8", "PHYSICAL_ADDRESS": 0x0105, "TCPLINK_PHYSICAL_ADDRESS": 0x0006}
           },
    "E12": {"TBOX": {"IP": "192.168.69.1", "PHYSICAL_ADDRESS": 0x0001, "TCPLINK_PHYSICAL_ADDRESS": 0x0001},
            "GW": {"IP": "192.168.69.21", "PHYSICAL_ADDRESS": 0x0002, "TCPLINK_PHYSICAL_ADDRESS": 0x0002},
            "CDC": {"IP": "192.168.69.6", "PHYSICAL_ADDRESS": 0x0300, "TCPLINK_PHYSICAL_ADDRESS": 0x0300},
            "MDC": {"IP": "192.168.69.41", "PHYSICAL_ADDRESS": 0x0400, "TCPLINK_PHYSICAL_ADDRESS": 0x0400},
            "VCU": {"IP": "192.168.69.36", "PHYSICAL_ADDRESS": 0x0100, "TCPLINK_PHYSICAL_ADDRESS": 0x0100},
            "MCU_R": {"IP": "192.168.69.36", "PHYSICAL_ADDRESS": 0x0104, "TCPLINK_PHYSICAL_ADDRESS": 0x0100},
            "MCU_F": {"IP": "192.168.69.36", "PHYSICAL_ADDRESS": 0x0103, "TCPLINK_PHYSICAL_ADDRESS": 0x0100},
            "PDU": {"IP": "192.168.69.36", "PHYSICAL_ADDRESS": 0x0102, "TCPLINK_PHYSICAL_ADDRESS": 0x0100},
            "TMS": {"IP": "192.168.69.36", "PHYSICAL_ADDRESS": 0x0105, "TCPLINK_PHYSICAL_ADDRESS": 0x0100},
            },
    "F2": {"TBOX": {"IP": "192.168.69.8", "PHYSICAL_ADDRESS": 0x0001, "TCPLINK_PHYSICAL_ADDRESS": 0x0006},
           "VDC_MCU": {"IP": "192.168.69.8", "PHYSICAL_ADDRESS": 0x0008,
                       "TCPLINK_PHYSICAL_ADDRESS": 0x0006},
           "CDC": {"IP": "192.168.69.8", "PHYSICAL_ADDRESS": 0x0300, "TCPLINK_PHYSICAL_ADDRESS": 0x0006},
           "MDC": {"IP": "192.168.69.11", "PHYSICAL_ADDRESS": 0x0400, "TCPLINK_PHYSICAL_ADDRESS": 0x0006},
           # VIU 挂靠在VDC下面，ip使用VDC_MPU的192.168.69.8, 逻辑地址使用自身的0x0004，但是TCPLINK_PHYSICAL_ADDRESS使用VDC的0x0006
           "VIU_F": {"IP": "192.168.69.8", "PHYSICAL_ADDRESS": 0x0004, "TCPLINK_PHYSICAL_ADDRESS": 0x0006},
           "VIU_R": {"IP": "192.168.69.8", "PHYSICAL_ADDRESS": 0x0003, "TCPLINK_PHYSICAL_ADDRESS": 0x0006},
           "VIU_ML": {"IP": "192.168.69.8", "PHYSICAL_ADDRESS": 0x0002, "TCPLINK_PHYSICAL_ADDRESS": 0x0006},
           "VIU_MR": {"IP": "192.168.69.8", "PHYSICAL_ADDRESS": 0x0005, "TCPLINK_PHYSICAL_ADDRESS": 0x0006},
           "VDC": {"IP": "192.168.69.8", "PHYSICAL_ADDRESS": 0x0006, "TCPLINK_PHYSICAL_ADDRESS": 0x0006},
           "TMS": {"IP": "192.168.69.8", "PHYSICAL_ADDRESS": 0x0105, "TCPLINK_PHYSICAL_ADDRESS": 0x0006}
           },
    'X1': {}
}
ECU_ADDRESS = ECU_ADDRESS_DICT.get(PROJECT, '')

# 诊断仪地址
TESTER_ADDRESS_DICT = {
    "N61": {
        "IP": "192.168.69.71",
        "PHYSICAL_ADDRESS": 0x0E80,
        "FUNCTIONAL_ADDRESS": 0xE400,
        "MULTICAST_IP": "239.2.0.1"
    },
    "E11": {
        "IP": "192.168.69.71",
        "PHYSICAL_ADDRESS": 0x0E80,
        "FUNCTIONAL_ADDRESS": 0xE400,
        "MULTICAST_IP": "224.2.0.1"
    },
    "X2": {
        "IP": "192.168.69.71",
        "PHYSICAL_ADDRESS": 0x0E80,
        "FUNCTIONAL_ADDRESS": 0xE400,
        "MULTICAST_IP": "239.2.0.1"
    },
    "E12": {
        "IP": "192.168.69.71",
        "PHYSICAL_ADDRESS": 0x0E80,
        "FUNCTIONAL_ADDRESS": 0xE400,
        "MULTICAST_IP": "224.2.0.1"
    },
    "F2": {
        "IP": "192.168.69.71",
        "PHYSICAL_ADDRESS": 0x0E80,
        "FUNCTIONAL_ADDRESS": 0xE400,
        "MULTICAST_IP": "239.2.0.1"
    },
    'X1': {}
}
TESTER_ADDRESS = TESTER_ADDRESS_DICT.get(PROJECT, "")

TLS_ADDRESS_DICT = {"N61": {"IP": "192.168.69.21", "PORT": 30504},
                    "E11": {"IP": "192.168.69.21", "PORT": 30504},
                    "X2": {"IP": "192.168.69.8", "PORT": 30504},
                    "E12": {"IP": "192.168.69.21", "PORT": 30504},
                    "F2": {"IP": "192.168.69.8", "PORT": 30504}
                    }
TLS_ADDRESS = TLS_ADDRESS_DICT.get(PROJECT, '')

KEY_FACTOR_DICT = {
    "N61": {"TBOX": [0x55, 0xE3, 0x06, 0x75, 0x4F, 0xD4, 0x62, 0x61, 0x0F, 0x02, 0x48, 0x8A, 0x90, 0xBA, 0xCE, 0xEA],
            "GW": [0xAF, 0x2E, 0x75, 0xA0, 0xC0, 0x34, 0xbf, 0x05, 0x3f, 0x72, 0xfe, 0x82, 0xd6, 0x12, 0x9a, 0xcd],
            "CDC": [0xED, 0xFC, 0x2C, 0xF7, 0x09, 0x6E, 0x46, 0x8F, 0xE9, 0xDC, 0xBB, 0x8C, 0x0B, 0xC8, 0xAD, 0xD4],
            "MDC": [0x6F, 0x0E, 0xAF, 0x3F, 0xEB, 0x15, 0x65, 0x64, 0xC9, 0xC7, 0xE2, 0x8E, 0x7C, 0x05, 0xCE, 0xCB],
            "VCU": [0x47, 0x87, 0xa9, 0xde, 0x79, 0x66, 0x54, 0x1f, 0x45, 0x0c, 0x2a, 0xfa, 0x08, 0xdc, 0x65, 0x9a],
            "PDU": [0x83, 0x48, 0x5C, 0x54, 0xA2, 0xE7, 0x0C, 0x6A, 0xC9, 0x5A, 0x6C, 0xE7, 0x1B, 0x94, 0x35, 0xDF],
            "TMS": [0x0C, 0x6C, 0x60, 0xA7, 0x36, 0xD2, 0x08, 0x32, 0x78, 0x2B, 0x67, 0xBF, 0x51, 0xBC, 0x01, 0x39],
            "MCU_F": [0xF2, 0x2E, 0xD9, 0xCE, 0xE6, 0x6D, 0x41, 0x8F, 0x07, 0x72, 0x00, 0x82, 0xA5, 0x41, 0xB5, 0x57],
            "MCU_R": [0x51, 0xA1, 0x2C, 0x4A, 0x67, 0x8E, 0xE0, 0x6D, 0x0F, 0x05, 0xF1, 0x46, 0x39, 0xD9, 0x0A, 0x63]
            },
    "E11": {"TBOX": [0x61, 0x01, 0xAE, 0x88],
            "GW": [0x49, 0x43, 0xB2, 0xD0],
            "CDC": [0xC6, 0x3E, 0x12, 0x34],
            "MDC": [0xBA, 0xB5, 0xDB, 0x65],
            "VCU": [0x7A, 0xE0, 0x17, 0x08],
            "MCU_R": [0xB6, 0x36, 0x55, 0x2A],
            "MCU_F": [0x6B, 0x04, 0xA5, 0x02],
            "PDU": [0x33, 0xF3, 0x3B, 0x09],
            "BMS": [0x24, 0x65, 0xBA, 0x2B],
            "TMS": [0xD1, 0xF7, 0x65, 0xDA]
            },
    "X2": {"TBOX": [0x8E, 0xA4, 0x0E, 0x70, 0x3C, 0xE2, 0x0E, 0x23, 0xFE, 0xB9, 0x24, 0x2B, 0x85, 0xE1, 0xFC, 0x00],
           "MDC": [0x63, 0xAA, 0x60, 0x5B, 0x6D, 0xCF, 0x91, 0x0D, 0xA2, 0x60, 0xC1, 0xDD, 0xDF, 0xE8, 0xB9, 0x7E],
           "TMS": [0x0C, 0x6C, 0x60, 0xA7, 0x36, 0xD2, 0x08, 0x32, 0x78, 0x2B, 0x67, 0xBF, 0x51, 0xBC, 0x01, 0x39],
           "CDC": [0xED, 0xFC, 0x2C, 0xF7, 0x09, 0x6E, 0x46, 0x8F, 0xE9, 0xDC, 0xBB, 0x8C, 0x0B, 0xC8, 0xAD, 0xD4],
           "VIU_F": [0x56, 0xF2, 0x90, 0x25, 0xEC, 0xEB, 0x2E, 0xD2, 0x55, 0x3B, 0xD4, 0x0E, 0xAD, 0x97, 0x41, 0xCB],
           "VIU_R": [0xBA, 0x71, 0x37, 0xA1, 0xE3, 0x8C, 0xAF, 0xF8, 0xEE, 0x53, 0xB0, 0x61, 0xA7, 0x72, 0xA8, 0x52],
           "VIU_ML": [0xDA, 0xCD, 0x3A, 0x55, 0xEA, 0x08, 0xF8, 0x10, 0x62, 0x31, 0x4B, 0x6E, 0xF0, 0xE4, 0x30, 0x11],
           "VIU_MR": [0xE0, 0xC2, 0x01, 0x4B, 0x08, 0x93, 0xE8, 0xA4, 0xB5, 0x94, 0xBA, 0xC5, 0x7C, 0xE6, 0x39, 0x91],
           "VDC": [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f]
           # TBD
           },
    "E12": {"TBOX": [0x61, 0x01, 0xAE, 0x88],
            "GW": [0x49, 0x43, 0xB2, 0xD0],
            "CDC": [0xC6, 0x3E, 0x12, 0x34],
            "MDC": [0xBA, 0xB5, 0xDB, 0x65],
            "VCU": [0x7A, 0xE0, 0x17, 0x08],
            "MCU_R": [0xB6, 0x36, 0x55, 0x2A],
            "MCU_F": [0x6B, 0x04, 0xA5, 0x02],
            "PDU": [0x33, 0xF3, 0x3B, 0x09],
            "TMS": [0xD1, 0xF7, 0x65, 0xDA]
            },
    "F2": {"TBOX": [0x8E, 0xA4, 0x0E, 0x70, 0x3C, 0xE2, 0x0E, 0x23, 0xFE, 0xB9, 0x24, 0x2B, 0x85, 0xE1, 0xFC, 0x00],
           "MDC": [0x63, 0xAA, 0x60, 0x5B, 0x6D, 0xCF, 0x91, 0x0D, 0xA2, 0x60, 0xC1, 0xDD, 0xDF, 0xE8, 0xB9, 0x7E],
           "TMS": [0x0C, 0x6C, 0x60, 0xA7, 0x36, 0xD2, 0x08, 0x32, 0x78, 0x2B, 0x67, 0xBF, 0x51, 0xBC, 0x01, 0x39],
           "CDC": [0xED, 0xFC, 0x2C, 0xF7, 0x09, 0x6E, 0x46, 0x8F, 0xE9, 0xDC, 0xBB, 0x8C, 0x0B, 0xC8, 0xAD, 0xD4],
           "VIU_F": [0x56, 0xF2, 0x90, 0x25, 0xEC, 0xEB, 0x2E, 0xD2, 0x55, 0x3B, 0xD4, 0x0E, 0xAD, 0x97, 0x41, 0xCB],
           "VIU_R": [0xBA, 0x71, 0x37, 0xA1, 0xE3, 0x8C, 0xAF, 0xF8, 0xEE, 0x53, 0xB0, 0x61, 0xA7, 0x72, 0xA8, 0x52],
           "VIU_ML": [0xDA, 0xCD, 0x3A, 0x55, 0xEA, 0x08, 0xF8, 0x10, 0x62, 0x31, 0x4B, 0x6E, 0xF0, 0xE4, 0x30, 0x11],
           "VIU_MR": [0xE0, 0xC2, 0x01, 0x4B, 0x08, 0x93, 0xE8, 0xA4, 0xB5, 0x94, 0xBA, 0xC5, 0x7C, 0xE6, 0x39, 0x91],
           "VDC": [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f]
           # TBD
           },
    'X1': {}
}
KEY_FACTOR = KEY_FACTOR_DICT.get(PROJECT, '')

# 增加L3秘钥
KEY_FACTOR_L3_DICT = {
    "N61": {"TBOX": [0x55, 0xE3, 0x06, 0x75, 0x4F, 0xD4, 0x62, 0x61, 0x0F, 0x02, 0x48, 0x8A, 0x90, 0xBA, 0xCE, 0xEA],
            "GW": [0x76, 0xAD, 0x1E, 0xB4, 0x3A, 0xAA, 0xCD, 0x2A, 0xCC, 0x1B, 0x46, 0x79, 0x10, 0x50, 0x26, 0x9D],
            "CDC": [0xEB, 0x2D, 0xAB, 0x73, 0x6A, 0xC6, 0x62, 0xF2, 0x3D, 0x80, 0x52, 0x94, 0xEC, 0xA9, 0x97, 0x54],
            "MDC": [0xA3, 0x47, 0xE3, 0x22, 0x8C, 0x51, 0x1F, 0x83, 0x5A, 0x2E, 0x46, 0xB3, 0x73, 0x97, 0x44, 0x62],
            "VCU": [0x00, 0x95, 0xf3, 0x93, 0xa7, 0x10, 0x61, 0xcc, 0x33, 0x82, 0x86, 0x16, 0xbf, 0x33, 0x30, 0xa3],
            "ECC": [0x00, 0xa9, 0x40, 0x10, 0x48, 0x57, 0xe0, 0x6e, 0x95, 0x7e, 0x06, 0x39, 0xe8, 0xe0, 0x7f, 0x1f],
            "PDU": [0xCE, 0x66, 0xC3, 0x7B, 0xC1, 0x4F, 0x03, 0x88, 0x9A, 0x65, 0xE2, 0x7C, 0x81, 0x40, 0xFE, 0xC6],
            "MCU_F": [0xAB, 0xA3, 0x19, 0x33, 0xD9, 0x54, 0x7E, 0xD6, 0x91, 0xEF, 0x38, 0x21, 0xC8, 0x10, 0x77, 0xEE],
            "MCU_R": [0x61, 0x94, 0xE5, 0xE3, 0x47, 0xDA, 0x67, 0x43, 0xBE, 0x7E, 0x93, 0xF2, 0x79, 0x9E, 0xD8, 0xF0],
            },
    "X2": {"TBOX": [0x55, 0xE3, 0x06, 0x75, 0x4F, 0xD4, 0x62, 0x61, 0x0F, 0x02, 0x48, 0x8A, 0x90, 0xBA, 0xCE, 0xEA],
           "MDC": [0x62, 0xA4, 0x38, 0x83, 0xB2, 0xCC, 0xF4, 0x9E, 0x80, 0x49, 0xEC, 0x73, 0xEB, 0x12, 0x6D, 0x0C],
           "TMS": [0x00, 0xa9, 0x40, 0x10, 0x48, 0x57, 0xe0, 0x6e, 0x95, 0x7e, 0x06, 0x39, 0xe8, 0xe0, 0x7f, 0x1f],
           "CDC": [0xEB, 0x2D, 0xAB, 0x73, 0x6A, 0xC6, 0x62, 0xF2, 0x3D, 0x80, 0x52, 0x94, 0xEC, 0xA9, 0x97, 0x54],
           "VIU_F": [0xD1, 0xEF, 0x35, 0xAF, 0xA2, 0x16, 0x84, 0xE2, 0x36, 0xA0, 0xD3, 0x43, 0xCF, 0x8B, 0x95, 0xD2],
           "VIU_R": [0xEB, 0x66, 0x14, 0x8E, 0xD7, 0xBE, 0x09, 0x82, 0x96, 0xE4, 0xA9, 0x48, 0x0B, 0xE3, 0xD2, 0x97],
           "VIU_ML": [0x0A, 0xF7, 0x13, 0xA6, 0x49, 0xA7, 0xFD, 0x77, 0xEE, 0x8E, 0xFF, 0x04, 0x17, 0xCB, 0x75, 0x1A],
           "VIU_MR": [0x5D, 0x07, 0x58, 0x7F, 0x29, 0x85, 0x05, 0x07, 0xCA, 0x62, 0x44, 0x9B, 0x99, 0x0D, 0x98, 0x1E],
           "VDC": [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f]
           # TBD
           },
    "F2": {"TBOX": [0x55, 0xE3, 0x06, 0x75, 0x4F, 0xD4, 0x62, 0x61, 0x0F, 0x02, 0x48, 0x8A, 0x90, 0xBA, 0xCE, 0xEA],
           "MDC": [0x62, 0xA4, 0x38, 0x83, 0xB2, 0xCC, 0xF4, 0x9E, 0x80, 0x49, 0xEC, 0x73, 0xEB, 0x12, 0x6D, 0x0C],
           "TMS": [0x00, 0xa9, 0x40, 0x10, 0x48, 0x57, 0xe0, 0x6e, 0x95, 0x7e, 0x06, 0x39, 0xe8, 0xe0, 0x7f, 0x1f],
           "CDC": [0xEB, 0x2D, 0xAB, 0x73, 0x6A, 0xC6, 0x62, 0xF2, 0x3D, 0x80, 0x52, 0x94, 0xEC, 0xA9, 0x97, 0x54],
           "VIU_F": [0xD1, 0xEF, 0x35, 0xAF, 0xA2, 0x16, 0x84, 0xE2, 0x36, 0xA0, 0xD3, 0x43, 0xCF, 0x8B, 0x95, 0xD2],
           "VIU_R": [0xEB, 0x66, 0x14, 0x8E, 0xD7, 0xBE, 0x09, 0x82, 0x96, 0xE4, 0xA9, 0x48, 0x0B, 0xE3, 0xD2, 0x97],
           "VIU_ML": [0x0A, 0xF7, 0x13, 0xA6, 0x49, 0xA7, 0xFD, 0x77, 0xEE, 0x8E, 0xFF, 0x04, 0x17, 0xCB, 0x75, 0x1A],
           "VIU_MR": [0x5D, 0x07, 0x58, 0x7F, 0x29, 0x85, 0x05, 0x07, 0xCA, 0x62, 0x44, 0x9B, 0x99, 0x0D, 0x98, 0x1E],
           "VDC": [0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07, 0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f]
           # TBD
           },
    'X1': {}
}
KEY_FACTOR_L3 = KEY_FACTOR_L3_DICT.get(PROJECT, '')

# ECU重启时间规格
ECUReset_time = {
    "X2": {"TBOX": 30,
           "MDC": 30,
           "TMS": 30,
           "CDC": 30,
           "VIU_F": 30,
           "VIU_R": 30,
           "VIU_ML": 30,
           "VIU_MR": 30,
           "VDC": 30  # 待定
           },
    "F2": {"TBOX": 30,
           "MDC": 30,
           "TMS": 30,
           "CDC": 30,
           "VIU_F": 30,
           "VIU_R": 30,
           "VIU_ML": 30,
           "VIU_MR": 30,
           "VDC": 30  # 待定
           }
}

# 追溯码设备ID映射表
deviceTypeId = {'TBOX': 0x000100, 'GW': 0x000200, 'VCU': 0x010000, 'PDU': 0x010200, 'MCU_F': 0x010300,
                'MCU_R': 0x010400, 'TMS': 0x010500, 'CDC-车机': 0x030000, 'CDC-显示屏': 0x030001,
                'MDC': 0x040000, 'LidarFC': 0x040001, 'LidarFL': 0x040002, 'LidarFR': 0x040003,
                'RadarFC': 0x040004, 'RadarRC': 0x040005, 'RadarFL': 0x040006, 'RadarFR': 0x040007,
                'RadarRL': 0x040008, 'RadarRR': 0x040009, 'INS': 0x04000A, 'BMS': 0x010100}

##########################################################固定参数####################################################
"""===================================================项目基础文件夹路径================================================="""
# 自动化文件夹基础路径
PROJECT_ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..'))
PROJECT_RESULT_PATH = os.path.abspath(os.path.join(PROJECT_ROOT_PATH, 'Result'))
PROJECT_DETAIL_PATH = os.path.abspath(os.path.join(PROJECT_RESULT_PATH, 'details'))
PROJECT_TESTCASE_PATH = os.path.join(os.path.join(PROJECT_ROOT_PATH, 'TestCase'))
PROJECT_TESTAW_PATH = os.path.join(os.path.join(PROJECT_ROOT_PATH, 'TestAW'))
PROJECT_LIBS_PATH = os.path.join(os.path.join(PROJECT_ROOT_PATH, 'Libs'))
SCENES_PATH = os.path.join(os.path.join(PROJECT_ROOT_PATH, 'TestData'))
PROJECT_FUNCTIONS_PATH = os.path.join(os.path.join(PROJECT_ROOT_PATH, 'Functions'))
PROJECT_FRAMEWORK_PATH = os.path.join(os.path.join(PROJECT_ROOT_PATH, 'FrameWork'))
PROJECT_TESTDATA_PATH = os.path.join(os.path.join(PROJECT_ROOT_PATH, 'TestData'))
PROJECT_TEMPLATE_PATH = os.path.join(os.path.join(PROJECT_TESTCASE_PATH, 'template'))
PROJECT_TESTENV_PATH = os.path.join(os.path.join(PROJECT_ROOT_PATH, 'TestEnv'))

"""===================================================ADB参数================================================="""
ATX_SERVER_PATH = '/data/local/tmp/atx-agent  server -d'
# 杀掉adb程序
ADB_EXE = r"taskkill /im adb.exe -f"
"""===================================================HMI_CTRL参数================================================="""
# hmi弹窗截图路径
FULL_SCR_PATH = os.path.join(PROJECT_FUNCTIONS_PATH, r'Public_Automation_Testing_Framework_WL\picture')
#  截图切分路径
PART_SCR_PATH = os.path.join(FULL_SCR_PATH, 'test')
#  图集路径
ATLAS_SCR_PATH = os.path.join(FULL_SCR_PATH, 'pic_database')

"""===================================================OTA_CTRL参数================================================="""
# 自动化代理账号
ACCOUNT = "lwx1265618"
PASSWD = ""
# SSID(WIFI账号密码)
ssid = ''
ssid_password = ''

SILENCE_SCHEDULE_DELTATIME = 15  # 升级任务定时时间
MAX_CHECK_UP_TIME = 10  # 点击检查更新后等待时间 s
MAX_DOWNLOAD_TIME = 600  # 最大下载时间 s
MAX_CHECK_INS_TIME = 15  # 升级前条件检查最大时间
MAX_EXCUTE_INS_TIME = 15  # 升级前条件检查最大时间
CASE_TIME = 5600  # 用例执行时长上限 s
TASK_CYCLE_TIME = 1200  # 用例任务状态循环超时次数 1200 次
TIME_OUT = 600  # 用例超时时间 s
DOWNLOAD_RETRY_TIME = 5000  # 静默下载断网重试时间
DOWNOAD_ETH_TRY = 5000  # 静默下载以太异常等待时间

# 车云状态分类
TASK_FAILED_STATE = ('回滚失败', '回滚成功', '升级失败')  # 任务失败
TASK_RELEASED_STATE = ['下发异常待重试', '下载失败待重试', '升级失败待重试']  # 失败待重试
TASK_SUCCESS_STATE = ['升级成功']  # 任务成功
# TASK_FINESHED_STATE = ['回滚失败', '升级失败', '回滚成功', 'ERROR', '无需升级', '任务撤销']  # 任务结束状态
TASK_FINESHED_STATE = ['回退失败', '任务失败', '任务取消', '升级成功', '回退成功', 'ERROR', '无需升级', '升级失败', '任务取消',
                       '未查询到当前任务的状态']  # 任务结束状态
TASK_FINALLY_STATE = ['升级中', '回滚中', '升级成功', '升级失败', '回滚成功', '回滚失败']
TASK_UNABLE_CANCEL = ['升级中', '回滚中', '升级成功', '无需升级']
TASK_DOWNLOAD_OK = ['下载成功', '等待用户确认升级', '升级中', '安装条件检查中', '安装条件检查结束', '安装倒计时', '安装准备', '升级成功']

STATUS = {
    'INIT': '初始状态', 'DOWNLOADED': '下载成功', 'DOWNLOADING': '下载中', 'DOWNLOAD_FAIL_CAN_RETRY': '下载失败',
    'DOWNLOAD_PAUSE': '暂停下载', 'WAITING_DOWNLOAD_CONFIRM': '等待用户确认下载', 'INSTALLED': '升级成功',
    'INSTALLING': '升级中', 'WAITING_TIME_INSTALL': '等待时间点升级', 'INSTALL_FAIL_CAN_RETRY': '升级失败',
    'WAITING_INSTALL_CONFIRM': '等待用户确认升级', 'INSTALL_FAIL_TO_ROLLBACK': '升级失败待回退',
    'ROLLBACKED': '回退成功', 'ROLLBACKING': '回退中', 'ROLLBACK_FAIL': '回退失败', 'TASK_FAIL': '升级失败',
    'TASK_CANCELED': '任务取消', 'DISPATCHING': '下发中', 'DISPATCHED': '已下发', 'DISPATCH_FAILED': '下发失败',
    'RETRYING': '重试中', 'CANCELING': '取消中', 'TASK_RECEIVED': '任务已接收', 'CONDITION_CHECK': '安装条件检查中',
    'CONDITION_CHECK_FIN': '安装条件检查结束', 'COUNTDOWN': '安装倒计时', 'INSTALL_CHECK': '安装准备',
    ' UPGRADE_SUSPEND': '安装暂停', 'NO_NEED_UPDATE': '无需升级', 'TASK_POLICIES_UPDATE': '升级策略变更',
    'ACTIVATING': '激活中',
}

ERROR_CODE = {
    "/": "/", "00000000": "/", "00000001": "参数错误", "00000002": "操作不支持",
    "00000003": "系统错误，请到“调试日志”导出查看详情",
    "00000004": "解密失败", "00000005": "磁盘空间不足", "00000006": "网络不可达，请检查车辆网络",
    "00000008": "切换高压异常",
    "00000009": "切换低压异常", "00000010": "进入OTA模式异常", "00000011": "退出OTA模式异常",
    "00000012": "服务暂不可用",
    "00000015": "任务接收异常", "00000016": "任务文件丢失或损坏", "00000132": "版本校验异常",
    "00001001": "升级前存在域校验失败",
    "00001002": "升级前条件检查超时", "00065536": "动力电池电量不足", "00065537": "蓄电池电压不足",
    "00065538": "档位未处于P档",
    "00065539": "充电状态不满足", "00065540": "正在进行近端诊断服务（OBD口被占用）", "00065541": "车速不满足",
    "00065542": "ready状态不满足", "00065543": "IG状态不满足", "00065544": "手刹状态不满足",
    "00065545": "车辆处于非设防状态",
    "00065546": "设防服务异常，请联系车控工程师确认", "00065548": "蓄电池电量不足", "00065550": "高压下电故障",
    "00065551": "正在执行哨兵模式，不允许升级", "00065553": "充电枪处于连接状态，无法进行系统升级",
    "00065554": "正在执行 Xcall业务，不允许升级",
    "00065555": "正在执行远控任务，不允许升级", "00065556": "正在执行诊断业务，不允许升级",
    "00065557": "正在恢复出厂设置，不允许升级",
    "00065558": "升级前检查VCU不允许升级，请联系VCU工程师确认", "00065559": "情景模式下，不允许升级",
    "00065560": "展车模式下，不允许升级",
    "00065561": "加油口盖未关闭", "00065562": "动力电池电量接口异常，请联系车控工程师确认",
    "00065563": "车速获取接口异常，请联系车控工程师确认",
    "00065564": "档位获取接口异常，请联系车控工程师确认", "00065565": "IG状态获取接口异常，请联系车控工程师确认",
    "00065566": "OBD口获取接口异常，请联系Vdc工程师确认",
    "00065567": "VCU整车允许刷写标志位接口异常，请联系车控工程师确认",
    "00065568": "蓄电池电量获取接口异常，请联系车控工程师确认", "00065569": "手刹状态接口异常，请联系车控工程师确认",
    "00065570": "快充枪连接状态接口异常，请联系车控工程师确认",
    "00065571": "充电枪连接状态接口异常，请联系车控工程师确认",
    "00065572": "加油口盖状态接口异常，请联系车控工程师确认",
    "00065573": "蓄电池电量百分比接口异常，请联系车控工程师确认",
    "00065574": "蓄电池voltage电压接口异常，请联系车控工程师确认", "00065575": "VCU升级服务异常，请上下电后重试",
    "00065576": "互斥服务异常，请联系车控工程师确认", "00065577": "展车模式获取接口异常，请联系车控工程师确认",
    "00065578": "智驾模式下，不允许升级",
    "00066562": "任务已撤销", "00066563": "任务刷写超时失败", "00066565": "当前网络类型与用户设置不匹配",
    "00066566": "蓄电池故障",
    "00066567": "下载时IG OFF暂停下载", "00066568": "整车版本校验不匹配", "00066569": "配套ECU版本校验不匹配",
    "00066570": "ECU版本校验不匹配", "00066571": "CAN唤醒失败", "00066572": "KL15唤醒失败",
    "00066573": "任务取消操作失败",
    "00066574": "保持高压失败", "00066575": "整车占用OBD状态失败", "00066576": "整车退出OBD状态失败",
    "00066577": "进入/退出升级模式时，整车OBD状态被占用", "00066578": "进入升级模式前检查失败",
    "00066579": "整车OTA模式保持失败",
    "00066580": "保持低压失败", "00066581": "升级条件检查超时", "00066582": "DID写入整车大版本失败",
    "00066583": "ECU版本获取失败",
    "00066584": "配套ECU版本获取失败", "00066585": "开启互斥失败", "00066586": "极致节能已生效",
    "00066587": "本地任务信息发生篡改，加载失败",
    "00066589": "FBL状态lock失败", "00066590": "状态机异常后自动复位",
    "00066591": "设置tbox休眠状态失败，请联系TBox工程师确认",
    "00066593": "获取fbl锁定状态失败，请联系车控工程师确认", "00066594": "请求刷写档位失败，请联系车控工程师确认",
    "00066595": "查询整车刷写档位，请联系车控工程师确认", "00066596": "保持fbl状态异常，请联系车控工程师确认",
    "00066597": "持久化任务信息失败",
    "00066598": "已经延迟到24小时之后不可延迟", "00066599": "自动预约升级任务失败", "00066600": "宠物模式中，无法升级",
    "00066603": "定时唤醒服务异常", "00066604": "部件更新失败，请重试", "00066605": "关闭DTC失败",
    "00066606": "打开DTC失败",
    "00066607": "清理DTC失败", "00066608": "KL15请求超时", "00066609": "任务初始化失败",
    "00066610": "Remote模式请求超时",
    "00066611": "OTA模式请求超时", "00066612": "授权信息不一致", "00066613": "刷写高压上电失败",
    "00066614": "刷写高压保持失败",
    "00066615": "刷写低压上电失败", "00066616": "刷写低压保持失败", "00100001": "TBox域错误：参数错误",
    "00100002": "TBox域错误：操作不支持错误", "00100003": "TBox域错误：系统错误，请到“调试日志”导出查看详情",
    "00100004": "TBox域错误：解密失败",
    "00100005": "TBox域错误：磁盘空间不足", "00100006": "TBox域错误：网络不可达，请检查车辆网络",
    "00100051": "TBox域错误：获取Inventory失败",
    "00100053": "TBox域错误：通知启动下载失败", "00100054": "TBox域错误：暂停下载失败",
    "00100055": "TBox域错误：获取资产信息中，系统忙碌",
    "00100056": "TBox域错误：撤销下载失败", "00100060": "TBox域错误：验签失败", "00100061": "TBox域错误：完整性验证失败",
    "00100063": "TBox域错误：通知升级前检查失败", "00100064": "TBox域错误：证书验证失败",
    "00100091": "TBox域错误：进入域的升级模式失败",
    "00100092": "TBox域错误：退出升级模式失败", "00100093": "TBox域错误：通知启动升级模式失败",
    "00100101": "TBox域错误：通知启动安装失败",
    "00100103": "TBox域错误：解压DC包失败", "00100104": "TBox域错误：部署安装包失败", "00100105": "TBox域错误：归档失败",
    "00100106": "TBox域错误：清理安装包失败", "00100121": "TBox域错误：通知启动激活失败",
    "00100131": "TBox域错误：升级失败：启动异常",
    "00100132": "TBox域错误：升级失败，版本校验异常", "00100141": "TBox域错误：通知启动回滚失败",
    "00100143": "TBox域错误：解压回滚包失败",
    "00100170": "TBox域错误：升级包不在位", "00100171": "TBox域错误：升级包错误", "00100172": "TBox域错误：回滚包不在位",
    "00100173": "TBox域错误：回滚包错误", "00100174": "TBox域错误：差分包基本版本错误",
    "00100175": "TBox域错误：域升级前检查失败",
    "00100180": "TBox域错误：调用installer网络异常", "00100182": "TBox域错误：OBD已被占用",
    "00100183": "TBox域错误：差分失败，写文件失败",
    "00100184": "TBox域错误：升级或回滚中出现磁盘空间不足", "00100187": "TBox域错误：差分失败，系统错误",
    "00100188": "TBox域错误：被通知停止，刷写失败", "00100190": "TBox域错误：授权文件校验失败",
    "00101001": "TBox域错误：升级前检查异常，可进行重试恢复", "00101002": "TBox域错误：升级前条件检查超时",
    "00166561": "Tbox域错误：调用UA网络异常",
    "00200001": "CDC域错误：参数错误", "00200002": "CDC域错误：操作不支持",
    "00200003": "CDC域错误：系统错误，请到“调试日志”导出查看详情",
    "00200004": "CDC域错误：解密失败", "00200005": "CDC域错误：磁盘空间不足",
    "00200006": "CDC域错误：网络不可达，请检查车辆网络",
    "00200051": "CDC域错误：获取Inventory失败", "00200053": "CDC域错误：通知启动下载失败",
    "00200054": "CDC域错误：暂停下载失败",
    "00200055": "CDC域错误：获取资产信息中，系统忙碌", "00200056": "CDC域错误：撤销下载失败",
    "00200060": "CDC域错误：验签失败",
    "00200061": "CDC域错误：完整性验证失败", "00200063": "CDC域错误：通知升级前检查失败",
    "00200064": "CDC域错误：证书验证失败",
    "00200091": "CDC域错误：进入域的升级模式失败", "00200092": "CDC域错误：退出升级模式失败",
    "00200093": "CDC域错误：通知启动升级模式失败",
    "00200100": "CDC域错误：切换分区失败", "00200101": "CDC域错误：通知启动安装失败",
    "00200103": "CDC域错误：解压DC包失败",
    "00200104": "CDC域错误：部署安装包失败", "00200105": "CDC域错误：归档失败", "00200106": "CDC域错误：清理安装包失败",
    "00200121": "CDC域错误：通知启动激活失败", "00200131": "CDC域错误：升级失败：启动异常",
    "00200132": "CDC域错误：升级失败，版本校验异常",
    "00200141": "CDC域错误：通知启动回滚失败", "00200143": "CDC域错误：解压回滚包失败",
    "00200170": "CDC域错误：升级包不在位",
    "00200171": "CDC域错误：升级包错误", "00200172": "CDC域错误：回滚包不在位", "00200173": "CDC域错误：回滚包错误",
    "00200174": "CDC域错误：差分包基本版本错误", "00200175": "CDC域错误：域升级前检查失败",
    "00200180": "CDC域错误：调用installer网络异常",
    "00200182": "CDC域错误：OBD已被占用", "00200183": "CDC域错误：差分失败，写文件失败",
    "00200184": "CDC域错误：升级或回滚中出现磁盘空间不足",
    "00200187": "CDC域错误：差分失败，系统错误", "00200188": "CDC域错误：被通知停止，刷写失败",
    "00200190": "CDC域错误：授权文件校验失败",
    "00201001": "CDC域错误：升级前检查异常，可进行重试恢复", "00201002": "CDC域错误：升级前条件检查超时",
    "00266561": "CDC域错误：调用UA网络异常",
    "00300001": "MDC域错误：参数错误", "00300002": "MDC域错误：操作不支持",
    "00300003": "MDC域错误：系统错误，请到“调试日志”导出查看详情",
    "00300004": "MDC域错误：解密失败", "00300005": "MDC域错误：磁盘空间不足", "00300006": "MDC域错误：网络不可达,网络异常",
    "00300051": "MDC域错误：获取Inventory失败", "00300053": "MDC域错误：通知启动下载失败",
    "00300054": "MDC域错误：暂停下载失败",
    "00300055": "MDC域错误：获取资产信息中，系统忙碌", "00300056": "MDC域错误：撤销下载失败",
    "00300060": "MDC域错误：验签失败",
    "00300061": "MDC域错误：完整性验证失败", "00300063": "MDC域错误：通知升级前检查失败",
    "00300064": "MDC域错误：证书验证失败",
    "00300091": "MDC域错误：进入域的升级模式失败", "00300092": "MDC域错误：退出升级模式失败",
    "00300093": "MDC域错误：通知启动升级模式失败",
    "00300101": "MDC域错误：通知启动安装失败", "00300103": "MDC域错误：解压DC包失败",
    "00300104": "MDC域错误：部署安装包失败",
    "00300105": "MDC域错误：归档失败", "00300106": "MDC域错误：清理安装包失败", "00300121": "MDC域错误：通知启动激活失败",
    "00300131": "MDC域错误：升级失败：启动异常", "00300132": "MDC域错误：升级失败，版本校验异常",
    "00300141": "MDC域错误：通知启动回滚失败",
    "00300143": "MDC域错误：解压回滚包失败", "00300170": "MDC域错误：升级包不在位", "00300171": "MDC域错误：升级包错误",
    "00300172": "MDC域错误：回滚包不在位", "00300173": "MDC域错误：回滚包错误",
    "00300174": "MDC域错误：差分包基本版本错误",
    "00300175": "MDC域错误：域升级前检查失败", "00300180": "MDC域错误：调用installer网络异常",
    "00300182": "MDC域错误：OBD已被占用",
    "00300183": "MDC域错误：差分失败，写文件失败", "00300184": "MDC域错误：升级或回滚中出现磁盘空间不足",
    "00300187": "MDC域错误：差分失败，系统错误",
    "00300188": "MDC域错误：被通知停止，刷写失败", "00300189": "MDC域错误：检查ADS-HMI-APK磁盘空间不足",
    "00300190": "MDC域错误：授权文件校验失败", "00301001": "MDC域错误：升级前检查异常，可进行重试恢复",
    "00301002": "MDC域错误：升级前条件检查超时",
    "00366561": "MDC域错误：调用UA网络异常", "00400001": "VDC域错误：参数错误", "00400002": "VDC域错误：操作不支持",
    "00400003": "VDC域错误：系统错误，请到“调试日志”导出查看详情", "00400004": "VDC域错误：解密失败",
    "00400005": "VDC域错误：磁盘空间不足",
    "00400006": "VDC域错误：网络不可达,网络异常", "00400051": "VDC域错误：获取Inventory失败",
    "00400053": "VDC域错误：通知启动下载失败",
    "00400054": "VDC域错误：暂停下载失败", "00400055": "VDC域错误：获取资产信息中，系统忙碌",
    "00400056": "VDC域错误：撤销下载失败",
    "00400060": "VDC域错误：验签失败", "00400061": "VDC域错误：完整性验证失败",
    "00400063": "VDC域错误：通知升级前检查失败",
    "00400064": "VDC域错误：证书验证失败", "00400091": "VDC域错误：进入域的升级模式失败",
    "00400092": "VDC域错误：退出升级模式失败",
    "00400093": "VDC域错误：通知启动升级模式失败", "00400101": "VDC域错误：通知启动安装失败",
    "00400103": "VDC域错误：解压DC包失败",
    "00400104": "VDC域错误：部署安装包失败", "00400105": "VDC域错误：归档失败", "00400106": "VDC域错误：清理安装包失败",
    "00400121": "VDC域错误：通知启动激活失败", "00400131": "VDC域错误：升级失败：启动异常",
    "00400132": "VDC域错误：升级失败，版本校验异常",
    "00400141": "VDC域错误：通知启动回滚失败", "00400143": "VDC域错误：解压回滚包失败",
    "00400170": "VDC域错误：升级包不在位",
    "00400171": "VDC域错误：升级包错误", "00400172": "VDC域错误：回滚包不在位", "00400173": "VDC域错误：回滚包错误",
    "00400174": "VDC域错误：差分包基本版本错误", "00400175": "VDC域错误：域升级前检查失败",
    "00400180": "VDC域错误：调用installer网络异常",
    "00400182": "VDC域错误：OBD已被占用", "00400183": "VDC域错误：差分失败，写文件失败",
    "00400184": "VDC域错误：升级或回滚中出现磁盘空间不足",
    "00400187": "VDC域错误：差分失败，系统错误", "00400188": "VDC域错误：被通知停止，刷写失败",
    "00400190": "VDC域错误：授权文件校验失败",
    "00401001": "VDC域错误：升级前检查异常，可进行重试恢复", "00401002": "VDC域错误：升级前条件检查超时",
    "00466561": "VDC域错误：调用UA网络异常"
}

TASK_TYPE = {'静默任务': 'SILENCE', '常规任务': 'NORMAL', '紧急任务': 'CRITICAL', }
# 任务类型
NORMAL_TASK = TASK_TYPE.get('常规任务')  # 常规任务
SILENCE_TASK = TASK_TYPE.get('静默任务')  # 静默任务
CRITICAL_TASK = TASK_TYPE.get('紧急任务')  # 紧急任务

EXECUTE_TYPE = {'立即执行': 'IMMEDIATE', '定时执行': 'SCHEDULED'}

# 触发类型
EXECUTE_IMME = EXECUTE_TYPE.get('立即执行')  # 立即执行
EXECUTE_SCHE = EXECUTE_TYPE.get('定时执行')  # 定时执行

TASK_TIMEOUT = {'6个月': 'SIX_MONTH', '12个月': 'ONE_YEAR', '长期': 'FOREVER'}

FAILED_ACTIONS = {'是': 'STOP'}

SILENCE_SCHEDULE_1 = 10  # 1级定时升级当前任务开始时间延迟 min
SILENCE_SCHEDULE_2 = 20  # 2级定时升级当前任务开始时间延迟 min
SILENCE_SCHEDULE_3 = 30  # 3级定时升级当前任务开始时间延迟 min
SILENCE_SCHEDULE_4 = 40  # 4级定时升级当前任务开始时间延迟 min

FAILACTION = 'STOP'
ROLLBACK = 'ROLLBACK'
TIMEOUTDURATION = 'SIX_MONTH'

CYCLE_TIME = 5  # 循环次数

CAR_FLAG = False  # 实车测试标志位

# HMI定时超时时间
HMI_SCHEDULE_DELAY = 5

# logic address
PDCU_ADDR = '0x0100'
MCUF_ADDR = '0x0103'
MCUR_ADDR = '0x0104'
TMS_ADDR = '0x0105'
BMS_ADDR = '0x0101'
PDU_ADDR = '0x0102'
CDC_ADDR = '0x0300'
MDC_ADDR = '0x0400'

#
CANCEL_DELTA_TIME = 120  # 执行撤销等待时间
PDU_FLASH_ADDR = '0x100'

# 升级时长
mdc_install_time = 20
mdc_rollback_time = 20

cdc_install_time = 15
cdc_rollback_time = 15

vgw_install_time = 3
vgw_rollback_time = 3

mcu_install_time = 4
mcu_rollback_time = 4

pdu_install_time = 5
pdu_rollback_time = 5

vcu_install_time = 3
vcu_rollback_time = 3

tbox_install_time = 5
tbox_rollback_time = 5

# 任务状态
INIT_STATE = {
    'vin': 'NONE',
    'taskID': 'NONE',
    'taskstate': 'ERROR',
    'taskprogress': '0',
    'taskname': 'NONE'
}

"""===================================================RELAY_CTRL参数================================================="""
SOC_LIMIT = 14  # 动力电池SOC额度（不满足升级条件）
BATTERY_SOC = 64  # 蓄电池SOC（不满足升级条件）

"""===================================================Ecu_Ctrl参数================================================="""
MDC_UPGRADE_CMD = "mdc-tool upgrade display version"
CLOSE_MDC_sysmonitor = 'pmupload --procName=unconfined rosparam set /SysMonitor/DirSpace/Switch 0 false true'
OPEN_MDC_sysmonitor = 'pmupload --procName=unconfined rosparam set /SysMonitor/DirSpace/Switch 1 false true'
MDC_OTA_PATH = "/home"
MDC_SPACE_FAIL = 'if=/dev/zero of=bigfile bs=1024M'
# MDC_BIF_FILE = '/home/mdc/ota/bigfile'
MDC_BIF_FILE = '/home/bigfile'
VDC_OTA_PATH = "/opt/ota_pkg/ota"
VDC_SPACE_FAIL = 'if=/dev/zero of=bigfile bs=102M'
VDC_BIF_FILE = '/opt/ota_pkg/ota/bigfile'
TBOX_OTA_PATH = "/mnt/upg/ota/duc/dc"
TBOX_SPACE_FAIL = 'if=/dev/zero of=bigfile bs=100M'
TBOX_BIF_FILE = '/mnt/upg/ota/duc/dc/bigfile'
FILE_REVISE = "mount -o rw,remount /"
SSH_ROOT_IP = "ssh root@192.168.2.76"
YES_SIGN = "yes"
EXIT_SIGN = "exit"
REBOOT_PAW = "Huawei12#$"
CLOSE_SIGN_VER = "scp /etc/ads/service/mdc_conf/swm_cfg_mdcpro610.json root@192.168.2.76:/etc/ads/service/mdc_conf/"
MDC_MAKE_ONE = "tar -zvcf 2-ADSE00112380S107227N61AB-C01.tar.gz ads_app/ board_base_firmware/ data_update/ " \
               "host_* mcu_app_firmware/ recovery/ sensors_firmware/ upgrade_toolbox/ version*"
MDC_MAKE_TWO = "tar -zvcf 2-ADSE00112380S108227N61AB-C01.tar.gz ads_app/ board_base_firmware/ data_update/" \
               " host_* mcu_app_firmware/ recovery/ sensors_firmware/ upgrade_toolbox/ version*"
MDC_MAKE_THREE = "tar -zvcf 2-ADSE00112380S109227N61AB-C01.tar.gz ads_app/ board_base_firmware/ data_update" \
                 "/ host_* mcu_app_firmware/ recovery/ sensors_firmware/ upgrade_toolbox/ version*"

MDC_PACKAGE_PATH = {
    0: ['/opt/ota/package', '回滚包'],
    1: ['/home/mdc/ota/3/working', '安装包']
}

# 删除部件安装包、回滚包路径（0：安装包 1：回滚包）
DEL_DOWNLOAD_ARCHIVE_PATH = {
    'CDC': ['/data/update/ota/manager/repository/work', ''], 'TBOX': ['/mnt/upg/ota/duc/dc/1/working/', ''],
    'VDC': ['/opt/ota_pkg/ota/dcPackage/4/working', '']}

# OTA升级日志路径
OtaManagerLog = {
    "X2": '/mnt/sdcard/ota/log/ota_manager.log',
    'X1': '',
}
OTA_MANAGER_LOG = OtaManagerLog.get(PROJECT)
# VDC 回滚包路径
VDC_REBOOT_PATH = '/mnt/sdcard/ota/4/archive/'
# TBOX/VDC本地回滚包
REBOOT_PATH = '/mnt/sdcard/ota/4/archive/'
# TBOX/VDC本地安装包
INSTALL_PATH = '/mnt/upg/ota/duc/dc/1/working/'
