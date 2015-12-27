#!/usr/bin/python

import os
import serial
import re

ser = serial.Serial('/dev/ttyAMA0', 9600)
r_unwanted = re.compile("[\n\r]")

while True:
    try:
        msg = ser.readline()
        msg = r_unwanted.sub("", msg)
        print msg

    except KeyboardInterrupt:
        break
    except: # catch-all
        e = sys.exc_info()[0]
        print(e)

ser.close()