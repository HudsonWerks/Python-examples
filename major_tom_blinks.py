#!/usr/bin/python

# Blinks one of the Beaglebone Black's on-board LEDs until CTRL-C is pressed. These LEDs include USR0, USR1, USR2, USR3

# Import PyBBIO library
from bbio import *
#import the time module which allows us to set the timing for a loop event
import time

#Create variable called ledPin which refers to one of the designated onboard USR LEDs. You can change the number to any of the USR LEDs listed above.
ledPin = "USR3"

# Create a setup function
def setup():
    # Set one of the USR LEDs as output
    pinMode(ledPin, OUTPUT)

# Set up a loop and the blink timing to two second intervals
while True:
    # Start the pin state at LOW = off
    digitalWrite(ledPin, LOW)
    # Hold this state for 2 seconds
    time.sleep(2)
    # Change the pin state to HIGH = on
    digitalWrite(ledPin, HIGH)
    time.sleep(2)
