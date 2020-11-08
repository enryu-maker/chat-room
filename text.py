#!usr/bin/python3
import socket, time
from termcolor import colored
print(colored("""
    
    ,,,,,,,, ,,    ,,     ,,     ,,,,,,,,
    ||'''''' ||    ||    ''''    ,,,,,,,,
    ||       ||====||   ''==''      ||
    ||,,,,,, ||    ||  ''    ''     || 
    '''''''' ''    '' ''      ''    ''
                       ,,,,,,,, ,,,,,,,, ,,,,,,,, ,,,    ,,,
                       ||,,,,|| ||''''|| ||''''|| ||''  ''||
                       || '' '' ||    || ||    || || '''' ||
                       ||  ''   ||,,,,|| ||,,,,|| ||  ''  ||
                       ''   ''  '''''''' '''''''' ''      ''
                                                            [+]CLIENT SIDE[+]

                    ""","cyan"))
print("============================================================================")
print(colored("[+]Author-->Enryu","red"))
print(colored("[+]Git-hub-->enryu-maker","red"))
print("============================================================================")
def out(a):
    print(colored(a,"blue"))
def inp(b):
    return (input(colored(b,"red")))
out("connecting a server")
s=socket.socket()
host=inp("Enter the ip of host-->")
prt=int(input(colored("Enter the port number-->","red")))
s.connect((host,prt))
name=inp("Enter the username-->")
out("waiting for connection!!!!!")
time.sleep(1)
s.send(name.encode())
out("[+]press bye or exit")
name2=s.recv(1024)
name2=name2.decode()
print(colored("typing....","yellow"))
while True:
    msg1=s.recv(1024)
    msg1=msg1.decode()
    time.sleep(1)
    print(colored(name2,"yellow"),colored(">>","yellow"),msg1)
    msg=inp("me >>")
    if msg=="bye" or msg=="exit":
        msg=msg.encode()
        s.send(msg)
        out("\n Diconnecting from server!!!")
        s.close()
        break
    else:
        msg=msg.encode()
        s.send(msg)
       