import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)

#sudo route -n
scan("192.168.x.x/24") #Ingresamos IP /24
