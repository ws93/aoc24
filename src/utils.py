from os import path 
def read_input(filename):
    print(path.dirname(__file__))
    filepath = path.relpath("data/" + filename, path.curdir)
    with open(filepath, "r") as file:
        return file.read().strip()