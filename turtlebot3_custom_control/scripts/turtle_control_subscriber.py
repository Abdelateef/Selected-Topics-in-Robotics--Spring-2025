#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from turtlebot3_custom_control.msg import Command

def callback(msg):
    vel_msg = Twist()

    if msg.direction == "forward":
        vel_msg.linear.x = msg.speed
    elif msg.direction == "backward":
        vel_msg.linear.x = -msg.speed
    elif msg.direction == "left":
        vel_msg.angular.z = msg.speed
    elif msg.direction == "right":
        vel_msg.angular.z = -msg.speed

    pub.publish(vel_msg)

def main():
    global pub
    rospy.init_node('turtle_control_subscriber', anonymous=True)
    pub = rospy.Publisher('/cmd_vel', Twist, queue_size=10)
    rospy.Subscriber('/turtlebot3_command', Command, callback)
    rospy.spin()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass