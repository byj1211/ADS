# 以下为  电源型号的SCPI指令


# 以下为JDK_23项目所涉及的SCPI指令
SYST_com_IT6722 = "ASRL4::INSTR"
V_step = "VOLT:STEP "
V_query = "VOLT?"
V_up = "VOLT UP"
V_down = "VOLT DOWN"

#  IT2806电源输出控制命令
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
A_set = "CURR "  # 后面直接加上所需设置的电压/电流数值
V_set = "VOLT "
A_meas = "MEAS:CURR?"  # meas测量方法比fetc测量更精准，但时间更长，根据项目需求选择
V_meas = "MEAS:VOLT?"
A_fetc = "FETC:CURR?"
V_fetc = "FETC:VOLT?"
