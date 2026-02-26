import socket
import sys

print("Enter Domain name")

target_host = input()
target_port = "443"

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("The socket created")
except socket.error as err:
    print("socket creation failed %s" %(err))

try:
    host_ip = socket.gethostbyname(target_host) # It will Resolve the ip domain name to IP ADRR
except:
    print("Enter a correct domain Error")

try:
    s.connect((host_ip, int(target_port)))
    print("The socket Successfully connected to Destination")
except:
    print("The connection Failed Error")


print("The Destination Ip:",host_ip)




