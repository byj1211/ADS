from lxml import etree
import datetime
import os

# template_head = r'D:/codes/ATE/_Template'
report_head = r'.'


def generate_xsd_ResultSet(root, elements_with_comments):
    # 创建 xs:complexType 元素
    element = etree.SubElement(root, "{http://www.w3.org/2001/XMLSchema}element", name="ResultSet", type="TestGroup")

    # 创建 testGroup 元素
    TestGroup = etree.SubElement(element, "{http://www.w3.org/2001/XMLSchema}complexType", name="TestGroup")
    Test = etree.SubElement(TestGroup, "{http://www.w3.org/2001/XMLSchema}complexType", name="Test")

    attribute1 = etree.SubElement(Test, "{http://www.w3.org/2001/XMLSchema}attribute", name='ID',
                                  type='NonBlankString', use="required")
    attribute3 = etree.SubElement(Test, "{http://www.w3.org/2001/XMLSchema}attribute", name='startDateTime',
                                  type='dateTime', use="required")

    attribute5 = etree.SubElement(Test, "{http://www.w3.org/2001/XMLSchema}attribute", name='CycleNum',
                                  type='NonBlankString', use="required")
    attribute1.text = elements_with_comments.get('Test_ID')
    attribute3.text = elements_with_comments.get('Test_startDateTime')
    attribute5.text = elements_with_comments.get('Test_CycleNum')
    outcome = etree.SubElement(Test, "{http://www.w3.org/2001/XMLSchema}complexType", name="outCome")
    attribute6 = etree.SubElement(outcome, "{http://www.w3.org/2001/XMLSchema}simpleType", name="value",
                                  type="OutcomeValue",
                                  use="required")
    attribute6.text = elements_with_comments.get('outCome')
    testResult = etree.SubElement(Test, "{http://www.w3.org/2001/XMLSchema}complexType", name="testResult")
    testResultSeq = etree.SubElement(testResult, "{http://www.w3.org/2001/XMLSchema}sequence")

    e3 = etree.SubElement(testResultSeq, "{http://www.w3.org/2001/XMLSchema}element", name="TestLimits", minOccurs="0")
    ct = etree.SubElement(e3, "{http://www.w3.org/2001/XMLSchema}complexType")
    sq = etree.SubElement(ct, "{http://www.w3.org/2001/XMLSchema}sequence")
    e = etree.SubElement(sq, "{http://www.w3.org/2001/XMLSchema}element", name="Limits", type="Limit", minOccurs="1",
                         maxOccurs="unbounded")
    cpx = etree.SubElement(e, "{http://www.w3.org/2001/XMLSchema}complexType", name="Limit")
    seqq = etree.SubElement(cpx, "{http://www.w3.org/2001/XMLSchema}sequence")
    elm = etree.SubElement(seqq, "{http://www.w3.org/2001/XMLSchema}sequence", name="SingleLimit", minOccurs="1",
                           maxOccurs="unbounded")
    cpx = etree.SubElement(elm, "{http://www.w3.org/2001/XMLSchema}complexType")
    seqq = etree.SubElement(cpx, "{http://www.w3.org/2001/XMLSchema}sequence")
    e = etree.SubElement(seqq, "{http://www.w3.org/2001/XMLSchema}element", name="Data", type="Data", minOccurs="1",
                         maxOccurs="unbounded")

    ccc = etree.SubElement(e, "{http://www.w3.org/2001/XMLSchema}complexType", name="Data")
    name = etree.SubElement(ccc, "{http://www.w3.org/2001/XMLSchema}attribute", name="name", type="NonBlankString",
                            use="required")
    type = etree.SubElement(ccc, "{http://www.w3.org/2001/XMLSchema}attribute", name="type", type="NonBlankString",
                            use="required")
    direction = etree.SubElement(ccc, "{http://www.w3.org/2001/XMLSchema}attribute", name="direction",
                                 type="NonBlankString",
                                 use="required")
    upperLimit = etree.SubElement(ccc, "{http://www.w3.org/2001/XMLSchema}attribute", name="upperLimit",
                                  type="NonBlankString",
                                  use="required")

    name.text = elements_with_comments.get('Data_name')
    type.text = elements_with_comments.get('Data_type')
    direction.text = elements_with_comments.get('Data_direction')
    upperLimit.text = elements_with_comments.get('Data_upperLimit')

    seqq = etree.SubElement(cpx, "{http://www.w3.org/2001/XMLSchema}attribute", name="comparator", use="required")

    seqq.text = elements_with_comments.get('comparator')

    a1 = etree.SubElement(testResult, "{http://www.w3.org/2001/XMLSchema}attribute", name="ID", type='NonBlankString',
                          use='required')
    a2 = etree.SubElement(testResult, "{http://www.w3.org/2001/XMLSchema}attribute", name="name", use="required")

    a1.text = elements_with_comments.get('comparator_ID')
    a2.text = elements_with_comments.get('comparator_Name')
    return root


def generate_xsd_Personal(root, data):
    # 创建 xs:complexType 元素
    element = etree.SubElement(root, "{http://www.w3.org/2001/XMLSchema}element", name="Personnel", type="Personal")
    # 创建 xs:sequence 元素

    e = etree.SubElement(element, "{http://www.w3.org/2001/XMLSchema}complexType", name='SystemOperator', type='Person')

    a = etree.SubElement(e, "{http://www.w3.org/2001/XMLSchema}attribute", name='ID')
    b = etree.SubElement(e, "{http://www.w3.org/2001/XMLSchema}attribute", name='name')

    a.text = data.get('Person_ID')
    b.text = data.get('Person_name')

    return root


def generate_xsd_TestStation(root, elements_with_comments):
    element = etree.SubElement(root, "{http://www.w3.org/2001/XMLSchema}element", name="TestStation")
    annotation = etree.SubElement(element, "{http://www.w3.org/2001/XMLSchema}annotation")
    documentation = etree.SubElement(annotation, "{http://www.w3.org/2001/XMLSchema}documentation")
    documentation.text = '本元素用于描述测试时测试环境的状态'

    complexType = etree.SubElement(element, "{http://www.w3.org/2001/XMLSchema}complexType")
    sequence = etree.SubElement(complexType, "{http://www.w3.org/2001/XMLSchema}sequence")
    element = etree.SubElement(sequence, "{http://www.w3.org/2001/XMLSchema}element", name="Parts")
    complexType1 = etree.SubElement(element, "{http://www.w3.org/2001/XMLSchema}complexType")
    sequence1 = etree.SubElement(complexType1, "{http://www.w3.org/2001/XMLSchema}sequence")
    element = etree.SubElement(sequence1, "{http://www.w3.org/2001/XMLSchema}element", name="Part", type="Part")
    element.attrib["minOccurs"] = '1'
    element.attrib["maxOccurs"] = 'unbounded'

    attribute1 = etree.SubElement(element, "{http://www.w3.org/2001/XMLSchema}attribute", name='NameID',
                                  type='NonBlankString', use="required")
    attribute2 = etree.SubElement(element, "{http://www.w3.org/2001/XMLSchema}attribute", name='Name',
                                  type='NonBlankString', use="required")
    attribute3 = etree.SubElement(element, "{http://www.w3.org/2001/XMLSchema}attribute", name='SerialNumber',
                                  type='NonBlankString', use="required")
    attribute4 = etree.SubElement(element, "{http://www.w3.org/2001/XMLSchema}attribute", name='TypeID',
                                  type='NonBlankString', use="required")
    attribute5 = etree.SubElement(element, "{http://www.w3.org/2001/XMLSchema}attribute", name='Version',
                                  type='NonBlankString', use="required")
    attribute6 = etree.SubElement(element, "{http://www.w3.org/2001/XMLSchema}attribute", name='Calibration',
                                  type='NonBlankString', use="required")

    attribute1.text = elements_with_comments.get('Part_NameID')
    attribute2.text = elements_with_comments.get('Part_Name')
    attribute3.text = elements_with_comments.get('Part_SerialNumber')
    attribute4.text = elements_with_comments.get('Part_TypeID')
    attribute5.text = elements_with_comments.get('Part_Version')
    attribute6.text = elements_with_comments.get('Part_Calibration')
    return root


def generate_xsd_Site(root, data: dict):
    element = etree.SubElement(root, "{http://www.w3.org/2001/XMLSchema}element", name="Site", type="Organization")
    cp1 = etree.SubElement(element, "{http://www.w3.org/2001/XMLSchema}complexType", name="Organization")
    attr1 = etree.SubElement(cp1, "{http://www.w3.org/2001/XMLSchema}string", name="name", use="required")
    attr1.text = data.get('Organization_name')
    return root


def generate_xsd_UUT(root, elements_with_comments):
    element = etree.SubElement(root, "{http://www.w3.org/2001/XMLSchema}element", name="UUT")
    annotation = etree.SubElement(element, "{http://www.w3.org/2001/XMLSchema}annotation")
    documentation = etree.SubElement(annotation, "{http://www.w3.org/2001/XMLSchema}documentation")
    documentation.text = '本元素用于描述参与测试的被测设备的信息'

    complexType = etree.SubElement(element, "{http://www.w3.org/2001/XMLSchema}complexType")
    sequence = etree.SubElement(complexType, "{http://www.w3.org/2001/XMLSchema}sequence")
    element = etree.SubElement(sequence, "{http://www.w3.org/2001/XMLSchema}element", name="Parts")
    complexType1 = etree.SubElement(element, "{http://www.w3.org/2001/XMLSchema}complexType")
    sequence1 = etree.SubElement(complexType1, "{http://www.w3.org/2001/XMLSchema}sequence")
    element = etree.SubElement(sequence1, "{http://www.w3.org/2001/XMLSchema}element", name="Part", type="Part")
    element.attrib["minOccurs"] = '1'
    element.attrib["maxOccurs"] = 'unbounded'
    attribute1 = etree.SubElement(element, "{http://www.w3.org/2001/XMLSchema}attribute", name='NameID',
                                  type='NonBlankString', use="required")
    attribute2 = etree.SubElement(element, "{http://www.w3.org/2001/XMLSchema}attribute", name='Name',
                                  type='NonBlankString', use="required")
    attribute3 = etree.SubElement(element, "{http://www.w3.org/2001/XMLSchema}attribute", name='SerialNumber',
                                  type='NonBlankString', use="required")
    attribute4 = etree.SubElement(element, "{http://www.w3.org/2001/XMLSchema}attribute", name='TypeID',
                                  type='NonBlankString', use="required")
    attribute5 = etree.SubElement(element, "{http://www.w3.org/2001/XMLSchema}attribute", name='Version',
                                  type='NonBlankString', use="required")

    attribute1.text = elements_with_comments.get('UUT_NameID')
    attribute2.text = elements_with_comments.get('UUT_Name')
    attribute3.text = elements_with_comments.get('UUT_SerialNumber')
    attribute4.text = elements_with_comments.get('UUT_TypeID')
    attribute5.text = elements_with_comments.get('UUT_Version')


def generate_xsd_TestProgram(root, data):
    complexType = etree.SubElement(root, "{http://www.w3.org/2001/XMLSchema}complexType", name="TestProgram", )
    annotation = etree.SubElement(complexType, "{http://www.w3.org/2001/XMLSchema}annotation", )
    documentation = etree.SubElement(annotation, "{http://www.w3.org/2001/XMLSchema}documentation", )
    documentation.text = '产生结果数据的测试程序，定义待定'

    seq1 = etree.SubElement(complexType, "{http://www.w3.org/2001/XMLSchema}sequence", )
    element = etree.SubElement(seq1, "{http://www.w3.org/2001/XMLSchema}element", name="TestProcedures")
    cp1 = etree.SubElement(element, "{http://www.w3.org/2001/XMLSchema}complexType")
    seq2 = etree.SubElement(cp1, "{http://www.w3.org/2001/XMLSchema}sequence")
    element = etree.SubElement(seq2, "{http://www.w3.org/2001/XMLSchema}element", name="TestProcedure",
                               type="TestProcedure", minOccurs="1", maxOccurs="unbounded")
    cpx = etree.SubElement(element, "{http://www.w3.org/2001/XMLSchema}complexType", name="TestProcedure")
    TestProcedure_name = etree.SubElement(cpx, "{http://www.w3.org/2001/XMLSchema}attribute", name='name',
                                          type='NonBlankString', use="required")
    TestProcedure_ID = etree.SubElement(cpx, "{http://www.w3.org/2001/XMLSchema}attribute", name='ID',
                                        type='NonBlankString', use="required")
    TestProcedure_Version = etree.SubElement(cpx, "{http://www.w3.org/2001/XMLSchema}attribute", name='Version',
                                             type='NonBlankString', use="required")
    TestProcedure_name.text = data.get('TestProcedure_name')
    TestProcedure_ID.text = data.get('TestProcedure_ID')
    TestProcedure_Version.text = data.get('TestProcedure_Version')

    NameID = etree.SubElement(complexType, "{http://www.w3.org/2001/XMLSchema}attribute", name='NameID',
                              type='NonBlankString', use="required")
    Name = etree.SubElement(complexType, "{http://www.w3.org/2001/XMLSchema}attribute", name='Name',
                            type='NonBlankString', use="required")
    Version = etree.SubElement(complexType, "{http://www.w3.org/2001/XMLSchema}attribute", name='Version',
                               type='NonBlankString', use="required")
    Publish = etree.SubElement(complexType, "{http://www.w3.org/2001/XMLSchema}attribute", name='Publish',
                               type='NonBlankString', use="required")

    NameID.text = data.get('TestProgram_NameID')
    Name.text = data.get('TestProgram_Name')
    Version.text = data.get('TestProgram_Version')
    Publish.text = data.get('TestProgram_Publish')
    return root


def generate(alldata):
    # 创建根元素 xs:element
    root = etree.Element("{http://www.w3.org/2001/XMLSchema}element", name="TestResults")

    # 添加 xs:annotation 元素及其子元素
    annotation = etree.SubElement(root, "{http://www.w3.org/2001/XMLSchema}annotation")
    documentation = etree.SubElement(annotation, "{http://www.w3.org/2001/XMLSchema}documentation")
    documentation.text = "测试描述"

    complexType = etree.SubElement(root, "{http://www.w3.org/2001/XMLSchema}complexType")

    # 创建 xs:sequence 元素
    sequence = etree.SubElement(complexType, "{http://www.w3.org/2001/XMLSchema}sequence")

    generate_xsd_Personal(sequence, alldata)

    generate_xsd_ResultSet(sequence, alldata)

    generate_xsd_TestStation(sequence, alldata)

    generate_xsd_UUT(sequence, alldata)

    generate_xsd_Site(sequence, alldata)

    generate_xsd_TestProgram(sequence, alldata)
    xsd_content = etree.tostring(root, pretty_print=True, xml_declaration=True, encoding="utf-8").decode('utf-8')
    # 打印或使用 xsd_content
    time_string = datetime.datetime.now().strftime("%Y-%m-%d %H-%M")
    savefilename = os.path.basename(time_string + '_log' + '.xsd')
    savefullname = os.path.join(report_head, savefilename)
    with open(savefullname, 'w', encoding='utf-8') as f:
        f.write(xsd_content)
    return xsd_content


if __name__ == '__main__':
    alldata = {
        'Person_ID': "1",
        'Person_name': '1',
        'Test_ID': 'ID-1',
        'Test_startDateTime': 'startDateTime-1',
        'Test_CycleNum': '1',
        'outCome': 'Passed',
        'Data_name': 'name2-1',
        'Data_type': 'type2-1',
        'Data_direction': 'direction2',
        'Data_upperLimit': 'upperLimit2',
        'comparator': 'comparator1',
        'comparator_ID': 'id3-1',
        'comparator_Name': 'name3-1',
        'Part_NameID': "NameID-1",
        'Part_Name': 'Name-1',
        'Part_SerialNumber': 'SerialNumber-1',
        'Part_TypeID': 'TypeID-1',
        'Part_Version': 'Version-1',
        'Part_Calibration': 'Calibration-1',
        'UUT_NameID': 'NameID-1',
        'UUT_Name': 'Name-1',
        'UUT_SerialNumber': 'SerialNumber-1',
        'UUT_TypeID': 'TypeID-1',
        'UUT_Version': 'Version-1',
        'Organization_name': 'Organization_name-1',
        'TestProgram_NameID': 'NameID-1',
        'TestProgram_Name': 'Name-1',
        'TestProgram_Version': 'Version-1',
        'TestProgram_Publish': 'Publish-1',
        'TestProcedure_name': 'TestProcedure_name',
        'TestProcedure_ID': 'TestProcedure_ID',
        'TestProcedure_Version': 'TestProcedure_Version',
    }
    # 调用函数生成带有注释的XSD字符串
    xsd_content = generate(alldata)
