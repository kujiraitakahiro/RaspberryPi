#!/bin/bash
/bin/ping 192.168.77.77 -c 1 > /home/pi/ping_results 
grep "received" /home/pi/ping_results > /home/pi/ping_results2
Results=`cut -d " " -f 7 /home/pi/ping_results2`
Results2=errors,
if [ $Results = $Results2 ];
then
#echo $Results
#echo $Results2
#echo match
curl https://notify-api.line.me/api/notify -X POST -H "Authorization: Bearer XXXXXXXXXXYYYYYYYYYYZZZZZZZZZZ123" -F "message=Ping Fail!"
else
:
#echo No
fi
