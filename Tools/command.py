class DAQ970A:
    Read_CH11_VOLT = 'MEAS:VOLT:DC? 100, (@111)'
    Read_CH14_VOLT = 'MEAS:VOLT:DC? 100, (@114)'
    Read_CH13_VOLT = 'MEAS:VOLT:DC? 100, (@113)'
    Read_CH12_VOLT = 'MEAS:VOLT:DC? 100, (@112)'

#-----------------------------以下是JDK需要的指令--------------------------------

output_on="OUTP ON"
output_off="OUTP OFF"
SYST_query = "*IDN?"
class dc_ITCH:
    SYST_com_IT2806 = "ASRL16::INSTR"
    SYST_query = "*IDN?"
    SYST_control = "SYSTem:REMote"
    SYST_link = "SYST:COMM:SEL VCP"  # 设置当前通讯方式为VCP
    SYST_error = "SYSTem:ERRor?"
    OUTP_mode = "FUNC:MODE "
    OUTP_curr = "FUNC:MODE CURR"
    OUTP_volt = "FUNC:MODE VOLT"
    OUTP_on = "OUTP 1"
    OUTP_off = "OUTP 0"
    A_range = "CURR:RANG:AUTO 1"  # 设置当前电压/电流量程为自动模式
    V_range = "VOLT:RANG:AUTO 1"
    set_curr_range="CURR:RANG "  #最大是1A，
    A_set = "CURR "  # 后面直接加上所需设置的电压/电流数值
    V_set = "VOLT "
    A_meas = "MEAS:CURR?"  # meas测量方法比fetc测量更精准，但时间更长，根据项目需求选择
    V_meas = "MEAS:VOLT?"
    A_fetc = "FETC:CURR?"
    V_fetc = "FETC:VOLT?"
class ac_kikusui:
    set_ac115="VOLT 115"
    set_freq400="FREQ 400"
    local_button_lock="SYST:KLOC 1"

class dc_kikusui:
    set_dc_28="VOLT 28"
    set_dc="VOLT "
    local_button_lock="SYST:KLOC 1"
class Multimeter:
    set_command_standard="CMDS RIGOL"
    set_func_volt_dc="FUNC:VOLT:DC"
    set_func_curr_dc="FUNC:CURR:DC"
    set_func_volt_ac="FUNC:VOLT:AC"
    set_func_curr_ac="FUNC:CURR:AC"
    set_func_res="FUNC:RES"     #注意是二线电阻的命令
    set_func_freq="FUNC:FREQ"
    meas_volt_dc="MEAS:VOLT:DC?"
    meas_res="MEAS:RES?"
    set_range_meas="MEAS AUTO"
    meas_freq="MEAS:FREQ"
    meas_curr_dc="MEAS:CURR:DC?"
class dc_28VHquality:
    set_VCP="SYST:COMM:SEL VCP"
    set_volt="VOLT "
    set_curr_range_aoto="CURR:RANG:AUTO 1"
    system_error="SYSTem:ERRor?"

class signal_generator:
    channel_c1_freq="C1:BSWV FRQ,"
    channel_c1_vpp="C1:BSWV AMP,"
    channel_c1_sine="C1:BSWV WVTP,SINE"
    channel_c1_offset="C1:BSWV OFST,0"
    channel_c1_phase="C1:BSWV PHSE,0"
    channel_c1_open="C1:OUTP ON"
    channel_c1_off="C1:OUTP OFF"
    query_c1="C1:BSWV?"
class PowerSupply:
    Mode = 'SYST:CONF:NOUT '
    Range = 'VOLT:RANG '
    Curr = 'CURR '
    Volt = 'VOLT '
    OVP = 'VOLT:PROT:UPP '
    UVP = 'VOLT:PROT:LOW '
    SystRem = 'SYST:REM'
    CurrProt = 'CURR:PROT '
    VoltProt = 'Volt:PROT '
    VoltProtON = 'VOLT:PROT:STAT 1'
    VoltProtOFF = 'VOLT:PROT:STAT 0'
    OutPutON = 'OUTP 1'
    OutPutOFF = 'OUTP 0'
    DCVolt = 'VOLT:OFFS '
    ACHz = 'FREQ '
    ReadVolt = 'MEAS:VOLT:ACDC?'
    ReadACVolt = 'MEAS:VOLT'
    ReadCurr = 'MEAS:CURR:ACDC?'
    ReadPow = 'MEAS:POW:ACDC?'
    ReadDCVolt = 'MEAS:VOLT?'
    ReadDCCurr = 'MEAS:CURR?'
    ReadDCPow = 'MEAS:POW?'


class DCLoad:
    ModeCC = 'FUNC CURR'
    ModeCV = 'FUNC VOLT'
    ModeCP = 'FUNC POW'
    ModeCR = 'FUNC RES'
    RangCC = 'SOUR:CURR:RANG '
    RangCV = 'SOUR:VOLT:RANG '
    RangCP = 'SOUR:POW:RANG '
    RangCR = 'SOUR:RES:RANG '
    OCPON = 'CURR:PROT:STAT 1'
    OCPOFF = 'CURR:PROT:STAT 0'
    OCPSTATSEARCH = 'CURR:PROT:STAT?'
    OCP = 'CURR:PROT '
    ALLInputON = 'INP:ALL 1'
    ALLInputOFF = 'INP:ALL 0'
    InputON = 'INP 1'
    InputOFF = 'INP 0'
    Curr = 'CURR '
    Volt = 'VOLT '
    Res = 'RES '
    Pow = 'POW '
    Chan = 'CHAN '
    ReadAllVolt = 'MEAS:ALLV?'
    ReadAllCurr = 'MEAS:ALLC?'
    ReadAllPow = 'MEAS:ALLP?'


class Oscilloscope:
    RollMode = 'ACQ:MODE ROLL'
    Ch1ACCoup = 'CHAN1:COUP AC'
    ReadVPP = 'MEAS:ADV:P1:VAL?'
    ReadVrms = 'MEAS:ADV:P3:VAL?'
    SetTypePKPK = 'MEAS:ADV:P1:TYPE PKPK'
    VRange = 'CHAN1:SCAL 2.00E-01'
    TRange = 'TIM:SCAL 1.00E-02'
