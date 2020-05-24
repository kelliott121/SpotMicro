from joint import Joint, DummyServo
from segment import Segment
from os import makedirs, path

# Class that represents a 3-jointed leg for the SpotMicro robot dog
class Leg:
    def __init__(self, leg_name, offset, servos):
        self.leg_name = leg_name
        if not path.exists("config/" + leg_name):
            makedirs(leg_name)
        
        self.offset = offset
        self.upper_hip = Joint(servos["upper_hip"], "config/" + leg_name + "/upper_hip.json")
        self.hip = Segment("config/" + leg_name + "/hip.json")
        self.lower_hip = Joint(servos["lower_hip"], "config/" + leg_name + "/lower_hip.json")
        self.femur = Segment("config/" + leg_name + "/femur.json")
        self.knee = Joint(servos["knee"], "config/" + leg_name + "/knee.json")
        self.tibia = Segment("config/" + leg_name + "/tibia.json")
        
    def store(self):
        self.upper_hip.store()
        self.hip.store()
        self.lower_hip.store()
        self.femur.store()
        self.knee.store()
        self.tibia.store()
    
    def move(self, upper_hip_angle, lower_hip_angle, knee_angle):
        self.upper_hip.move(upper_hip_angle)
        self.lower_hip.move(lower_hip_angle)
        self.knee.move(knee_angle)

if __name__ == "__main__":
    servos = {"upper_hip":DummyServo(),
              "lower_hip":DummyServo(),
              "knee":DummyServo()}

    l = Leg("FL", [-75, 150, 0], servos)
    l.store()
    print(l.upper_hip.constraints)
    print(l.hip.constraints)
    print(l.lower_hip.constraints)
    print(l.femur.constraints)
    print(l.knee.constraints)
    print(l.tibia.constraints)
