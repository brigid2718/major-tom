# Main script for running the teleporter!

# modules to import
import requests
import RPi.GPIO as GPIO

import time
import sys
import pygame
sys.path.append('/home/pi/rpi_ws281x/python')
sys.path.append('/home/pi/ground-control/lib')

from lib import groundcontrol
from lib import sensorcontrol
from neopixel import *

# LED strip configuration:
LED_COUNT      = 30      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)

# useful functions for the strip patterns

def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

# set up comminications with ground control

ground_control = groundcontrol.GroundControl("826dev")

# set up light strip

light_strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
light_strip.begin()

# set up the button sensor

sensor = sensorcontrol.Sensor()
sensor.button_setup()

# start the loop

previous_sensor_state = GPIO.input(sensor.pin)

while True:
    current_sensor_state = GPIO.input(sensor.pin)
    sensor.check_for_trigger(previous_sensor_state, current_sensor_state)
    if sensor.is_triggered:
        print "in triggered block"
        if ground_control.light_permission():
            light_pattern = "mars" # ground_control.light_pattern_str
            execfile("pattern-lib/"+light_pattern+".py")
            display_pattern(light_strip)
        sensor.untrigger()
    previous_sensor_state = current_sensor_state
