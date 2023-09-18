import pandas as pd


def read_file(file_path):
    df = pd.read_excel(file_path)
    return df


read_file("utils/mates.xlsx")
