#!/usr/bin/python3

"""Module: CSV to JSON"""


import csv
import json


def convert_csv_to_json(filename):

    try:
        with open(filename, mode="r", newline='', encoding='utf-8') as f:
            data = list(csv.DictReader(f))

        with open("data.json", mode='w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
    except Exception:
        return False

    return True
