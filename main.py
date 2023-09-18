from utils.file_utils import read_file
from utils.table import Table
from utils.openspace import Openspace


if __name__ == "__main__":
    names = ["Nicolas DEL", "Zian", "Alexandre", "Nicolas DEN", "Anthony"]
    openspace = Openspace()
    openspace.organize(names)
    openspace.display()
