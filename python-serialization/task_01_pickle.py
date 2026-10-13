#!/bin/usr/python3
"""Module: Serialize using Pickle"""


import pickle


class CustomObject():
    """Custom class"""
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}\n"
              f"Age: {self.age}\n"
              f"Is Student: {self.is_student}")

    def serialize(self, filename):
        with open(filename, mode="wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        with open(filename, mode="rb") as f:
            return pickle.load(f)
