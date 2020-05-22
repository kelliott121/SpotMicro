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
    ax.set_zlim(-100, 50)

    # Plot the main body of the robot
    base_plot = base_to_plot(robot_base)
    ax.plot(base_plot[0], base_plot[1], base_plot[2])

    for leg_name in robot_base.legs:
        leg = robot_base.legs[leg_name]
        # Plot the hip line
        hip_plot = plot_segment(leg.hip, leg.offset, 0, "y")
        ax.plot(hip_plot[0], hip_plot[1], hip_plot[2])
        ax.plot(hip_plot[0], hip_plot[1], hip_plot[2], "o")

        # Plot the femur line
        femur_origin = [hip_plot[0][1], hip_plot[1][1], hip_plot[2][1]]
        femur_plot = plot_segment(leg.femur, femur_origin, -170, "x")
        ax.plot(femur_plot[0], femur_plot[1], femur_plot[2])
        ax.plot(femur_plot[0], femur_plot[1], femur_plot[2], "o")

        # Plot the tibia line
        tibia_origin = [femur_plot[0][1], femur_plot[1][1], femur_plot[2][1]]
        tibia_plot = plot_segment(leg.tibia, tibia_origin, -30, "x")
        ax.plot(tibia_plot[0], tibia_plot[1], tibia_plot[2])
        ax.plot(tibia_plot[0], tibia_plot[1], tibia_plot[2], "o")

    plt.show()

def plot_segment(leg_segment, origin, angle_deg, axis):
    coord2 = [0, 0, 0]
    angle = math.radians(angle_deg) + math.radians(leg_segment.constraints["angle_offset"])
    length = leg_segment.constraints["length"]

    if axis == "x":
        coord2[0] = origin[0]
        coord2[1] = length * math.cos(angle) + origin[1]
        coord2[2] = length * math.sin(angle) + origin[2]
        return [[origin[0], coord2[0]], [origin[1], coord2[1]], [origin[2], coord2[2]]]
    elif axis == "y":
        coord2[0] = length * math.cos(angle) + origin[0]
        coord2[1] = origin[1]
        coord2[2] = length * math.sin(angle) + origin[2]
        return [[origin[0], coord2[0]], [origin[1], coord2[1]], [origin[2], coord2[2]]]

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

    plt.show()