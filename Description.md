# Overview of Application, 
This is an adaptation of my project 1 client server interaction but now using a VPN. The client takes in the port number and IP address as well as the message, and creates a string using "|" characters in between. It is then sent to the VPN which parses the message and sends the message to the server. The server then sends the desired response. 
My server does two things: offers advice or a bad celebrity look alike. If you want advice, type "general advice" or "romatic advice" as the message in the command line. If you want a look-alike, type "look-alike [hair color] [eyebrow status]", the options for hair color are red, blonde and brunette. The options for eyebrow status are "none" and "aggressive" 
# Client->VPN Server Message Format
If you want advice, type "general advice" or "romatic advice" as the message in the command line. If you want a look-alike, type "look-alike [hair color] [eyebrow status]", the options for hair color are red, blonde and brunette. The options for eyebrow status are "none" and "aggressive". The message should be sent to the VPN grouped as  "Message|ServerIP|ServerPort#" separated by the "|" character. The VPN should parse the message and send the message itsef to the server. 
# VPN Server->Client Message Format
Based on the message recieved, the server will reply with either randomly generated advice of the appropriate nature, or with a wisely chosen celebrity look alike. The server should send back the message to the VPN, which should have kept the connection with the client open, and then send the message to the client. 
# Example Output 
python3 client.py --message look-alike red none
client starting - connecting to VPN at IP 127.0.0.1 and port 55554
look-alike red none|127.0.0.1|65432
connection established, sending message 'look-alike red none|127.0.0.1|65432'
message sent, waiting for reply
Received response: 'You are Emma Stone' [18 bytes]
client is done!

python3 VPN.py
VPN starting - listening for connections at IP 127.0.0.1 and port 55554
Connected established with client ('127.0.0.1', 50566)
Received client message: 'b'look-alike red none|127.0.0.1|65432'' [35 bytes] from client
connection established with server , sending message 'look-alike red none'
message sent to server, waiting for reply
message recieved from server
sending ''You are Emma Stone'' to client
VPN is done!

python3 echo-server.py
server starting - listening for connections at IP 127.0.0.1 and port 65432
Connected established with ('127.0.0.1', 50567)
Received client message: ''look-alike red none'' [19 bytes]
echoing ''You are Emma Stone'' back to client
server is done!

# Network Layers Description 
The application layer gets the text input from the user. The data is then encapsulated by the transport and netowrk layer. The transport layer puts the port in the header. The network layer puts the IP adress on the header, and includes the port and IP adress of the final server destination. The link layer then sends the data to the VPN. The VPN link layer takes the data and gives it to the network layer, which takes the IP address of the server to put in the header, and gives the data to the link layer. The link layer sends the message to the Server. The server takes the package, reads that it is for the server, then the network layer confirms it is for the proper server ip adress. The transport layer then ensures the message was complete to the correct port, and the application then reads the message itself and formulates the response. it then sends it back, putting the VPN port and IP adress into the header and sending it to the IP adress. The VPN has kept the connection to the client open, so it forwards the message to the client. The client link layer then accepts the frame, sends it to the network layer, which passes it to the transport layer, and then finally to the application, which prints the reply to the user. 

# Acknowledgments.
I'd like to thank my mom. 