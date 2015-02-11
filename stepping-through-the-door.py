# Main script for running the teleporter!

# modules to import
import requests
import time
import RPi.GPIO as GPIO
import sys
import pygame
sys.path.append('/home/pi/rpi_ws281x/python')
# sys.path.append('/home/pi/adxl345-python')

from neopixel import *

# from adxl345 import ADXL345
# from random import randint

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

# light_strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
# light_strip.begin()

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
    def __init__(self, pin=18):
        self.is_triggered = False
        self.pin = pin

    def button_setup(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def trigger(self):
        self.is_triggered = True

    def untrigger(self):
        self.is_triggered = False

    def check_for_trigger(self, previous_sensor_state, current_sensor_state):
        d_sensor_state_dt = abs(current_sensor_state - previous_sensor_state)
        if d_sensor_state_dt > 0:
            if current_sensor_state == 0:
                print "button is pressed down"
            elif current_sensor_state == 1:
                print "button released"
                self.trigger()

# Here is the setup of the sensor (button right now)

sensor = Sensor()
sensor.button_setup()

# initiate sound control and load functions
    # there should be a sounds object that can play and pause
soundfile = "teleport.wav"
pygame.init()
pygame.mixer.music.load(soundfile)
pygame.mixer.music.set_volume(0.1)

def toggle_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
    else:
        pygame.mixer.music.play(-1)

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

previous_sensor_state = GPIO.input(sensor.pin)

while True:
    current_sensor_state = GPIO.input(sensor.pin)
    # listen for sensor trigger
    sensor.check_for_trigger(previous_sensor_state, current_sensor_state)
    if sensor.is_triggered:
        print "in triggered block"
        # check api for light and sound state as a condition of playing
        # sounds.play() if sound_permission(ground_control) else 0
        toggle_music() if ground_control.light_permission() else 0
        # teleport(light_strip) if ground_control.light_permission() else 0
        # untrigger the sensor state
        sensor.untrigger()
        # stop the sounds if they are currently playing (because the lights are now done)
        # sounds.stop() if sounds.are_playing()
    previous_sensor_state = current_sensor_state
