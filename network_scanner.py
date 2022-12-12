import scapy.all as scapy

def scan(ip):
    scapy.arping(ip)

scan("192.x.x.x") #Ingresamos IP /24

