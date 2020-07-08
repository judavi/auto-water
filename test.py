# Dry: (520 430]
# Wet: (430 350]
# Water: (350 260]
# External module imp
import RPi.GPIO as GPIO
import datetime
import time

init = False

# The format for how to read the pins
GPIO.setmode(GPIO.BOARD)

# Inputs/Outputs
GPIO.setup(7, GPIO.OUT) 
GPIO.setup(8, GPIO.IN) 

consecutive_water_count = 0

# A test cycle
while 1 and consecutive_water_count < 10:
  wet = GPIO.input(8)
  print(wet)
  GPIO.output(7, GPIO.HIGH)
  time.sleep(5)
  # GPIO.output(7, GPIO.LOW)
  consecutive_water_count += 1

GPIO.output(7, GPIO.LOW)
print(end)
