import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst = ip)
    broadcast = scapy.Ether(dst = "ff:ff:ff:ff:ff:ff") #hace referencia al campo de MAC
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout =1, verbose = False)[0]

    clients_list = []
    for element in answered_list:
        clients_dict = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        clients_list.append(clients_dict)
    return(clients_list)

def print_result (results_list):
    print("IP\t\t\tMAC addrress\n--------------------------------------")
    for client in results_list:
        print(client["ip"]+"\t\t"+client["mac"])

scan_result = scan("192.168.x.1 /24")
print_result(scan_result)


