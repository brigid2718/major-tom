# Main script for running the teleporter!

# modules to import
import requests

# initiate light strip and load light strip functions
    # there should be a strip object that can display a pattern
# initiate sensor and load sensor reading functions
    # there should be a sensor object that has a is_triggered attribute
class Sensor:
    def __init__(self):
        self.is_triggered = False

    def trigger(self):
        self.is_triggered = True

    def untrigger(self):
        self.is_triggered = False

# initiate sound control and load functions
    # there should be a sounds object that can play and pause
# initiate ground control communications
    # there should be a ground_control object that has attributes light_permission
    # and sound_permission
class GroundControl:
    def __init__(self, url, uid):
        self.url = url
        self.uid = uid

    def light_permission(self):
        if requests.get(self.url+"/"+self.uid+"/state_settings").json()["state_settings"]["lights_on"]:
            return True
        else:
            return False

# while loop for running

while True:
    # listen for sensor trigger
    if sensor.is_triggered:
        # check api for light and sound state as a condition of playing
        # sounds.play() if sound_permission(ground_control) else 0
        strip.display() if light_permission(ground_control) else 0
        # stop the sounds if they are currently playing (because the lights are now done)
        # sounds.stop() if sounds.are_playing()
