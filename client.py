#!/usr/bin/env python3

import socket
import arguments
import argparse

# Run 'python3 client.py --help' to see what these lines do
parser = argparse.ArgumentParser('Send a message to a server at the given address and print the response')
parser.add_argument('--server_IP', help='IP address at which the server is hosted', **arguments.ip_addr_arg)
parser.add_argument('--server_port', help='Port number at which the server is hosted', **arguments.server_port_arg)
parser.add_argument('--VPN_IP', help='IP address at which the VPN is hosted', **arguments.ip_addr_arg)
parser.add_argument('--VPN_port', help='Port number at which the VPN is hosted', **arguments.vpn_port_arg)
parser.add_argument('--message', default=['Hello, world'], nargs='+', help='The message to send to the server', metavar='MESSAGE')
args = parser.parse_args()

SERVER_IP = args.server_IP  # The server's IP address
SERVER_PORT = args.server_port  # The port used by the server
VPN_IP = args.VPN_IP  # The server's IP address
VPN_PORT = args.VPN_port  # The port used by the server
MSG = ' '.join(args.message) # The message to send to the server

#encodes message with dilinate values of "|"
def encode_message(message):
    # Add an application-layer header to the message that the VPN can use to forward it
    message = message + "|" + SERVER_IP + "|" + str(SERVER_PORT)
    return message

#starting client
if(MSG == "romatic advice" or MSG == "general advice" or MSG == "look-alike red none" or MSG == "look-alike red intense" or MSG == "look-alike blonde none" or MSG == "look-alike blonde intense" or MSG == "look-alike brunette none" or MSG == "look-alike brunette intense"):
    print("client starting - connecting to VPN at IP", VPN_IP, "and port", VPN_PORT)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((VPN_IP, VPN_PORT))
        tosend = encode_message(MSG)
        print(tosend)
        print(f"connection established, sending message '{tosend}'")
        s.sendall(bytes(tosend, 'utf-8'))
        print("message sent, waiting for reply")
        data = s.recv(1024).decode("utf-8")
    print(f"Received response: '{data}' [{len(data)} bytes]")
    print("client is done!")
else: 
    print("whoopsie there was a problem. Make sure your inputs are correct.")
