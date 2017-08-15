#!/usr/bin/env python3
#cofing: utf-8
file = open('/sys/devices/w1_bus_master1/28-0000068d4e4e/driver/28-0000068d4e4e/w1_slave', 'r')
string = file.read()
file.close()
#print(string) 
print(string[69])
print(string[70])
print(string[71])
print(string[72])
