import requests

class GroundControl:
    def __init__(self, uid):
        self.url = "http://www.teleporter-ground-control.com/"
        self.uid = uid
        self.state_q = "/state_settings"
        self.mission_q = "/mission_settings"
        self.sound_q = "/sound_pattern"

    def power_off(self):
        if self.query_state_settings("power_off"):
            return True
        else:
            return False

    def light_permission(self):
        if self.query_state_settings("lights_on"):
            return True
        else:
            return False

    def sound_permission(self):
        if self.query_state_settings("sound_on"):
            return True
        else:
            return False

    def light_directive(self):
        directive = self.query_mission_settings("light_directive")
        if directive == False:
            return "oz" # default is the rainbow
        else:
            return directive

    def sound_directive(self):
        directive = self.query_sound_pattern()
        if directive == False:
            return ["teleport2", "teleport1", "zap1", "zap1", "zap1", "teleport3"] # default is greenwoodave
        else:
            return directive

    def query_sound_pattern(self):
        try:
            r = requests.get(self.url+self.uid+self.sound_q).json()["sound_pattern"]
            return r
        except:
            return False

    def query_state_settings(self, str):
        try:
            r = requests.get(self.url+self.uid+self.state_q).json()["state_settings"][str]
            return r
        except:
            return False

    def query_mission_settings(self, str):
        try:
            r = requests.get(self.url+self.uid+self.mission_q).json()["mission_settings"][str]
            return r
        except:
            return False
