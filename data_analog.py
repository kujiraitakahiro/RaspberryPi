#!/usr/bin/python3
# -*- coding: utf-8 -*-

import spidev
import time

spi = spidev.SpiDev()
spi.open(0, 1)
spi.max_speed_hz = 1000000 #must spidev3.3

while True:
  try:
    resp = spi.xfer2([0x78, 0x00])
    value = (resp[0] * 256 + resp[1]) & 0x3ff
    volt = value * 3.3 / 1023
    print("Value: ",value," Volt: ",volt,"V")
    time.sleep(0.5)
  except KeyboardInterrupt:
    break

spi.close()
