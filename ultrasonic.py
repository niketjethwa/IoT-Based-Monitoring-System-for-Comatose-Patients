import RPi.GPIO as GPIO
import datetime
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

trigger = 21
echo = 16

GPIO.setup(trigger, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)
GPIO.setup(17, GPIO.OUT)

def check_distance():
    trigger = 21
    echo = 16
    start = 0
    end = 0
    
    GPIO.output(trigger, True)
    time.sleep(0.00001)
 
    GPIO.output(trigger, False)

    while GPIO.input(echo) == 0:
       start = time.time()

    while GPIO.input(echo) == 1:
       end = time.time()

    tof = end - start

    distance = (tof * 34300.0) / 2.0
    distance = round(distance, 2)

    #print "Total Distance: ",distance
    return distance


