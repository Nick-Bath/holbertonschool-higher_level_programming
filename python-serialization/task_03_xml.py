#!/usr/bin/python3

"""Module: Serialize and Deserialize XML"""


import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize python dictionary to XMl file"""
    elem = ET.Element("data")
    for key, val in dictionary.items():
        child = ET.Element(key)
        child.text = str(val)
        elem.append(child)

    tree = ET.ElementTree(elem)

    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """deserialize xml to python dictionary"""
    dictionary = {}

    tree = ET.parse("filename")
    root = tree.getroot()

    for child in root:
        dictionary[child.tag] = child.text

    return dictionary
