#discordpy version of soundbored

#My Libs
from Bigbrother import * #Call the discord bot
import ctypes
#myappid = 'daytondaniels.soundbored.alpha.1'
#ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
#Core Libs
import sys
import os
import time
#PyQT
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
#CFG
from dotenv import load_dotenv
load_dotenv()
MusicPort=os.getenv('PORT1')
SoundPort=os.getenv('PORT2')
WeatherPort=os.getenv('PORT3')
ports=[os.getenv('PORT1'),os.getenv('PORT2'),os.getenv('PORT3')]
playImg='./resources/img/play.png'
loopImg='./resources/img/loop.png'
stopImg='./resources/img/stop.png'

def PlayMusic():
    item=musictree.selectedIndexes()
    CmdSEND(MusicPort,f'play + {musicmodel.filePath(item[-1])}'.encode())
def LoopMusic():
    if mLoop.isChecked():
        CmdSEND(int(MusicPort),b'loop + yes')
    elif mLoop.isChecked()==False:
        CmdSEND(int(MusicPort),b'loop + no')
def StopMusic():
        CmdSEND(int(MusicPort),b'stop')
def PlaySound():
    item=soundtree.selectedIndexes()
    CmdSEND(int(SoundPort),f'play + {soundmodel.filePath(item[-1])}'.encode())
def LoopSound():
    if sLoop.isChecked():
        CmdSEND(int(SoundPort),b'loop + yes')
    else:
        CmdSEND(int(SoundPort),b'loop + no')
def StopSound():
        CmdSEND(int(SoundPort),b'stop')

def PlayWeather():
    item=weathertree.selectedIndexes()
    CmdSEND(int(WeatherPort),f'play + {weathermodel.filePath(item[-1])}'.encode())
def LoopWeather():
    if wLoop.isChecked():
        CmdSEND(int(WeatherPort),b'loop + yes')
    else:
        CmdSEND(int(WeatherPort),b'loop + no')
def StopWeather():
        CmdSEND(int(WeatherPort),b'stop')


def GUI():
    def init():
        global app
        global window
        app = QApplication(sys.argv)
        window = QWidget()
        def initLayout():
            global mainSound
            global extraSound
            global mainMusic
            global extraMusic
            global extraWeather
            global mainWeather
            global mainLayout
            mainSound= QHBoxLayout()
            extraSound= QVBoxLayout()
            mainMusic= QHBoxLayout()
            extraMusic= QVBoxLayout()
            mainWeather= QHBoxLayout()
            extraWeather= QVBoxLayout()
            mainLayout= QHBoxLayout()
        initLayout()
    init()
    def treemodels():
        global soundmodel
        global musicmodel
        global weathermodel
        soundmodel = QFileSystemModel()
        soundmodel.setRootPath('')
        musicmodel = QFileSystemModel()
        musicmodel.setRootPath('')
        weathermodel = QFileSystemModel()
        weathermodel.setRootPath('')
    treemodels()
    def treeview():
        def init():
            global soundtree
            global musictree
            global weathertree
            soundtree = QTreeView()
            soundtree.setModel(soundmodel)
            soundtree.setRootIndex(soundmodel.index(f'{os.getcwd()}/src/Sounds'))
            soundtree.setIndentation(20)
            soundtree.setAnimated(False)
            soundtree.setIndentation(10)
            soundtree.setSortingEnabled(True)
            soundtree.setWindowTitle("Sounds")
            
          
            for i in range(1,soundmodel.columnCount()):
                soundtree.hideColumn(i)
            
            musictree = QTreeView()
            musictree.setModel(musicmodel)
            musictree.setRootIndex(musicmodel.index(f'{os.getcwd()}/src/Music'))
            for i in range(1,musicmodel.columnCount()):
                musictree.hideColumn(i)
            musictree.setIndentation(20)
            musictree.setAnimated(False)
            musictree.setIndentation(10)
            musictree.setSortingEnabled(True)
            musictree.setWindowTitle("Sounds")
            weathertree = QTreeView()
            weathertree.setModel(weathermodel)
            weathertree.setRootIndex(weathermodel.index(f'{os.getcwd()}/src/Weather'))  
            for i in range(1,weathermodel.columnCount()):
                weathertree.hideColumn(i)
            weathertree.setIndentation(20)
            weathertree.setAnimated(False)
            weathertree.setIndentation(10)
            weathertree.setSortingEnabled(True)
            weathertree.setWindowTitle("Sounds")
            weathertree.alternatingRowColors()
            
        init()
        def show():
            def sound():
                s = mainSound.addWidget
                s(soundtree)
            sound()
            def music():
                m = mainMusic.addWidget
                m(musictree)
            def weather():
                m = mainWeather.addWidget
                m(weathertree)
            music()
            weather()
        show()
    treeview()
    def buttons():
            #SOUND
            global sPlay
            global sLoop
            global sStop
            es = extraSound.addWidget
            sPlay=QPushButton()
            sPlay.clicked.connect(PlaySound); sPlay.setStyleSheet(f"image : url({playImg});")
            sLoop=QPushButton(); sLoop.setStyleSheet(f"image : url({loopImg});")
            sLoop.setCheckable(True)
            sLoop.toggled.connect(LoopSound)
            sStop=QPushButton(); sStop.setStyleSheet(f"image : url({stopImg});")
            sStop.clicked.connect(StopSound)
            #EXTRA SOUND
            es(sPlay)
            es(sLoop)
            es(sStop)
            extraSound.addStretch()
            #MUSIC
            global mPlay
            global mLoop
            global mStop
            em = extraMusic.addWidget
            mPlay=QPushButton()
            mPlay.clicked.connect(PlayMusic); mPlay.setStyleSheet(f"image : url({playImg});")
            mLoop=QPushButton()
            mLoop.setCheckable(True)
            mLoop.toggled.connect(LoopMusic); mLoop.setStyleSheet(f"image : url({loopImg});")
            mStop=QPushButton(); mStop.setStyleSheet(f"image : url({stopImg});")
            mStop.clicked.connect(StopMusic)
            #EXTRA MUSIC
            em(mPlay)
            em(mLoop)
            em(mStop)
            extraMusic.addStretch()
            #MAIN WEATHER
            ew = extraWeather.addWidget
            global wPlay
            global wLoop
            global wStop
            wPlay=QPushButton(); wPlay.setStyleSheet(f"image : url({playImg});")
            wPlay.clicked.connect(PlayWeather)
            wLoop=QPushButton(); wLoop.setStyleSheet(f"image : url({loopImg});")
            wLoop.setCheckable(True)
            wLoop.toggled.connect(LoopWeather)
            wStop=QPushButton(); wStop.setStyleSheet(f"image : url({stopImg});")
            wStop.clicked.connect(StopWeather)
            #EXTRA WEATHER
            ew(wPlay)
            ew(wLoop)
            ew(wStop)
            extraWeather.addStretch()
    buttons()
    def finalinit():
        mainLayout.addLayout(mainMusic)
        mainLayout.addLayout(extraMusic)
        mainLayout.addLayout(mainSound)
        mainLayout.addLayout(extraSound)
        mainLayout.addLayout(mainWeather)
        mainLayout.addLayout(extraWeather)
        window.setLayout(mainLayout)
        window.setWindowTitle('SoundBored | Dayton Daniels')  
        window.setStyleSheet("""
        background-color: #484b6a;
        color:  #658c95;
        font-size: 18px;
        """)
        window.setWindowIcon(QIcon('logo.png'))
    finalinit()
    def fin():
        window.show()
        app.exec()
        if (sys.flags.interactive != 1):  
            for i in ports:
                 CmdSEND(int(i),b'death')
            quit()
    fin()
GUI()
