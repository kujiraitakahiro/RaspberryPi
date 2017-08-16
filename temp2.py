#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setup
GPIO.setmode(GPIO.BCM)
channels = [14, 18, 25 ,8, 13, 19, 21, 23]
dots = [2, 3]
GPIO.setup(channels,GPIO.OUT)
GPIO.setup(dots,GPIO.OUT)

#23(anode)on
GPIO.output(channels,1)
GPIO.output(dots,1)

#file operation
file = open('/sys/devices/w1_bus_master1/28-0000068d4e4e/driver/28-0000068d4e4e/w1_slave', 'r')
#file = open('testtemp.txt', 'r')
string = file.read()
file.close()
slice = string[69:]
temp1 = slice.rstrip()
temp2 = temp1.rjust(5,"0")
#print temp2 
print (temp2[0]+temp2[1]+"."+temp2[2]+temp2[3])

#0
def display_0():
	c00 = [14, 21, 19, 13, 8, 18]
	c01 = [25, 3]
	GPIO.output(c00,0)
	GPIO.output(c01,1)
	time.sleep(1)

#1
def display_1():
	c10 = [21, 19]
	c11 = [14, 13, 8, 18, 25, 3]
	GPIO.output(c10,0)
	GPIO.output(c11,1)
	time.sleep(1)

#2
def display_2():
	c20 = [14, 21, 13, 8, 25]
	c21 = [19, 18, 3]
	GPIO.output(c20,0)
	GPIO.output(c21,1)
	time.sleep(1)

#3
def display_3():
	c30 = [14, 21, 19, 13, 25]
	c31 = [8, 18, 3]
	GPIO.output(c30,0)
	GPIO.output(c31,1)
	time.sleep(1)

#4
def display_4():
	c40 = [21, 19, 18, 25]
	c41 = [14, 13, 8, 3]
	GPIO.output(c40,0)
	GPIO.output(c41,1)
	time.sleep(1)
#5
def display_5():
	c50 = [14, 19, 13, 18, 25]
	c51 = [21, 8, 3]
	GPIO.output(c50,0)
	GPIO.output(c51,1)
	time.sleep(1)
#6
def display_6():
	c60 = [14, 19, 13, 8, 18, 25]
	c61 = [21, 3]
	GPIO.output(c60,0)
	GPIO.output(c61,1)
	time.sleep(1)
#7
def display_7():
	c70 = [14, 21, 19, 18]
	c71 = [13, 8, 25, 3]
	GPIO.output(c70,0)
	GPIO.output(c71,1)
	time.sleep(1)
#8
def display_8():
	c80 = [14, 21, 19, 13, 8, 18, 25]
	c81 = [3]
	GPIO.output(c80,0)
	GPIO.output(c81,1)
	time.sleep(1)
#9
def display_9():
	c90 = [14, 21, 19, 13, 18, 25]
	c91 = [8, 3]
	GPIO.output(c90,0)
	GPIO.output(c91,1)
	time.sleep(1)

#0dot
def display_0d():
	c00 = [14, 21, 19, 13, 8, 18, 3]
	c01 = [25]
	GPIO.output(c00,0)
	GPIO.output(c01,1)
	time.sleep(1)

#1dot
def display_1d():
	c10 = [21, 19, 3]
	c11 = [14, 13, 8, 18, 25]
	GPIO.output(c10,0)
	GPIO.output(c11,1)
	time.sleep(1)

#2dot
def display_2d():
	c20 = [14, 21, 13, 8, 25, 3]
	c21 = [19, 18]
	GPIO.output(c20,0)
	GPIO.output(c21,1)
	time.sleep(1)

#3dot
def display_3d():
	c30 = [14, 21, 19, 13, 25, 3]
	c31 = [8, 18]
	GPIO.output(c30,0)
	GPIO.output(c31,1)
	time.sleep(1)

#4dot
def display_4d():
	c40 = [21, 19, 18, 25, 3]
	c41 = [14, 13, 8]
	GPIO.output(c40,0)
	GPIO.output(c41,1)
	time.sleep(1)
#5dot
def display_5d():
	c50 = [14, 19, 13, 18, 25, 3]
	c51 = [21, 8]
	GPIO.output(c50,0)
	GPIO.output(c51,1)
	time.sleep(1)
#6dot
def display_6d():
	c60 = [14, 19, 13, 8, 18, 25, 3]
	c61 = [21]
	GPIO.output(c60,0)
	GPIO.output(c61,1)
	time.sleep(1)
#7dot
def display_7d():
	c70 = [14, 21, 19, 18, 3]
	c71 = [13, 8, 25]
	GPIO.output(c70,0)
	GPIO.output(c71,1)
	time.sleep(1)
#8dot
def display_8d():
	c80 = [14, 21, 19, 13, 8, 18, 25, 3]
	c81 = []
	GPIO.output(c80,0)
	GPIO.output(c81,1)
	time.sleep(1)
#9dot
def display_9d():
	c90 = [14, 21, 19, 13, 18, 25, 3]
	c91 = [8]
	GPIO.output(c90,0)
	GPIO.output(c91,1)
	time.sleep(1)

#do function 
if temp2[0] == "0":
	display_0()
elif temp2[0] == "1":
	display_1()
#do function 
if temp2[0] == "0":
	display_0()
elif temp2[0] == "1":
	display_1()
elif temp2[0] == "2":
	display_2()
elif temp2[0] == "3":
	display_3()
elif temp2[0] == "4":
	display_4()
elif temp2[0] == "5":
	display_5()
elif temp2[0] == "6":
	display_6()
elif temp2[0] == "7":
	display_7()
elif temp2[0] == "8":
	display_8()
elif temp2[0] == "9":
	display_9()
else:
	print("program finish!")
time.sleep(1)

if temp2[1] == "0":
	display_0d()
elif temp2[1] == "1":
	display_1d()
elif temp2[1] == "2":
	display_2d()
elif temp2[1] == "3":
	display_3d()
elif temp2[1] == "4":
	display_4d()
elif temp2[1] == "5":
	display_5d()
elif temp2[1] == "6":
	display_6d()
elif temp2[1] == "7":
	display_7d()
elif temp2[1] == "8":
	display_8d()
elif temp2[1] == "9":
	display_9d()
else:
	print("program finish!")
time.sleep(1)


if temp2[2] == "0":
	display_0()
elif temp2[2] == "1":
	display_1()
elif temp2[2] == "2":
	display_2()
elif temp2[2] == "3":
	display_3()
elif temp2[2] == "4":
	display_4()
elif temp2[2] == "5":
	display_5()
elif temp2[2] == "6":
	display_6()
elif temp2[2] == "7":
	display_7()
elif temp2[2] == "8":
	display_8()
elif temp2[2] == "9":
	display_9()
else:
	print("program finish!")
time.sleep(1)

if temp2[3] == "0":
	display_0()
elif temp2[3] == "1":
	display_1()
elif temp2[3] == "2":
	display_2()
elif temp2[3] == "3":
	display_3()
elif temp2[3] == "4":
	display_4()
elif temp2[3] == "5":
	display_5()
elif temp2[3] == "6":
	display_6()
elif temp2[3] == "7":
	display_7()
elif temp2[3] == "8":
	display_8()
elif temp2[3] == "9":
	display_9()
else:
	print("program finish!")
time.sleep(1)

#23(anode)off
GPIO.cleanup()
