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

def wheel(pos):
    """Generate rainbow colors across 0-255 positions."""
    if pos < 85:
        return Color(pos * 3, 255 - pos * 3, 0)
    elif pos < 170:
        pos -= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def turnOff(strip):
    colorWipe(strip, Color(0,0,0))

# set up comminications with ground control

ground_control = groundcontrol.GroundControl("826dev")

# set up light strip

light_strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
light_strip.begin()

# set up the button sensor

sensor = sensorcontrol.Sensor(16)
sensor.pir_setup()

# start the loop

previous_sensor_state = GPIO.input(sensor.pin)

while True:
    current_sensor_state = GPIO.input(sensor.pin)
    sensor.check_for_motion(previous_sensor_state, current_sensor_state)
    if sensor.is_triggered:
        print "in triggered block"
        if ground_control.light_permission():
            light_pattern = ground_control.light_directive()
            execfile("pattern-lib/"+light_pattern+".py")
            start_time = time.time()
            time_elapsed = 0
            while time_elapsed < 20:
                display_pattern(light_strip)
                time_elapsed = time.time() - start_time
        sensor.untrigger()
        turnOff(light_strip)
    previous_sensor_state = current_sensor_state
