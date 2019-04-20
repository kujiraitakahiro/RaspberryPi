#!/usr/bin/python3

import smbus

Bus = smbus.SMBus(1)
Addr = 0x23
LxRead2 = Bus.read_i2c_block_data(Addr,0x10)
print(str((LxRead2[0] * 256 + LxRead2[1]) / 1.2))
