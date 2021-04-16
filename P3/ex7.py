from Client0 import Client
IP = "172.17.0.1"
PORT = 8081
c = Client(IP, PORT)
l = ["U5", "ADA", "FXN", "PRAT1", "RNU6_269P"]
end = 0
while end == 0:
    a = input("")
    if a == "PING":
        print("Testing PING")
        print(c.talk("PING"))
    elif a == "GET":
        for n in range(0,4):
            print("Testing GET...")
            print("SEQ " + str(n))
            print(c.talk("GET " + str(n)))

    elif a == "INFO":
        print("Testing INFO...")
        print("Seq 0 Len = " + c.talk("INFO " + c.talk("GET " + str(0))))

    elif a == "COMP":
        print("Testing COMP...\n")
        print("SEQ 0 --> " + str(c.talk("GET " + str(0))) , "\n" + "COMP -->" + c.talk("COMP " + c.talk("GET " + str(0))))

    elif a == "REV":
        print("Testing REV...\n")
        print("SEQ 0 --> " + str(c.talk("GET " + str(0))), "\n" + "REV -->" + c.talk("REV " + c.talk("GET " + str(0))))

    elif a == "GENE":
        print("Testing GENE...\n")
        for n in range(0, len(l)):
            print ("GENE * " + l[n] +"\n" + str(c.talk("GENE " + l[n])))
    else:
        print ("The option u have selected is not available")
        end += 1

