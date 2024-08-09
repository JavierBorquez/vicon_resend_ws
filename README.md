
This is a companion script to https://github.com/JavierBorquez/libmotioncapture it takes rigidbody position measurements and publishes them as a odometry topic.

## Install

From the workspace build and source the package:

```
colcon build
source install/setup.bash
```

## Usage

First get the libmotioncapture package send the rigidbody data trough UDP:

```
./vicon_sender vicon 192.168.1.39
```

Afterwards run the publisher node:
```
ros2 run vicon_resend vicon_resend
```

To read the stream from a new terminal do:
```
source /opt/ros/humble/setup.bash
ros2 topic echo /odometry --field pose.pose
```

This will stream the pose of all rigidbodies without making any distinction between them.
To properly use it for control make sure there is only one rigidbody in the working area.
