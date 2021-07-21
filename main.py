from machine import Pin, PWM

import time

from app.obstacleavoidance import avoid
from app.connect_and_update import connectToWifiAndUpdate
from app.start import start

connectToWifiAndUpdate()
start()
#avoid()

