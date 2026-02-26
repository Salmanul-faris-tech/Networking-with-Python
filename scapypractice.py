import scapy.all as scapy

print("Enter you ip with cidr notation")
target = input()

request = scapy.ARP() # Creating ARP Packet

print(scapy.ls(scapy.ARP())) # Listing All Fields of an ARP packet

request.pdst = target

broadcast = scapy.Ether()

broadcast.dst = 'ff:ff:ff:ff:ff:ff'

request_broadcast = broadcast / request

clients = scapy.srp(request_broadcast, timeout = 1)[0] # Sending ARP Request to broadcast

for element in clients:
    print(element[1].psrc + "      " + element[1].hwsrc)


