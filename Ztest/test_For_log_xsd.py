from lxml import etree

personal_data = [
    ("CustomerRepresentative", "Person", "代表"),
    ("QualityAssurance", "Person", "检验"),
    ("SystemOperator", "Person", "测试人员"),
    ("Extension", "NonBlankString", "其他人员")
]


def generate_xsd_Personal(root, elements_with_comments):
    # 创建 xs:complexType 元素
    element = etree.SubElement(root, "{http://www.w3.org/2001/XMLSchema}element", name="Personnel", type="Personal")
    # 创建 xs:sequence 元素

    for name, type_name, comment in elements_with_comments:
        element = etree.SubElement(element, "{http://www.w3.org/2001/XMLSchema}element", name=name)
        if type_name:
            element.attrib["type"] = type_name

        if comment:
            annotation = etree.SubElement(element, "{http://www.w3.org/2001/XMLSchema}annotation")
            documentation = etree.SubElement(annotation, "{http://www.w3.org/2001/XMLSchema}documentation")
            documentation.text = comment
    return root


def generate_xsd_ResultSet(root,elements_with_comments):
    # 创建 xs:complexType 元素
    element = etree.SubElement(root, "{http://www.w3.org/2001/XMLSchema}element", name="Personnel", type="Personal")
    # 创建 xs:sequence 元素
    sequence = etree.SubElement(element, "{http://www.w3.org/2001/XMLSchema}sequence")
    # 创建子元素及其注释

    for name, type_name, comment in elements_with_comments:
        element = etree.SubElement(sequence, "{http://www.w3.org/2001/XMLSchema}element", name=name)
        if type_name:
            element.attrib["type"] = type_name

        if comment:
            annotation = etree.SubElement(element, "{http://www.w3.org/2001/XMLSchema}annotation")
            documentation = etree.SubElement(annotation, "{http://www.w3.org/2001/XMLSchema}documentation")
            documentation.text = comment
    return root

def generate_xsd_with_comments():
    # 创建根元素 xs:element
    root = etree.Element("{http://www.w3.org/2001/XMLSchema}element", name="TestResults")

    # 添加 xs:annotation 元素及其子元素
    annotation = etree.SubElement(root, "{http://www.w3.org/2001/XMLSchema}annotation")
    documentation = etree.SubElement(annotation, "{http://www.w3.org/2001/XMLSchema}documentation")
    documentation.text = "测试描述"

    complexType = etree.SubElement(root, "{http://www.w3.org/2001/XMLSchema}complexType")

    # 创建 xs:sequence 元素
    sequence = etree.SubElement(complexType, "{http://www.w3.org/2001/XMLSchema}sequence")

    generate_xsd_Personal(sequence, personal_data)

    generate_xsd_Personal(sequence, personal_data)

    # 将XML树写入字符串
    xsd_content = etree.tostring(root, pretty_print=True, xml_declaration=True, encoding="utf-8").decode('utf-8')

    return xsd_content


def main():
    return generate_xsd_with_comments()


if __name__ == '__main__':
    # 调用函数生成带有注释的XSD字符串
    xsd_content = main()

    # 打印或使用 xsd_content
    with open('log.xsd', 'w', encoding='utf-8') as f:
        f.write(xsd_content)
