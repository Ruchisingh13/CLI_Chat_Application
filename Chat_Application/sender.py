# import socket
# client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# client.connect(("localhost",3306))
# done = False
# while not done:
#     client.send(input("Message:").encode('utf-8'))
#     try:
#         msg = client.recv(1024).decode('utf-8')
#     except UnicodeDecodeError as e:
#         print(f"UnicodeDecodeError: {e}")
#         if msg == "quit":
#             done = True
#         else:
#             print(msg)
                
# client.close()        



import socket  
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)    #UDP PROTOCAL

#target_ip = "192.168.1.64"  
target_ip = "127.0.0.1"
target_port = 2525
while True:
    message = input('enter message:')
    message = message.encode('ascii')
    s.sendto(message,(target_ip,target_port))
    print("your message has been successfully sent!")

