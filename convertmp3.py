import glob
import os
import time

logtime = time.strftime("%Y%m%d-%H%M%S")
logmessage = "convertmp3.py started."
command = "sed -i '1s/^/" + logtime + " " + logmessage + "\\n/' /home/pi/selcuk/log.txt"
os.system(command)

os.chdir("/home/pi/selcuk/wav/")
for file in glob.glob("*.wav"):
	filename = file.rsplit('.', 1)[0]
	convert_command = "lame /home/pi/selcuk/wav/" + file + " /home/pi/selcuk/wav/" + filename + ".mp3"
	move_command = "mv /home/pi/selcuk/wav/" + filename + ".mp3 /home/pi/selcuk/mp3/"
	delete_command = "rm /home/pi/selcuk/wav/" + file
	os.system(convert_command)
	os.system(move_command)
	os.system(delete_command)
	logtime = time.strftime("%Y%m%d-%H%M%S")
	logmessage = file + " converted to mp3 and moved to /mp3 folder"
	command = "sed -i '1s/^/" + logtime + " " + logmessage + "\\n/' /home/pi/selcuk/log.txt"
	os.system(command)
