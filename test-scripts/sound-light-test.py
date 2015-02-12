import requests
import RPi.GPIO as GPIO

import time
import sys
import pygame
sys.path.append('/home/pi/rpi_ws281x/python')

from neopixel import *

# functions that will be used below

def toggle_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
    else:
        pygame.mixer.music.play(-1)

def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms/1000.0)

def teleport(strip):
    colorWipe(strip, Color(0,255,0))
    colorWipe(strip, Color(0,0,0))

# Here is the initialization of the light strip

# LED strip configuration:
LED_COUNT      = 30      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 5       # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)


# light_strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
# light_strip.begin()

# Initialize sound stuff

soundfile = "teleport.wav"
pygame.init()
pygame.mixer.music.load(soundfile)
pygame.mixer.music.set_volume(0.1)


# start the music, make the lights go, stop the music

pygame.mixer.music.play(-1)
