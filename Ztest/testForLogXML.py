# import logging
# import xml.etree.ElementTree as ET
#
# # 2023-09-21 14:51:15,677 - AutoTestQThread.py do_DI_Test() [line:56] INFO - Interrupt DI Test!
# # 将日志文件转换为XML格式
# xml_root = ET.Element('TestResults')
# for line in open(r'2023-09-21.log', 'r', encoding='utf-8'):
#     d = (line.strip()).split(' ')
#     print(d)
#     log_message = ET.SubElement(xml_root, 'message')
#     log_message.text = '\n' + "".join(d) + '\n'
#     log_date = ET.SubElement(log_message, 'date')
#     log_date.text = '\n' + "    " + d[0] + d[1] + '\n'
#     log_file = ET.SubElement(log_date, 'file')
#     log_file.text = '\n' + "    " * 2 + d[3] + '\n'
#     log_function = ET.SubElement(log_file, 'function')
#     log_function.text = '\n' + "    " * 3 + d[4] + '\n'
#
# # 将XML写入文件
# xml_tree = ET.ElementTree(xml_root)
# xml_tree.write('log.xml', encoding='utf-8', xml_declaration=True)
data = {
    'Personnel': {
        'Personnel': '人员信息',
        'CustomerRepresentative': '客户代表',
        'QualityAssurance': '质量监督员',
        'SystemOperator': '操作人员',
        'Extension': '其他人员',
    },
    'ResultSet': {
        'ResultSet': [1, 2, 3, 4, 5, 6, 7, 8, 9],  # 描述测试结果数据集合
    },
}

import xml.etree.ElementTree as ET
import xml.dom.minidom


def generate_test_log(filename='2023-09-21.log'):
    root = ET.Element('TestResults')
    root.set('attr1', 'value1')
    for line in open(filename, 'r', encoding='utf-8'):
        # 生成Personnel元素
        d = (line.strip()).split(' ')
        print(d)
        log_message = ET.SubElement(root, 'message')
        log_message.text = "".join(d)
        log_date = ET.SubElement(log_message, 'date')
        log_date.text = d[0] + d[1]
        log_file = ET.SubElement(log_date, 'file')
        log_file.text = d[3]
        log_function = ET.SubElement(log_file, 'function')
        log_function.text = d[4]
    # 添加SystemOperator、Extension等子元素

    # 生成其他元素,比如ResultSet、TestStation等
    # ......

    # 生成各种类型的元素,比如TestGroup、SessionAction
    # 根据test_data参数传入的数据生成元素内容

    # 设置属性

    # 调整格式
    xml_str = ET.tostring(root, encoding='utf8').decode('utf8')

    return xml.dom.minidom.parseString(xml_str).toprettyxml()


def generate_test_log_New(d):
    root = ET.Element(f'xs\:element')
    root.set('name', 'TestResults')
    # 生成Personnel元素
    root.text = '123'

    # 调整格式
    xml_str = ET.tostring(root, encoding='utf8').decode('utf8')

    return xml.dom.minidom.parseString(xml_str).toprettyxml()


if __name__ == '__main__':
    a = generate_test_log_New(data)
    print(a)
