from gpiozero import PWMLED
from time import sleep

LedName = {}
LedName[1] = PWMLED(14)
LedName[1].on(10)
sleep(5)
