# TurtleBot3 Custom Control

## Purpose
Control **TurtleBot3** in **Gazebo** using a custom **ROS publisher & subscriber**.

## Custom Message: `Command.msg`
```plaintext
string direction  # "forward", "backward", "left", "right"
float32 speed     # 0.1 to 1.0
```

## Implementation
### **Publisher (`turtle_control_publisher.py`)**
- Publishes **user input** (direction & speed) to `/turtle_control`.
- Runs at a **fixed rate** using `rospy.Publisher`.

### **Subscriber (`turtle_control_subscriber.py`)**
- Subscribes to `/turtle_control`, converts messages into **velocity commands**.
- Publishes `Twist` messages to `/cmd_vel`.

## Running the Simulation
```bash
export TURTLEBOT3_MODEL=burger
roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
rosrun turtlebot3_custom_control turtle_control_publisher.py
rosrun turtlebot3_custom_control turtle_control_subscriber.py
rostopic echo /turtle_control  # Verify messages
rostopic echo /cmd_vel         # Verify movement
```

## Observations
- TurtleBot3 moves correctly with valid inputs.
- Invalid directions are ignored.
- /cmd_vel` topic updates confirm velocity commands.

