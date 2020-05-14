from adafruit_motor import servo
import json
import os.path
from os import path

# Dummy class that pretends to be an Adafruit servo motor
class DummyServo:
    def __init__(self):
        self.min_duty = None
        self.max_duty = None
        self.fraction = None
        self.angle = None
        self.actuation_range = None
        
    def set_pulse_width_range(self, min_duty, max_duty):
        self.min_duty = min_duty
        self.max_duty = max_duty
        self.fraction = None
        self.angle = None
        

# Class that represents a joint on a robot arm
class Joint:
    # Take in an Adafruit servo motor and a config file where joint
    # configuration data is stored
    def __init__(self, servo, config_file="servo.json"):
        self.servo = servo
        self.config_file = config_file
        
        # Load constraint data from the config file if it exists
        if path.exists(config_file):
            self.constraints = json.load(open(config_file, 'r'))
        #Otherwise use generic defaults
        else:
            self.constraints = {"min_duty" : 1500,
                                "max_duty" : 2500,
                                "actuation_range" : 180}
        # Update the servo object to reflect the constraints
        self.servo.set_pulse_width_range(self.constraints["min_duty"],
                                         self.constraints["max_duty"])
        self.servo.actuation_range = self.constraints["actuation_range"]
        
    # Used to store config data out to a file
    def store(self):
        with open(self.config_file, 'w') as fp:
            json.dump(self.constraints, fp)
        
j = Joint(DummyServo())
j.constraints["min_duty"] = 1250
j.store()
