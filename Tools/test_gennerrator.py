


# 示例使用
response = "BSWV\sWVTP,SINE,FRQ,1000HZ,PERI,0.001S,AMP,4V,OFST,0V,HLEV,2V,LLEV,-2V,PHSE,0\n"  # 假设示波器返回的原始数据

frq, amp = extract_data(response)
print(frq)  # 输出提取出的FRQ数据
print(amp)  # 输出提取出的AMP数据
