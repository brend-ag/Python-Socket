#!/usr/bin/env python

## Name: Brenda Gutierrez
## Resources: https://www.youtube.com/watch?v=3QiPPX-KeSc&ab_channel=TechWithTim

import socket
import sys

HEADER = 64
PORT = 5050

#Google DNS IP address has been put here as a placeholder
#Input your local machine's local IP address here before running
SERVER = "8.8.8.8" 
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
 
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(ADDR)

def send(msg):

    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))

    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

def msgs():
    #Continues to send messages to the client side until they write "done"
    #Client can go through messages by pressing enter
    msg1 = "Type done to stop sending."
    msg2 = "I am a program. My name is Mog, which you may recognize from a certain fantasy game."
    msg3 = "It's nice to meet you!"
    msg4 = "I hope you have..."
    msg5 = "a wonderful day!"
    msgList = [msg1, msg2, msg3, msg4, msg5]

    for i in msgList:
        #Using send ensures that the message is echoed on the server side
        msg_sent = send(i) 
        inp = input('')
        
        if inp == "done":
            send(DISCONNECT_MESSAGE)
            break


send("Hello!")
send("Please press enter on the client side to keep seeing mesages.")
     
msgs()

    


    