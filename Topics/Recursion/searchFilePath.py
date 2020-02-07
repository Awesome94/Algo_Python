import os 
from os.path import isfile, join

def search(full_filepath, filename):
    print("checking: " +full_filepath)
    if filename in full_filepath:
        print("Found" +filename + "in" +full_filepath)
        return True
    if isfile(full_filepath):
        return False
    for file in os.listdir(full_filepath):
        if search(join(full_filepath, file), filename):
            break
    return "Done"

print(search("/users/awesome/python_tryouts", "knapsack.py"))
