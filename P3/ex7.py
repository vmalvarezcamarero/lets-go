from Client0 import Client
IP = "172.17.0.1"
PORT = 8081
c = Client(IP, PORT)
print(c.talk(input("What functionality do you want to test? \n")))


