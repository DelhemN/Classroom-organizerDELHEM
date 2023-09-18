import random 
import pandas as pd 
import typing 
from utils.table import *


class Openspace:
    def __init__(self, tables=4, number_of_tables=6):
        self.tables = [Table() for _ in range(number_of_tables)]
        self.number_of_tables = number_of_tables

    def organize(self, names):
        random.shuffle(names)
        for name in names:
            for table in self.tables:
                if table.has_free_spot():
                    table.assign_seat(name)
                    break

    def display(self):
        for i, table in enumerate(self.tables):
            print(f"Table {i + 1}: {table}")

if __name__ == "__main__":
    names = ["Nicolas Del", "Nicolas Den", "Zian", "Alexandre", "Anthony"]
    openspace = Openspace()
    openspace.organize(names)
    openspace.display()
