import socket

print("Enter you Target Host address")
target_host = input()
target_port = "80"

# TCP Socket creation
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except:
    print("Failed to create Socket")

# Resolving HOST address to IP
try:
    target_ip = socket.gethostbyname(target_host)
except:
    print("Enter a correct Host address Error")

# Connecting to the target
try:
    client.connect((target_ip, int(target_port)))
except:
    print("Can't connect to without entering correct host address")

# Sending GET Request and Recieving the Response
try:
    client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n".encode())
    response = client.recv(4096)
    print(response.decode())
except:
    print("Can't send Request to a Incorrect Host Adress")



