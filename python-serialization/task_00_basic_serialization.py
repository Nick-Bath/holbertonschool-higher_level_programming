#!/usr/bin/python3
"""Module: basic serialization"""


import json


def serialize_and_save_to_file(data, filename):
    with open(filename, mode="w") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    with open(filename, mode="r") as f:
        return json.load(f)
