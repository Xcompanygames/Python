import datetime
import socket
import sys
import time 
from random import *

host = raw_input("Please put in IP address or domain name: ")
timestart = datetime.datetime.today() #time the script started
t1 = str(timestart)
port = 0
group=0
print "Enter a scanning option"
select = str(input("\nWhich type of scan do you want: \n 1. Slow scan \n 2. Random scan \n 3. Smart scan"))
if "1" in select:
    while port <= 65536 : #max 65536
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      print "....................."
      with open('results.csv', 'a') as f:
        f.write(t1)
        try:
          if group>9:
        	    time.sleep(1)
        	    group=0
        	    print "sleep"
          if group<10:
  				     	s.settimeout(.105) #time
  				     	group += 1
  				     	s.connect((host,port))
  				     	value = ", %s,%s,OPEN\n" % (host, port)
	  			    	v = str(value)
	  			     	f.write(v)
	  			     	s.shutdown(2)
	  			    	s.close()
	  			     	print "port found"
	  			    	print '\a' # beeps on open port
	  			    	port += 1 
	  			    	print port
	  			     	continue
        except:
            
            if group>9:
              time.sleep(1)
              group=0
            if group<10:
              group += 1
              value =  ", %s,%s,CLOSED\n" % (host, port)
              v = str(value)
              f.write(v)
              port += 1 
              print port
              print "..CLOSED"
	f.closed
if "2" in select:
    while port <= 65536 : #max 65536
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      print "....................."
      with open('results.csv', 'a') as f:
        f.write(t1)
        try:
			portrand = randint(1, 65536)
  			s.settimeout(.105) #time
  			s.connect((host,port))
  			value = ", %s,%s,OPEN\n" % (host, portrand)
	  		v = str(value)
	  		f.write(v)
	  		s.shutdown(2)
	  		s.close()
	  		print "port found"
	  		print '\a' # beeps on open port
	  		port += 1 
	  		print portrand
	  		continue
        except:
            value =  ", %s,%s,CLOSED\n" % (host, port)
            v = str(value)
            f.write(v)
            port += 1 
            print portrand
            print "..CLOSED"
	f.closed
#List of common ports 
#    "21": "FTP",
#    "22": "SSH",
#    "23": "Telnet",
#    "25": "SMTP",
#    "53": "DNS",
#    "67":"DHCP",
#    "68":"DHCP",
#    "69":"TFTP",
#    "80": "HTTP",
#    "110":"POPv3",
#    "123":"NTP",
#    "143":"IMAP",
#    "194": "IRC",
#    "389":"LDAP",
#    "443": "HTTPS",
#    "3306": "MySQL",
#    "25565": "Minecraft"
if "3" in select:
    for x in [21,22,23,25,53,67,68,69,80,110,123,143,194,389,443,3306,25565]:
      s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      print "....................."
      with open('results.csv', 'a') as f:
        f.write(t1)
        try:
  			s.settimeout(.105) #time
  			s.connect((host,port))
  			value = ", %s,%s,OPEN\n" % (host, x)
	  		v = str(value)
	  		f.write(v)
	  		s.shutdown(2)
	  		s.close()
	  		print "port found"
	  		print '\a' # beeps on open port
	  		print x
	  		continue
        except:
            value =  ", %s,%s,CLOSED\n" % (host, port)
            v = str(value)
            f.write(v)
            print x
            print "..CLOSED"
	f.closed
