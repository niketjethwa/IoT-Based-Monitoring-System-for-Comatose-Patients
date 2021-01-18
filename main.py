import time
import RPi.GPIO as GPIO
import sys
import urllib2
import httplib
import urllib
import ultrasonic
import PIR

key = "LBCJLIBK42JKSIS5"
baseURL = 'https://api.thingspeak.com/update?api_key=%s' % key

def main():
    print 'starting...'
    while True:
        try:
	    distance = ultrasonic.check_distance()
	    motion = PIR.detect_motion()
	    print "Distance: ",distance
 	    print "Motion: ",motion
            f = urllib2.urlopen(baseURL + "&field1=%s&field2=%s" % (distance,motion))
	    print "OUTPUT: ",f.read()
  	    f.close()
            time.sleep(15)
	    print "\n"
        except:
            print 'exiting.'


# call main
if __name__ == '__main__':
    while True:
       main()
