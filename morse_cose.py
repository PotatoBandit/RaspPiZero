import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

ledPin = 12

GPIO.setup(ledPin, GPIO.OUT)

word = "SOS"

s = 3
o = 3
dot = .5 
dash = 1.5
next_letter = 1.5
next_word = 3.5
part = .5



for i in range(s):
	print("LED turning on")
	GPIO.output(ledPin, GPIO.HIGH)
	time.sleep(.25)
	print("LED turning off")
	GPIO.output(ledPin, GPIO.LOW)
	time.sleep(.25)

for i in range(o):
	print("LED turning on")
	GPIO.output(ledPin, GPIO.HIGH)
	time.sleep(.5)
	print("LED turning off")
	GPIO.output(ledPin, GPIO.LOW)
	time.sleep(.25)

for i in range(s):
	print("LED turning on")
	GPIO.output(ledPin, GPIO.HIGH)
	time.sleep(.25)
	print("LED turning off")
	GPIO.output(ledPin, GPIO.LOW)
	time.sleep(.25)
