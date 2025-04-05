import sys, pickle

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("{0}: {1}".format(self.name, "Hau!"))

def restore(file_name):
    with open(file_name, "rb") as file:
        return pickle.load(file)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        dog = restore(sys.argv[1])
        dog.bark()
