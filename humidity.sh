#!/bin/bash
cat /sys/bus/iio/devices/iio\:device0/in_humidityrelative_input
sleep 1
cat /sys/bus/iio/devices/iio\:device0/in_humidityrelative_input
sleep 1
cat /sys/bus/iio/devices/iio\:device0/in_humidityrelative_input
sleep 1
value=`cat /sys/bus/iio/devices/iio\:device0/in_humidityrelative_input | sed -r "s/000$/ /g"`
if [ $value -gt 0 ];
then
 zabbix_sender -z 192.168.11.6 -s "RaspberryPizeroW" -k humidity -o $value
else
 echo "failed"
fi
