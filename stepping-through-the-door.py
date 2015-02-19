# Main script for running the teleporter!

# modules to import
import requests
import threading
import RPi.GPIO as GPIO
import pygame
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

# pygame sound thread

# def music_thread(arg1, stop_event):
#     load first song and move it to the end of the list
#     play music
#     queue second song
#
#     while not stop event is set:
#         if music end event exists:
#             load and play next song
#     stop music

def music_thread(sounds, stop_event):
    pygame.mixer.music.load("/home/pi/major-tom/sound-lib/"+sounds[0]+".wav")
    sounds.append(sounds.pop(0)) # move to the end of the list
    pygame.mixer.music.play()
    # queue second song
    pygame.mixer.music.queue("/home/pi/major-tom/sound-lib/"+sounds[0]+".wav")
    sounds.append(sounds.pop(0)) # move to the end of the list
    pygame.mixer.music.set_endevent(1)

    while(not stop_event.is_set()):
        if len(pygame.event.get()) > 0:
            pygame.mixer.music.load("/home/pi/major-tom/sound-lib/"+sounds[0]+".wav")
            sounds.append(sounds.pop(0)) # move to the end of the list

    pygame.mixer.music.stop()



# set up comminications with ground control

ground_control = groundcontrol.GroundControl("826dev")

# set up light strip

light_strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
light_strip.begin()

# set up the button sensor

sensor = sensorcontrol.Sensor(16)

# set up the sound file
pygame.init()
# has to have a display set for event handling
pygame.display.set_mode((0, 0))
pygame.mixer.init()

# start the loop

while True:
    # if sensor trigger for given amount of time do:
        # play lights if allowed
        # play music if allowed
    print sensor.value # debugging
    if sensor.is_triggered():
        print "in triggered block" # debugging
        start_time = time.time()
        time_elapsed = 0
        if ground_control.sound_permission():
            # sound_pattern = ground_control.sound_directive()
            sound_pattern = ["teleport2", "teleport1", "zap1", "zap1", "zap1", "teleport3"]
            music_stop= threading.Event()
            play_music = threading.Thread(target=music_thread, args=(sound_pattern, music_stop))
        if ground_control.light_permission():
            light_pattern = ground_control.light_directive()
            #patternlib = os.listdir(patternlibdir)
            execfile("/home/pi/major-tom/pattern-lib/"+light_pattern+".py") # if light_pattern.py in patternlib
            while time_elapsed < 15:
                display_pattern(light_strip)
                time_elapsed = time.time() - start_time
            turnOff(light_strip)
        while time_elapsed < 15:
            time_elapsed = time.time() - start_time
        # turn off the music thread by sending the stop event
        music_stop.set()
