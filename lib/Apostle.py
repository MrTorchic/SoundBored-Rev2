##Imports
import socket#$
import os
from dotenv import load_dotenv
load_dotenv()
#
#
##Vars
HOST=os.getenv('HOST')
from dotenv import load_dotenv
load_dotenv()
def CmdSEND(port,cmd): #(server)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST,int(port)))
            s.sendall(cmd)
        except:
            s.sendall(cmd)

def CmdRECIEVE(port):#(reciever)
    def main():
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind((HOST, int(port)))
                s.listen()
            except:
                s.connect((HOST, int(port)))
                s.listen()

            conn, addr = s.accept()
            with conn:
                while True:
                    global data
                    data = conn.recv(2048)
                    if not data:
                        pass
                    else:     
                        return conn.recv(2048)
                          
    try:
        main()
    except:
        quit()
    return data
def InitLoopVAR():
    Ports=[os.getenv('PORT1'),os.getenv('PORT2'),os.getenv('PORT3')]
    for i in Ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print('init')
            s.sendall(b'init')
    