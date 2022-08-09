#!/usr/bin/python3

import time
import socket
 
while True:
    host = socket.gethostname()
    date = time.strftime("%Y-%m-%d%H:%M:%S")
     
    now  = str(date)
    print("Open file and stated writing to it ...")
    with open('data.txt', 'a') as f:
        
        f.write(now + '\n')
        f.write(host + '\n')
         
    time.sleep(10)
    break