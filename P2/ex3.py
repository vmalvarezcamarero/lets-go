from Client0 import Client
from termcolor import colored
PRACTICE = 2
EXERCISE = 3
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "127.0.0.1"
PORT = 8080
c = Client(IP, PORT)
response = c.talk(colored("This is something random", "yellow", ))
print("Response: " + response)