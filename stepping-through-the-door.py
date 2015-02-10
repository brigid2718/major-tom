# Main script for running the teleporter!

# modules to import
import requests
import time

import sys
sys.path.append('/home/pi/rpi_ws281x/python')

from neopixel import *
from random import randint

# initiate light strip and load light strip functions
    # there should be a strip object that can display a pattern
# class LightStrip:
#     def __init__(self, input_list):
#         self.strip = Adafruit_NeoPixel(*input_list)
#
#     def display(self):
#         self.strip.setPixelColor(3,Color(0,255,0))
#         self.strip.show()
#         time.sleep(0.5)
#         self.strip.setPixelColor(3,Color(0,0,0))
#         self.strip.show()

# Here is the initialization of the light strip

# LED strip configuration:
LED_COUNT      = 30      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)


# light_strip = LightStrip(input_list)
# light_strip.strip.begin()

light_strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
light_strip.begin()

def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def teleport(strip):
    colorWipe(strip, Color(0,255,0))
    colorWipe(strip, Color(0,0,0))

# initiate sensor and load sensor reading functions
    # there should be a sensor object that has a is_triggered attribute
class Sensor:
    def __init__(self):
        self.is_triggered = False

    def trigger(self):
        self.is_triggered = True

    def untrigger(self):
        self.is_triggered = False

    def check_input(self):
        sensor_reading = randint(1,8001)
        if sensor_reading > 8000:
            print sensor_reading
            self.trigger()
        else:
            self.untrigger()


# Here is the setup of the sensor (dummy sensor right now)

sensor = Sensor()


# initiate sound control and load functions
    # there should be a sounds object that can play and pause
# initiate ground control communications
    # there should be a ground_control object that has attributes light_permission
    # and sound_permission
class GroundControl:
    def __init__(self, uid):
        self.url = "http://www.teleporter-ground-control.com/"
        self.uid = uid
        self.state_q = "/state_settings"
        self.mission_q = "/mission_settings"

    def light_permission(self):
        if self.query_state_settings():
            return True
        else:
            return False

    def query_state_settings(self):
        try:
            r = requests.get(self.url+self.uid+self.state_q).json()["state_settings"]["lights_on"]
            return r
        except:
            return False

ground_control = GroundControl("826dev")

# while loop for running

while True:
    # listen for sensor trigger
    sensor.check_input()
    if sensor.is_triggered:
        # check api for light and sound state as a condition of playing
        # sounds.play() if sound_permission(ground_control) else 0
        teleport(light_strip) if ground_control.light_permission() else 0
        # stop the sounds if they are currently playing (because the lights are now done)
        # sounds.stop() if sounds.are_playing()
