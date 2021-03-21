from Client0 import Client
from pathlib import Path
PRACTICE = 2
EXERCISE = 1
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "127.0.0.1"
PORT = 8080
c = Client(IP, PORT)

print(c.talk(Path("P2/Sequences/U5.txt").read_text()))