from joint import Joint, DummyServo
from segment import Segment

# Class that represents a 3-jointed leg for the SpotMicro robot dog
class Leg:
    def __init__(self, leg_name, servos):
        self.leg_name = leg_name
        self.upper_hip = Joint(servos["upper_hip"], leg_name + "upper_hip.json")
        self.hip = Segment(leg_name + "hip.json")
        self.lower_hip = Joint(servos["lower_hip"], leg_name + "lower_hip.json")
        self.femur = Segment(leg_name + "femur.json")
        self.knee = Joint(servos["knee"], leg_name + "knee.json")
        self.tibia = Segment(leg_name + "tibia.json")
        
    def store(self):
        self.upper_hip.store()
        self.hip.store()
        self.lower_hip.store()
        self.femur.store()
        self.knee.store()
        self.tibia.store()

if __name__ == "__main__":
    servos = {"upper_hip":DummyServo(),
              "lower_hip":DummyServo(),
              "knee":DummyServo()}

    l = Leg("FL", servos)
    l.store()
    print(l.upper_hip.constraints)
    print(l.hip.constraints)
    print(l.lower_hip.constraints)
    print(l.femur.constraints)
    print(l.knee.constraints)
    print(l.tibia.constraints)
