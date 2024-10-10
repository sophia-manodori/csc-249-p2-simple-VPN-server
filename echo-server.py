#!/usr/bin/env python3
import random
import socket
import arguments
import argparse

#advice prompts from mama
radvice = ["don't share a man, let several men share you", "the fancier the car, the smaller the penis", "stop talking about women that way", "*sigh* if I were to divorce my wife, I would date several younger men all at the same time. You aren't married! You still can... if you want...", "marriage is like icing on the cake of life. but, cake is better without icing sometimes."]
gadvice = ["go outside. It's weird to be inside this much. not normal *italian hand movements*", "you should talk to your therapist about that", "I'd say that mole looks normal, actually. Don't worry about it.", "it's okay to speed on the freeway. Just don't get a ticket.", "don't listen to people with borderline personality disorder"]
random.seed(version=2)
#list of celebrity look alikes
unhinged = ["Emilia Clark", "Dwayne 'The Rock' Johnson", "Emma Stone", "Merida (the princess from Brave)", "Ross Lynch", "Troye Sivan"]


# Run 'python3 echo-server.py --help' to see what these lines do
parser = argparse.ArgumentParser('Starts a server that returns the data sent to it unmodified')
parser.add_argument('--server_IP', help='IP address at which to host the server', **arguments.ip_addr_arg)
parser.add_argument('--server_port', help='Port number at which to host the server', **arguments.server_port_arg)
args = parser.parse_args()

SERVER_IP = args.server_IP  # Address to listen on
SERVER_PORT = args.server_port  # Port to listen on (non-privileged ports are > 1023)

#randomly generates romantic advice
def romanticanswer(message):
    if(message == "romantic advice"):
        num = random.randint(0, 4)
        answer = radvice[num]
    elif(message == "general advice"):
        num = random.randint(0, 4)
        answer = gadvice[num]
    return answer

#randomly generates celebrity lookalike based on message
def celeb(message):
    if(message[1]=="red"):
        if(message[2]=="none"):
            data = "You are Emma Stone"
        elif (message[2]=="intense"):
            data = "You are Merida (the princess from Brave)"
        else:
            data = "whoops. There's an error."
    elif(message[1]=="blonde"):
        if(message[2]=="none"):
            data = "You are Troye Sivan"
            print(data)
        elif (message[2]=="intense"):
            data = "You are Ross Lynch"
        else:
            data = "whoopsie. There was an error"
    elif(message[1]=="brunette"):
        if(message[2]=="none"):
            data = "Pitbull"
        elif (message[2]=="intense"):
            data = "The Rock"
        else: 
            data = "whopsie. there was an error"
    return data

#run server
print("server starting - listening for connections at IP", SERVER_IP, "and port", SERVER_PORT)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((SERVER_IP, SERVER_PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected established with {addr}")
        while True:
            data = conn.recv(1024)
            data = data.decode("utf-8")
            if not data:
                break
            print(f"Received client message: '{data!r}' [{len(data)} bytes]")
            words = data.split(" ")
            #send advice
            if(words[1]=="advice"): 
                print("generating advice...")
                reply = romanticanswer(data)
            #send look alike
            elif (words[0]== "look-alike"):
                print("generating celebrit look alike...")
                reply = celeb(words)
            print(f"sending '{reply!r}' back to client")
            conn.sendall(reply.encode("utf-8"))

print("server is done!")
