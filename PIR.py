import RPi.GPIO as GPIO
import datetime
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

sensor = 14
led = 18
GPIO.setup(sensor, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

#print "Initializing PIR Sensor......"
i = GPIO.input(sensor)
#print "Value Before: ",i

#print "PIR Ready..."

def detect_motion():
	while True:
		i = GPIO.input(sensor)
		print "Value of PIR: ",i
		if i==1:
			print "Motion Detected"
			GPIO.output(led, GPIO.HIGH)
			#time.sleep(5)
			GPIO.output(led, GPIO.LOW)
			#while GPIO.input(sensor):
				#print "Hello"
				#time.sleep(0.2)
		elif i==0:
			GPIO.output(led, GPIO.LOW)
			print "No Motion Detected"
		return i;



