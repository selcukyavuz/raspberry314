import os
import time

logtime = time.strftime("%Y%m%d-%H%M%S")
logmessage = "connect3g.py started"
command = "sed -i '1s/^/" + logtime + " " + logmessage + "\\n/' /home/pi/selcuk/log.txt"
os.system(command)

SIM_PIN = "0000" // SET YPUR SIM CARD PIN NUMBER
CUSTOM_APN = "Internet"
USBMODEM = "12d1:1003" // SET 3G MODEM USB NUMBER. YOU CAN GET THIS NUMBER WITH COMMAND lsusb
ip = '8.8.8.8'

if os.system("ping -c1 " + ip) == 0:
    print "OK"
else:
	command =   "sudo /home/pi/sakis3g connect --console --interactive --silent APN=CUSTOM_APN CUSTOM_APN='" + CUSTOM_APN + "' APN_USER='0' APN_PASS='0' USBINTERFACE=3 USBDRIVER=sierra USBMODEM=" + USBMODEM + " OTHER=USBMODEM MODEM=OTHER SIM_PIN='" + SIM_PIN + "'"
	os.system(command)
	logtime = time.strftime("%Y%m%d-%H%M%S")
	logmessage = "3g connected"
	command = "sed -i '1s/^/" + logtime + " " + logmessage + "\\n/' /home/pi/selcuk/log.txt"
	os.system(command)
