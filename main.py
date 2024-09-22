from src.wifi import connect_to_wifi
from src.rest.server import start_server
from src.display import display
from time import sleep

display.show_text("ready")
sleep(2.5)
display.clear()

connect_to_wifi()
start_server()
