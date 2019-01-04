import smtplib
import time
from time import sleep
from sense_hat import SenseHat
from datetime import datetime
import MobilText
sense=SenseHat()
t1=time.clock()
while True:
    t1=time.clock()
    print(t1)
    for event in sense.stick.get_events():
        
        if event.action=="held":
            
            print (event.action)
            print (event.direction)
            exit()
    if t1>300.0:
        MobilText.andre()
        MobilText.chiquilla()
        exit()
        

