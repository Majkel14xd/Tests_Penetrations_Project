import sys, json

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print("{0}: {1}".format(self.name, "Hau!"))

    @staticmethod
    def from_dict(data):
        if "name" not in data:
            raise ValueError("Nieprawidłowe dane!")
        return Dog(data["name"])

def restore_from_json(file_name):
    with open(file_name, "r") as file:
        data = json.load(file)
        return Dog.from_dict(data)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        dog = restore_from_json(sys.argv[1])
        dog.bark()