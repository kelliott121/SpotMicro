import argparse
from leg import Leg
from joint import DummyServo

class DummyServoKit:
    def __init__(self, channels, address=0x40):
        self.channels = channels
        self.address = address
        self.servo = [DummyServo()] * self.channels

# Class that represents a four-legged robot base
class Base:
    def __init__(self, servo_kit):
        self.legs = {}
        # Move servo mapping to a saveable config
        fl_map = {}
        fl_map["upper_hip"] = servo_kit.servo[0]
        fl_map["lower_hip"] = servo_kit.servo[1]
        fl_map["knee"] = servo_kit.servo[2]
        self.legs["FL"] = Leg("FL", [-75, 150], fl_map)
        fr_map = {}
        fr_map["upper_hip"] = servo_kit.servo[3]
        fr_map["lower_hip"] = servo_kit.servo[4]
        fr_map["knee"] = servo_kit.servo[5]
        self.legs["FR"] = Leg("FR", [75, 150], fr_map)
        bl_map = {}
        bl_map["upper_hip"] = servo_kit.servo[6]
        bl_map["lower_hip"] = servo_kit.servo[7]
        bl_map["knee"] = servo_kit.servo[8]
        self.legs["BL"] = Leg("BL", [-75, -150], bl_map)
        br_map = {}
        br_map["upper_hip"] = servo_kit.servo[9]
        br_map["lower_hip"] = servo_kit.servo[10]
        br_map["knee"] = servo_kit.servo[11]
        self.legs["BR"] = Leg("BR", [75, -150], br_map)
        
    def store(self):
        for l in self.legs.values():
            l.store()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--sim", action="store_true")
    args = parser.parse_args()
    
    kit = None
    if (args.sim):
        kit = DummyServoKit(channels=16)
    else:
        from adafruit_servokit import ServoKit
        # Set channels to the number of servo channels on your kit.
        # 8 for FeatherWing, 16 for Shield/HAT/Bonnet.
        kit = ServoKit(channels=16)

    b = Base(kit)
    b.store()
