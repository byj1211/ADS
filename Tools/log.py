import xml.etree.ElementTree as ET

# 解析XML文件

import xml.etree.ElementTree as ET

# tree = ET.parse('过程数据_测试日志格式过程传输示例.xml')
# root = tree.getroot()
# import xml.etree.ElementTree as ET

tree = ET.parse('过程数据_测试日志格式过程传输示例.xml')
root = tree.getroot()

def print_element_names(element):
    print(element.tag)  # 打印元素名称
    for child in element:
        print_element_names(child)  # 递归遍历子元素

print_element_names(root)

# # 解析 TestSummory 元素
# test_summory = root.find('TestSummory')
# session = test_summory.get('Session')
# id = test_summory.get('ID')
# end_datetime = test_summory.get('endDateTime')
# start_datetime = test_summory.get('startDateTime')
#
# print("Session: " + session)
# print("ID: " + id)
# print("End DateTime: " + end_datetime)
# print("Start DateTime: " + start_datetime)
#
# # 解析 TestStation 元素
# test_station = root.find('TestStation')
# test_name = test_station.get('name')
# name_id = test_station.get('NameID')
# type_id = test_station.get('TypeID')
# serial_number = test_station.get('SerialNumber')
#
# print("Test Name: " + test_name)
# print("Name ID: " + name_id)
# print("Type ID: " + type_id)
# print("Serial Number: " + serial_number)
