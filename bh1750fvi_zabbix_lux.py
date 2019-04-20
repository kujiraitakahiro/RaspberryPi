#!/usr/bin/python3

import smbus

Bus = smbus.SMBus(1)
Addr = 0x23
LxRead = Bus.read_i2c_block_data(Addr,0x11)
print(str(LxRead[1]* 10))
