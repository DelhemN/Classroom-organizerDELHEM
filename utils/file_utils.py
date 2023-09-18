import pandas as pd


def read_file(file_path):
    """
    Reads an Excel file from the given file path
    and returns a Pandas DataFrame.

    Args:
        file_path (str): The path to the Excel file

    Returns:
        df (DataFrame): The DataFrame read from the Excel file
    """
    df = pd.read_excel(file_path)
    return df
