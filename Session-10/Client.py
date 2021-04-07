import Client0

c = Client0.Client("172.17.0.1", 8081)
for i in range(0,5):
    c.talk("Message "+ str(i))