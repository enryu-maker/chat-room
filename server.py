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
                                                            [+]SERVER SIDE[+]

                    ""","cyan"))
print("============================================================================")
print(colored("[+]Author-->Enryu","red"))
print(colored("[+]Git-hub-->enryu-maker","red"))
print("============================================================================")
print(colored("Hosting a server","blue"))
s=socket.socket()
host=socket.gethostname()
host=socket.gethostbyname(host)
prt=1234
print(colored("server ip & port %s:%d"%(host,prt),"red"))
time.sleep(1)
s.bind((host,prt))
name=input(colored("Enter the username-->","red"))
s.listen(1)
print(colored("waiting for connection!!!!!","green"))
time.sleep(1)
conn,addr=s.accept()
print("received connection from",addr[0],":",addr[1])
conn.send(name.encode())
print(colored("[+]press BYE to exit","red"))
name2=conn.recv(1024)
name2=name2.decode()
while True:
    msg=input(colored("me >>","yellow"))
    if msg=="bye" or msg=="gn":
        msg=msg.encode()
        conn.send(msg)
        s.close()
        break
    else:
        msg=msg.encode()
        conn.send(msg)
        msg1=conn.recv(1024)
        msg1=msg1.decode()
        time.sleep(1)
        print(colored(name2,"red"),colored(">>","red"),msg1)
