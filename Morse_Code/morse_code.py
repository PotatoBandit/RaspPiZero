import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

ledPin = 12

GPIO.setup(ledPin, GPIO.OUT)

dot_length = .1
dash_length = .3
part = .1
next_letter = .2
space = .7

def dot():
	print("LED turning on")
	GPIO.output(ledPin, GPIO.HIGH)
	time.sleep(dot_length)
	print("LED turning off")
	GPIO.output(ledPin, GPIO.LOW)
	time.sleep(part)

def dash():
	print("LED turning on")
	GPIO.output(ledPin, GPIO.HIGH)
	time.sleep(dash_length)
	print("LED turning off")
	GPIO.output(ledPin, GPIO.LOW)
	time.sleep(part)

def next():
	print("LED turning off")
	GPIO.output(ledPin, GPIO.LOW)
	time.sleep(next_letter)

def space():
	print("Space")
	GPIO.output(ledPin, GPIO.LOW)
	time.sleep(space)

def a():
	dot()
	dash()
def b():
	dash()
	dot()
	dot()
	dot()
def c():
	dash()
	dot()
	dash()
	dot()
def d():
	dash()
	dot()
	dot()
def e():
	dot()
def f():
	dot()
	dot()
	dash()
	dot()

def g():
	dash()
	dash()
	dot()
def h():
	dot()
	dot()
	dot()
	dot()
def i():
	dot()
	dot()
def j():
	dot()
	dash()
	dash()
	dash()
def k():
	dash()
	dot()
	dash()
def l():
	dot()
	dash()
	dot()
	dot()
def m():
	dash()
	dash()
def n():
	dash()
	dot()
def o():
	dash()
	dash()
	dash()
def p():
	dot()
	dash()
	dash()
	dot()
def q():
	dash()
	dash()
	dot()
	dash()
def r():
	dot()
	dash()
	dot()
def s():
	dot()
	dot()
	dot()
def t():
	dash()
def u():
	dot()
	dot()
	dash()
def v():
	dot()
	dot()
	dot()
	dash()
def w():
	dot()
	dash()
	dash()
def x():
	dash()
	dot()
	dot()
	dash()
def y():
	dash()
	dot()
	dash()
	dash()
def z():
	dash()
	dash()
	dot()
	dot()

s()
next()
o()
next()
s()
next()
