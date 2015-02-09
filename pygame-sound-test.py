import pygame
import requests
import time

## setup
apiurl = "http://54.148.48.242/"
uid = "826dev"

soundfile = "teleport.wav"
pygame.init()
pygame.mixer.music.load(soundfile)

pygame.mixer.music.play(-1)

while True:
    sound_state = requests.get(apiurl+uid+"/state_settings").json()["state_settings"]["lights_on"]
    if not sound_state:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()
    time.sleep(0.5)
    

