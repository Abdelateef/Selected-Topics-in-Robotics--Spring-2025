#!/usr/bin/env python3

import rospy
from turtlebot3_custom_control.msg import Command

def main():
    rospy.init_node('turtle_control_publisher', anonymous=True)
    pub = rospy.Publisher('/turtlebot3_command', Command, queue_size=10)
    rate = rospy.Rate(10)  # 10Hz

    while not rospy.is_shutdown():
        direction = input("Enter direction (forward/backward/left/right): ")
        speed = float(input("Enter speed (0.1 to 1.0): "))

        if direction not in ["forward", "backward", "left", "right"]:
            print("Invalid direction! Try again.")
            continue

        if speed < 0.1 or speed > 1.0:
            print("Speed must be between 0.1 and 1.0! Try again.")
            continue

        command = Command()
        command.direction = direction
        command.speed = speed
        pub.publish(command)
        rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass