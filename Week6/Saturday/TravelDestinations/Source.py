import json
import csv
import pickle
import pandas as pd

class Source:

    def __init__(self, file_type):
        self.file_type = file_type
        self.contents = self.read_file()

    def read_file(self):
        return contents

