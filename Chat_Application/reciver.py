
import socket
from datetime import datetime

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#ip_address = "192.168.35.177" 
ip_address = "127.0.0.1"
port_no = 2525

complete_address = (ip_address, port_no)
s.bind(complete_address)
print("hey I am listening")

while True:
    message, complete_address = s.recvfrom(100)
    message = message.decode()  # Decode the message to a string

    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    print(f"Message: {message} from {complete_address} at {current_time}")

    with open("data.txt", "a") as file:
        file.write(f"Message: {message}, IP: {complete_address[0]}, Port: {complete_address[1]}, Time: {current_time}\n")
