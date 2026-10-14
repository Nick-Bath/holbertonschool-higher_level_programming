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
    ET.indent(tree, space="    ")

    tree.write(filename, encoding="utf-8",)


def deserialize_from_xml(filename):
    """deserialize xml to python dictionary"""
    dictionary = {}

    tree = ET.parse(filename)
    root = tree.getroot()

    for child in root:
        dictionary[child.tag] = _convert(child.text)

    return dictionary

def _convert(text):
    """Convert XML text to int or float when possible"""
    for kind in (int, float):
        try:
            return kind(text)
        except (TypeError, ValueError):
            continue
    return text