import scapy
from scapy.all import *

ip_receiver = input('IP address: ')
msg = input('Message: ')
msg = list(msg)
msg = [ord(char) for char in msg]
msg = [IP(dst=ip_receiver, id=char) for char in msg]
for ip in msg:
    r = sr1(ip/ICMP())