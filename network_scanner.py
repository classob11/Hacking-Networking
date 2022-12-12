import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)

scan("192.x.x.1/24") #Ingresamos IP /24

