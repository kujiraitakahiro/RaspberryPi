#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setup
GPIO.setmode(GPIO.BCM)
channels = [14, 18, 25 ,8, 13, 19, 21, 23]
GPIO.setup(channels,GPIO.OUT)
#23(anode)on
GPIO.output(23,1)
#0
GPIO.output(14,0)
GPIO.output(21,0)
GPIO.output(19,0)
GPIO.output(13,0)
GPIO.output(8,0)
GPIO.output(18,0)
GPIO.output(25,1)
time.sleep(1)
#1
GPIO.output(14,1)
GPIO.output(21,0)
GPIO.output(19,0)
GPIO.output(13,1)
GPIO.output(8,1)
GPIO.output(18,1)
GPIO.output(25,1)
time.sleep(1)
#2
GPIO.output(14,0)
GPIO.output(21,0)
GPIO.output(19,1)
GPIO.output(13,0)
GPIO.output(8,0)
GPIO.output(18,1)
GPIO.output(25,0)
time.sleep(1)
#3
GPIO.output(14,0)
GPIO.output(21,0)
GPIO.output(19,0)
GPIO.output(13,0)
GPIO.output(8,1)
GPIO.output(18,1)
GPIO.output(25,0)
time.sleep(1)
#4
GPIO.output(14,1)
GPIO.output(21,0)
GPIO.output(19,0)
GPIO.output(13,1)
GPIO.output(8,1)
GPIO.output(18,0)
GPIO.output(25,0)
time.sleep(1)
#5
GPIO.output(14,0)
GPIO.output(21,1)
GPIO.output(19,0)
GPIO.output(13,0)
GPIO.output(8,1)
GPIO.output(18,0)
GPIO.output(25,0)
time.sleep(1)
#6
GPIO.output(14,0)
GPIO.output(21,1)
GPIO.output(19,0)
GPIO.output(13,0)
GPIO.output(8,0)
GPIO.output(18,0)
GPIO.output(25,0)
time.sleep(1)
#7
GPIO.output(14,0)
GPIO.output(21,0)
GPIO.output(19,0)
GPIO.output(13,1)
GPIO.output(8,1)
GPIO.output(18,0)
GPIO.output(25,1)
time.sleep(1)
#8
GPIO.output(14,0)
GPIO.output(21,0)
GPIO.output(19,0)
GPIO.output(13,0)
GPIO.output(8,0)
GPIO.output(18,0)
GPIO.output(25,0)
time.sleep(1)
#9
GPIO.output(14,0)
GPIO.output(21,0)
GPIO.output(19,0)
GPIO.output(13,0)
GPIO.output(8,1)
GPIO.output(18,0)
GPIO.output(25,0)
time.sleep(1)
#23(anode)off
GPIO.cleanup()
