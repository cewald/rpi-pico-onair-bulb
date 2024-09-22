from src.wifi import connectToWifi
from src.rest.server import startServer
from src.display import init, showText, clear
from time import sleep

init()

showText("ready")
sleep(2.5)
clear()

connectToWifi()
startServer()
