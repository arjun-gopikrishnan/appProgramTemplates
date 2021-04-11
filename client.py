import socket             
s = socket.socket()         
  
port = 8080                
s.connect(('127.0.0.1', port)) 

server_response = s.recv(1024)
server_message = server_response.decode()
if server_message == 'ping' or server_message == 'Ping':
    print(server_message)
    message = 'pong'
else:
    print(server_message)
    message = 'response dropped'
print (message)

s.close()     