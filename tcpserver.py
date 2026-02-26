import socket
import threading

# Enter here your ilstening ip and port
bind_ip = "127.0.0.1"
bind_port = 9999


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))


server.listen(5)

print(f"[+] Listening on port {bind_ip} : {bind_port}")

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print(f"[+] Recieved: {request}")

    client_socket.send("Ping Recieved".encode())
    client_socket.close()

try:
    while True:
        client, addr = server.accept()
        print(f"[+] Accepted connection from:{addr[0]}:{addr[1]}")

        t = threading.Thread(target=handle_client, args=(client,))
        t.start()
except Exception as e:
    print("Try Again Error:{e}")


