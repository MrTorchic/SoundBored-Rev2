from multiprocessing import Process
import subprocess
from threading import Thread
from lib.Bigbrother import *
BotLocations = ['./lib/OMEGA.py','./lib/LAMBDA.py','./lib/PSI.py']
Main = ['./lib/Dashboard.py']
Dirs = BotLocations + Main
def init():
    global InitBots
    def thread(b):
        global t
        def proc(c):
            x = subprocess.run(c,shell=True)
        t = Process(target=proc(b))
        t.start()
    for i in Dirs:
        InitBots=Thread(target=thread,args=(f'py {i}',))
        InitBots.start()
init()

