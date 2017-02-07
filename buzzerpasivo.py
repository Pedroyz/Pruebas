#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

BZRPin = 12
PinLed = 11

def setup():
	GPIO.setmode(GPIO.BOARD)       # Numbers pins by physical location
	GPIO.setup(BZRPin, GPIO.OUT)   # Set pin mode as output
	GPIO.output(BZRPin, GPIO.LOW)
	GPIO.setup(PinLed, GPIO.OUT)
	GPIO.output(PinLed, GPIO.HIGH)

def creciente():
	print 'creciente'
	for f in range(100, 2000, 100):
		p.ChangeFrequency(f)
		time.sleep(0.2)

def decreciente():
	print 'decreciente'
	for f in range(2000, 100, -100):
		p.ChangeFrequency(f)
		time.sleep(0.2)

def clear():
	GPIO.output(PinLed, GPIO.LOW)
	p.stop()
	GPIO.cleanup()

def loop():
	while True:
		GPIO.output(PinLed, GPIO.HIGH)
		creciente()
		GPIO.output(PinLed, GPIO.LOW)
		decreciente()


if __name__ == '__main__': 
	setup()
	p = GPIO.PWM(BZRPin, 50) # init frequency: 50HZ
	p.start(50)  # Duty cycle: 50%
	try:
		loop()
	except KeyboardInterrupt:
		clear()

