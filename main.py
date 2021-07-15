from machine import Pin, PWM

import time

from app.obstacleavoidance import avoid
from app.connect_and_update import connectToWifiAndUpdate

connectToWifiAndUpdate()
import app.start
#avoid()
