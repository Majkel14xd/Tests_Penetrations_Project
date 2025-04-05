import sys, pickle

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("{0}: {1}".format(self.name, "Hau!"))

def save(file_name, dog):
    with open(file_name, "wb") as file:
        pickle.dump(dog, file)

if __name__ == "__main__":
    dog = Dog("Reks")
    dog.bark()
    if len(sys.argv) == 2:
        save(sys.argv[1], dog)
    
