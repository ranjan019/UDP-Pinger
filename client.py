#from socket import *

import socket
from socket import AF_INET, SOCK_DGRAM
import time, datetime

print 'The client is running...'
print

serverip = '127.0.0.1' 
clientSocket = socket.socket(AF_INET,SOCK_DGRAM) 
clientSocket.settimeout(1) 

sequence_num_of_ping = 1 

while sequence_num_of_ping<=10:
    current_time= datetime.datetime.now().time().isoformat()
    message = 'Ping '+ str(sequence_num_of_ping) + ' ' +  str(current_time) 
    start_time=time.time() 
    clientSocket.sendto(message,(serverip, 12000))
    
    try:
        message, address = clientSocket.recvfrom(1024) 
        time_taken = ((time.time())-start_time) 
        print 
        print 'Ping number: '+ str(sequence_num_of_ping)
        print 'Message: ' + message
        print 'Round-Trip-Time (RTT) for the ping number '+ str(sequence_num_of_ping) + ' is: ' + str(time_taken) + ' seconds' 
    except socket.timeout:
        print
        print 'Ping number: '+ str(sequence_num_of_ping)
        print 'Request timed out'
    
    sequence_num_of_ping+=1 

if sequence_num_of_ping > 10: 
    clientSocket.close()


