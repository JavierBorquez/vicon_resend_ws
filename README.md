
This is a companion script to https://github.com/JavierBorquez/libmotioncapture it takes rigidbody position measurements and publishes them as a odometry topic.

- UDP tunnel to ROS2 odometry publisher
- Only tested with Vicon mocap so far


## Install

From the workspace rubuild and souce the package

```
colcon build
source install/setup.bash
```

## Usage

First get the libmotiocapture package send thr rigidbody info trough UDP:

```
./vicon_sender vicon 192.168.1.39
```

Afterwards run the publisher node:
```
ros2 run vicon_resend vicon_resend
```

to read the stream from a new terminal do:
```
source /opt/ros/humble/setup.bash
ros2 topic echo /odometry --field pose.pose
```

This will stream the pose of all rigidbodies without making any distinction between them.
To properly use it for control make sure there is only one rigidbody in the working area.
