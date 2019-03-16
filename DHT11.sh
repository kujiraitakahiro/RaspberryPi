#!/bin/bash
cat /sys/bus/iio/devices/iio\:device0/in_humidityrelative_input | sed -r s/000$/'%'/g
sleep 1
cat /sys/bus/iio/devices/iio\:device0/in_humidityrelative_input | sed -r s/000$/'%'/g
sleep 1
cat /sys/bus/iio/devices/iio\:device0/in_humidityrelative_input | sed -r s/000$/'%'/g
sleep 1
cat /sys/bus/iio/devices/iio\:device0/in_humidityrelative_input | sed -r s/000$/'%'/g
sleep 1
cat /sys/bus/iio/devices/iio\:device0/in_humidityrelative_input | sed -r s/000$/'%'/g
sleep 1
cat /sys/bus/iio/devices/iio\:device0/in_temp_input | sed s/000/'℃'/g
sleep 1
cat /sys/bus/iio/devices/iio\:device0/in_temp_input | sed s/000/'℃'/g
sleep 1
cat /sys/bus/iio/devices/iio\:device0/in_temp_input | sed s/000/'℃'/g
sleep 1
cat /sys/bus/iio/devices/iio\:device0/in_temp_input | sed s/000/'℃'/g
sleep 1
cat /sys/bus/iio/devices/iio\:device0/in_temp_input | sed s/000/'℃'/g
sleep 1
cat /sys/bus/iio/devices/iio\:device0/in_temp_input | sed s/000/'℃'/g
