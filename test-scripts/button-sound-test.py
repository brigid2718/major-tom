import pygame
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

soundfile = "teleport.wav"
pygame.init()
pygame.mixer.music.load(soundfile)
pygame.mixer.music.set_volume(0.1)

def toggle_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()
    else:
        pygame.mixer.music.play(-1)

previous_input_state = GPIO.input(18)

while True:
    current_input_state = GPIO.input(18)
    d_input_state_dt = abs(current_input_state - previous_input_state)
    if d_input_state_dt > 0:
        if current_input_state == 0:
            print "button is pressed down"
        elif current_input_state == 1:
            print "button is let go, this is the trigger"
            toggle_music()
    previous_input_state = current_input_state
