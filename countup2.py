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
def display_0():
	GPIO.output(14,0)
	GPIO.output(21,0)
	GPIO.output(19,0)
	GPIO.output(13,0)
	GPIO.output(8,0)
	GPIO.output(18,0)
	GPIO.output(25,1)
	time.sleep(1)
#1
def display_1():
	GPIO.output(14,1)
	GPIO.output(21,0)
	GPIO.output(19,0)
	GPIO.output(13,1)
	GPIO.output(8,1)
	GPIO.output(18,1)
	GPIO.output(25,1)
	time.sleep(1)
#2
def display_2():
	GPIO.output(14,0)
	GPIO.output(21,0)
	GPIO.output(19,1)
	GPIO.output(13,0)
	GPIO.output(8,0)
	GPIO.output(18,1)
	GPIO.output(25,0)
	time.sleep(1)
#3
def display_3():
	GPIO.output(14,0)
	GPIO.output(21,0)
	GPIO.output(19,0)
	GPIO.output(13,0)
	GPIO.output(8,1)
	GPIO.output(18,1)
	GPIO.output(25,0)
	time.sleep(1)
#4
def display_4():
	GPIO.output(14,1)
	GPIO.output(21,0)
	GPIO.output(19,0)
	GPIO.output(13,1)
	GPIO.output(8,1)
	GPIO.output(18,0)
	GPIO.output(25,0)
	time.sleep(1)
#5
def display_5():
	GPIO.output(14,0)
	GPIO.output(21,1)
	GPIO.output(19,0)
	GPIO.output(13,0)
	GPIO.output(8,1)
	GPIO.output(18,0)
	GPIO.output(25,0)
	time.sleep(1)
#6
def display_6():
	GPIO.output(14,0)
	GPIO.output(21,1)
	GPIO.output(19,0)
	GPIO.output(13,0)
	GPIO.output(8,0)
	GPIO.output(18,0)
	GPIO.output(25,0)
	time.sleep(1)
#7
def display_7():
	GPIO.output(14,0)
	GPIO.output(21,0)
	GPIO.output(19,0)
	GPIO.output(13,1)
	GPIO.output(8,1)
	GPIO.output(18,0)
	GPIO.output(25,1)
	time.sleep(1)
#8
def display_8():
	GPIO.output(14,0)
	GPIO.output(21,0)
	GPIO.output(19,0)
	GPIO.output(13,0)
	GPIO.output(8,0)
	GPIO.output(18,0)
	GPIO.output(25,0)
	time.sleep(1)
#9
def display_9():
	GPIO.output(14,0)
	GPIO.output(21,0)
	GPIO.output(19,0)
	GPIO.output(13,0)
	GPIO.output(8,1)
	GPIO.output(18,0)
	GPIO.output(25,0)
	time.sleep(1)

#do function 
display_0()
display_1()
display_2()
display_3()
display_4()
display_5()
display_6()
display_7()
display_8()
display_9()

#23(anode)off
GPIO.cleanup()
