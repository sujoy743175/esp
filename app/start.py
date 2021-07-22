from app.obstacleavoidance import avoid
from app.connect_and_update import connectToWifiAndUpdate
from app.blink import blink

def start():
    print('now its working..')
    connectToWifiAndUpdate()
    blink()
    #avoid()   


