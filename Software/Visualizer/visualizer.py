from mpl_toolkits.mplot3d import Axes3D
import matplotlib
import matplotlib.pyplot as plt
import sys
import math

sys.path.append("../Motion")

from base import Base
from segment import Segment

def base_to_plot(robot_base):
    x_coords = [robot_base.dimensions[0]/2, robot_base.dimensions[0]/2, -robot_base.dimensions[0]/2, -robot_base.dimensions[0]/2, robot_base.dimensions[0]/2]
    y_coords = [robot_base.dimensions[1]/2, -robot_base.dimensions[1]/2, -robot_base.dimensions[1]/2, robot_base.dimensions[1]/2, robot_base.dimensions[1]/2]
    z_coords = [0, 0, 0, 0, 0]

    return [x_coords, y_coords, z_coords]

def plot_robot(robot_base):
    fig = plt.figure()
    ax = Axes3D(fig)

    plt.xlim(-200, 200)
    plt.ylim(-200, 200)
    ax.set_zlim(-300, 100)

    ax.set_xlabel("X (mm)")
    ax.set_ylabel("Y (mm)")
    ax.set_zlabel("Z (mm)")

    # Plot the main body of the robot
    base_plot = base_to_plot(robot_base)
    ax.plot(base_plot[0], base_plot[1], base_plot[2])

    for leg_name in robot_base.legs:
        leg = robot_base.legs[leg_name]
        print("=========================")
        print(leg_name)
        print("=========================")

        # Each joint of the leg affects the angle of the joints below it. Define a spin (Angle Around X, Angle Around Y)
        # to represent the progressive spin the the joints
        spin = [0, 0]

        # Plot the hip line
        hip_angle = 0
        # Invert for left hips
        if leg.leg_name.endswith("L"):
            hip_angle = 180
        elif leg.leg_name.endswith("R"):
            hip_angle = 0
        print("=====HIP=====")
        hip_plot = plot_segment(leg.hip, leg.offset, spin, hip_angle, leg.upper_hip.constraints["axis"])
        hip_points = hip_plot["points"]
        spin = hip_plot["spin"]
        ax.plot(hip_points[0], hip_points[1], hip_points[2])
        ax.plot(hip_points[0], hip_points[1], hip_points[2], "o")

        # Plot the femur line
        print("=====FEMUR=====")
        femur_origin = [hip_points[0][1], hip_points[1][1], hip_points[2][1]]
        femur_plot = plot_segment(leg.femur, femur_origin, spin, -30, leg.lower_hip.constraints["axis"])
        femur_points = femur_plot["points"]
        spin = femur_plot["spin"]
        ax.plot(femur_points[0], femur_points[1], femur_points[2])
        ax.plot(femur_points[0], femur_points[1], femur_points[2], "o")

        # Plot the tibia line
        print("=====TIBIA=====")
        tibia_origin = [femur_points[0][1], femur_points[1][1], femur_points[2][1]]
        tibia_plot = plot_segment(leg.tibia, tibia_origin, spin, -120, leg.knee.constraints["axis"])
        tibia_points = tibia_plot["points"]
        spin = tibia_plot["spin"]
        ax.plot(tibia_points[0], tibia_points[1], tibia_points[2])
        ax.plot(tibia_points[0], tibia_points[1], tibia_points[2], "o")

    plt.show()

def plot_segment(leg_segment, origin, spin, angle_deg, axis):
    coord2 = [0, 0, 0]
    length = leg_segment.constraints["length"]

    angleRX = math.radians(leg_segment.constraints["angle_offset"][0] + spin[0])
    angleRY = math.radians(leg_segment.constraints["angle_offset"][1] + spin[1])
    print("CMD: " + str(angle_deg))
    print("Spin: " + str(spin))

    if axis == "X":
        angleRX += math.radians(angle_deg)

        coord2[0] = origin[0] - (length * math.cos(angleRY))
        print("X:" + str(coord2[0]))
        coord2[1] = origin[1] - (length * math.cos(angleRX))
        print("Y:" + str(coord2[1]) + " = l:" + str(length) + " * cos(RX:" + str(math.degrees(angleRX)) + ")")
        coord2[2] = origin[2] + (length * math.sin(angleRX) * math.sin(angleRY))
        print("Z:" + str(coord2[2]) + " = l:" + str(length) + " * sin(RX" + str(math.degrees(angleRX)) + ") * sin(RY" + str(math.degrees(angleRY)) + ")")

        spin[0] += angle_deg
    elif axis == "Y":
        angleRY += math.radians(angle_deg)

        coord2[0] = origin[0] + (length * math.cos(angleRY))
        print("X:" + str(coord2[0]) + " = l:" + str(length) + " * cos(" + str(math.degrees(angleRY)) + ")")
        coord2[1] = origin[1]
        print("Y:" + str(coord2[1]))
        coord2[2] = origin[2] + (length * math.sin(angleRY))
        print("Z:" + str(coord2[2]) + " = l:" + str(length) + " * sin(RY" + str(math.degrees(angleRY)) + ")")

        spin[1] += angle_deg

    print ("Origin: " + str(origin))
    print("RX: " + str(math.degrees(angleRX)))
    print("RY: " + str(math.degrees(angleRY)))

    return {"points":[[origin[0], coord2[0]], [origin[1], coord2[1]], [origin[2], coord2[2]]], "spin":spin}

if __name__ == "__main__":
    fig = plt.figure()
    ax = Axes3D(fig)
    plt.xlim(-200, 200)
    plt.ylim(-200, 200)
    ax.set_zlim(-100, 50)

    x = [-75,75,75,-75,-75]
    y = [-150,-150,150,150,-150]
    z = [0,0,0,0,0]
    ax.plot(x, y, z)
    ax.plot(x, y, z, 'o')
    ax.set_xlabel("X (mm)")
    ax.set_ylabel("Y (mm)")
    ax.set_zlabel("Z (mm)")

    plt.show()