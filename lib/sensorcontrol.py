import RPi.GPIO as GPIO

class Sensor:
    def __init__(self, pin=18, sensor_type="pir"):
        self.pin = pin
        self.sensor_type = sensor_type
        self.setup()
        self.value = GPIO.input(self.pin)

    def is_triggered(self):
        self.update_state()
        if self.value == 1 and self.previous_value == 0:
            return True
        else:
            return False

    def update_state(self):
        self.previous_value = self.value
        self.value = GPIO.input(self.pin)

    def setup(self):
        GPIO.setmode(GPIO.BOARD)
        if self.sensor_type == "pir":
            GPIO.setup(self.pin, GPIO.IN)
        elif self.sensor_type == "button":
            GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def check_for_button_press(self, previous_sensor_state, current_sensor_state):
        d_sensor_state_dt = abs(current_sensor_state - previous_sensor_state)
        if d_sensor_state_dt > 0:
            if current_sensor_state == 0:
                print "button is down"
            elif current_sensor_state == 1:
                print "button is released"
                self.trigger()

    def check_for_motion(self, previous_sensor_state, current_sensor_state):
        d_sensor_state_dt = current_sensor_state - previous_sensor_state
        if d_sensor_state_dt > 0:
            "motion detected!"
            self.trigger()
