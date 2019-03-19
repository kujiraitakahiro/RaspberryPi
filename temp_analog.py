#!/usr/bin/python3
# -*- coding: utf-8 -*-

#Import wiringgpi for Control GPIOs, Import time for Using Sleep function.
import wiringpi as pi
import time

#Select SPI channel on MCP3002(ADconverter)
SPI_CH = 0
READ_CH = 0

pi.wiringPiSPISetup( SPI_CH, 1000000 )

#for LM61BIZ
while True:
	Buffer = 0x6800 | ( 0x1800 * READ_CH )
	Buffer = Buffer.to_bytes( 2, byteorder='big' )
	pi.wiringPiSPIDataRW( SPI_CH, Buffer )
	Value = ( Buffer[0] * 256 + Buffer[1] ) & 0x3ff
	Volt = ( Value * 3.3 / 1023 ) - 0.6 #offset 0.6V(600mV)
	Temp = Volt * 100
	print ("Temperature: ", Temp , "℃")
	time.sleep(1)
