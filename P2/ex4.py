
from Client0 import Client
from termcolor import colored
PRACTICE = 2
EXERCISE = 4
print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")
IP = "127.0.0.1"
PORT = 8080
c = Client(IP, PORT)
print(c.debug_talk(colored("Message 1: First connection", "blue", )))
print(c.debug_talk(colored("Message 2: Testing !!!", "blue", )))
