import json
import os.path
from os import path

# Class representing the span between two joints on a robot arm
class Segment:
    def __init__(self, config_file="segment.json"):
        self.config_file = config_file
        
        # Load constraint data from the config file if it exists
        if path.exists(config_file):
            self.constraints = json.load(open(config_file, 'r'))
        #Otherwise use generic defaults
        else:
            self.constraints = {"offsets" : [0, 0],
                                "length" : 0}
        
    # Used to store config data out to a file
    def store(self):
        with open(self.config_file, 'w') as fp:
            json.dump(self.constraints, fp)

