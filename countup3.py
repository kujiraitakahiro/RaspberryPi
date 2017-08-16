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
	c00 = [14, 21, 19, 13, 8, 18]
	c01 = [25]
	GPIO.output(c00,0)
	GPIO.output(c01,1)
	time.sleep(1)

#1
def display_1():
	c10 = [21, 19]
	c11 = [14, 13, 8, 18, 25]
	GPIO.output(c10,0)
	GPIO.output(c11,1)
	time.sleep(1)

#2
def display_2():
	c20 = [14, 21, 13, 8, 25]
	c21 = [19, 18]
	GPIO.output(c20,0)
	GPIO.output(c21,1)
	time.sleep(1)

#3
def display_3():
	c30 = [14, 21, 19, 13, 25]
	c31 = [8, 18]
	GPIO.output(c30,0)
	GPIO.output(c31,1)
	time.sleep(1)

#4
def display_4():
	c40 = [21, 19, 18, 25]
	c41 = [14, 13, 8]
	GPIO.output(c40,0)
	GPIO.output(c41,1)
	time.sleep(1)
#5
def display_5():
	c50 = [14, 19, 13, 18, 25]
	c51 = [21, 8]
	GPIO.output(c50,0)
	GPIO.output(c51,1)
	time.sleep(1)
#6
def display_6():
	c60 = [14, 19, 13, 8, 18, 25]
	c61 = [21]
	GPIO.output(c60,0)
	GPIO.output(c61,1)
	time.sleep(1)
#7
def display_7():
	c70 = [14, 21, 19, 18]
	c71 = [13, 8, 25]
	GPIO.output(c70,0)
	GPIO.output(c71,1)
	time.sleep(1)
#8
def display_8():
	c80 = [14, 21, 19, 13, 8, 18, 25]
	c81 = []
	GPIO.output(c80,0)
	GPIO.output(c81,1)
	time.sleep(1)
#9
def display_9():
	c90 = [14, 21, 19, 13, 18, 25]
	c91 = [8]
	GPIO.output(c90,0)
	GPIO.output(c91,1)
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
