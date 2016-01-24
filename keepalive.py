import datetime
import os
import time
import codecs
import sys

def log(message):
    logmessage = str(message)
    logmessage = logmessage.replace("'","")
    print(logmessage)
    logtime = time.strftime("%Y%m%d-%H%M%S")
    value = logtime + " " + str(logmessage)
    f = codecs.open('/home/pi/selcuk/log.txt','a')
    s = str(value)
    f.write(s)
    f.write('\n')
    f.close()

log("KeepAlive.py started")

try:

    file = open('/home/pi/selcuk/alive.txt', 'r')
    alive_string = file.readline()
    alive_string = alive_string.strip()
    last_alive = datetime.datetime.strptime(alive_string,'%Y%m%d-%H%M%S')
    current = datetime.datetime.now()
    last_alive_duration = abs((current - last_alive).seconds)

    if last_alive_duration > 90:
        log("selcuk.py trigging. Last Alive Duration : " + str(last_alive_duration))
        os.system("sudo python /home/pi/selcuk/selcuk.py")
    else:
        log("selcuk.py already alive. Duration:" + str(last_alive_duration) + " Time:" + str(last_alive))

except Exception, e:
    log("Error occurred " + str(e))
    log("selcuk.py trigging.")
    os.system("sudo python /home/pi/selcuk/selcuk.py")
