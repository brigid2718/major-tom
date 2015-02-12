import requests

class GroundControl:
    def __init__(self, uid):
        self.url = "http://www.teleporter-ground-control.com/"
        self.uid = uid
        self.state_q = "/state_settings"
        self.mission_q = "/mission_settings"

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

    def query_state_settings(self, str):
        try:
            r = requests.get(self.url+self.uid+self.state_q).json()["state_settings"][str]
            return r
        except:
            return False
