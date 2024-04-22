from multiprocessing import Process
import subprocess
from threading import Thread
import os
from lib.Apostle import *
Bots = ['./lib/Bot-OMEGA.py','./lib/Bot-LAMBDA.py','./lib/Bot-PSI.py']
Main = ['./main.py']
Dirs = Bots + Main
def init():
    global InitBots
    def thread(b):
        global t
        def proc(c):
            x = subprocess.run(c,shell=True)
        t = Process(target=proc(b))
        t.start()
    for i in Dirs:
        InitBots=Thread(target=thread,args=(f'python3 {i}',))
        InitBots.start()
init()

