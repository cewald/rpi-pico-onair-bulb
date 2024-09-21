from src.wifi import connectToWifi
from src.rest.server import startServer
from src.display import showText, clear
from time import sleep

showText("ready")
sleep(1)
clear()

connectToWifi()
startServer()
