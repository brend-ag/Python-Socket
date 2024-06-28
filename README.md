# Python-Socket
A Python 3 socket that allows for server-client connection on a local machine. It sends messages from the server side in response to user input on the client's side. Followed [this tutorial](https://www.youtube.com/watch?v=3QiPPX-KeSc&ab_channel=TechWithTim) as part of coursework for CSC 251: Network Security at Smith College. The socket was programmed using Visual Studio Code and run on a Windows 10 machine.

## Setup
1. Install [Python](https://www.python.org/downloads/).

2. To run the client.py file, you need to input the IPv4 IP address of your local machine. You can find this IP address by running:
-  `ipconfig` for the command prompt on a Windows machine and locating the IPv4 IP Address
- ` ipconfig getifaddr en0` if on Wi-Fi or `ipconfig getifaddr en1` if on Ethernet for the terminal on a Mac 

3. Enter this IP address in client.py at line 14 and replace the placeholder IP address.

## How to Use
1. Run the server.py file first in your IDE of choice. It should output in the IDE terminal that the server is listening and waiting for a connection.

2. While server.py file is running, open the command line and access the directory that contains the two files. 

3. Run client.py in the command line and follow the instructions to see the server's messages! Type "done" when you want to exit communication with the server. 
