import RPi.GPIO as GPIO

class Sensor:
    def __init__(self, pin=18):
        self.is_triggered = False
        self.pin = pin

    def button_setup(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def pir_setup(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.IN)

    def trigger(self):
        self.is_triggered = True

    def untrigger(self):
        self.is_triggered = False

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
