import socket, threading
from colorama import Fore, init; init()

# Choosing Nickname
print(f"{Fore.RED}Choose your nickname:{Fore.GREEN} ", end="")
nickname = input()
Fore.RESET

# Connecting To Server
data = input("Server info (host;port. Example: 127.0.0.1;8080): ")
host, port = data[:data.find(";")], int(data[data.find(";")+1:])

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

# Listening to Server and Sending Nickname
def receive():
    while True:
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('utf-8')
            if message == 'NICK':
                client.send(nickname)
            else:
                print(message)
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break

# Sending Messages To Server
def write():
    while True:
        x = input("Command: ")
        if x == "spam":
            for i in range(0, 200):
                client.send("©©©©©©©©©©©©©©©©©©©©©©©©©©© -- RAID BY SERVER_NUKE -- ©©©©©©©©©©©©©©©©©©©©©©©©©©©".encode('utf-8'))
        else:
            client.send(x.encode("utf-8"))

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
