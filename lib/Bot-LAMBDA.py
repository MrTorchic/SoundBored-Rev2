from Apostle import *
import threading
import subprocess
import discord
import os
from dotenv import load_dotenv
load_dotenv()
Discord_Token = os.getenv('TOKEN3')
Port = os.getenv('PORT3')
intents = discord.Intents.default()
intents.message_content = True
global loopInt
loopInt=None
def Listen():
    while True:
        x = CmdRECIEVE(Port).decode()
        if 'play' in x:
            x=x.split(' + ')[-1]
            play(x)
        elif 'loop' in x:
            global loopInt
            if 'yes' in x:
                loopInt=1
            else:
                loopInt=0    
        elif 'stop' in x:
            stop()
        elif 'death' in x:
            print('slayed')
            break

        
#START LISTENING
initSocket=threading.Thread(target=Listen)
initSocket.start()
#START BOT PAST HERE
def initbot(Discord_Token):
    client = discord.Client(intents=intents)
    id=int(os.getenv('ownerid'))
    @client.event
    async def on_ready():        
        global play;global loop;global stop
        def play(file):
            def repeat(file):
                if loopInt==1:
                    global loop
                    initplayer.play(discord.FFmpegPCMAudio(file), after=lambda e: repeat(file))
                    initplayer.is_playing()
            if loopInt==1:
                initplayer.pause()
                repeat(file)
            else:
                initplayer.pause()
                initplayer.play(discord.FFmpegPCMAudio(file))
        def stop():
            if not initplayer.is_playing:
                pass
            else:
                initplayer.pause()  
            
    @client.event
    async def on_voice_state_update(member, before, after):
        if not before.channel and after.channel and member.id == id:
            global initplayer
            vc = member.voice.channel
            initplayer = await vc.connect()            
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
    client.run(Discord_Token)
initbot(Discord_Token)


