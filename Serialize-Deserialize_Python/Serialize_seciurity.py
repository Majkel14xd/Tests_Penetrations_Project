import json

class Dog:
    def __init__(self, name):
        self.name = name

    def to_dict(self):
        return {"name": self.name}

def save_to_json(file_name, obj):
    with open(file_name, "w") as file:
        json.dump(obj.to_dict(), file)

if __name__ == "__main__":
    dog = Dog("Reksio")
    save_to_json("dog.json", dog)