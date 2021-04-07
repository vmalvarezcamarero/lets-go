import socket
import server_utiles

list_sequences = ["AAAAAAAAAATTGGCCT", "ACCACAAATGGGGGGTCA", "AAAAATGGGCCTG", "TTTTTTGGGGGTGGGG", "ATGC"]
PORT = 8081
IP = "172.17.0.1"

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print("The server is configured!")
n = 0
while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()
        n += 1

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listenning socket
        ls.close()

        # -- Exit!
        exit()

        # -- Execute this part if there are no errors
    else:

        print("CONNECTION " , str(n), "(", IP,",",str(PORT),")")

        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()
        formatted_message = server_utiles.format_command(msg)
        formatted_message = formatted_message.split(" ")

        if len(formatted_message) == 1:
            command = formatted_message[0]
        else:
            command = formatted_message[0]
            argument = formatted_message[1]
        if command == "PING":
            server_utiles.ping(cs)

        elif command == "GET":
            response = list_sequences[int(argument)] + "\n"
            cs.send(response.encode())

        else:

            response = "No available PING\n"

            print(f"Message received: {msg}")

            cs.send(response.encode())

        # -- Close the data socket
        cs.close()