import scapy
from scapy.all import *

def print_id(pkt):
    print(chr(pkt.id))

ip_sender= input('IP address: ')
sniff(filter='ip and host ' + ip_sender, prn=print_id)