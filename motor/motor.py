import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

GPIO.setup(40, GPIO.OUT)

p = GPIO.PWM(40,207)

p.start(0)

while True:
    for i in range(100):
        p.ChangeDutyCycle(i)
        time.sleep(0.02)
    for i in range(100):
        p.ChangeDutyCycle(100-i)
        time.sleep(0.02)

