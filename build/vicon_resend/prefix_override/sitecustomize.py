import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/javier/ROS2_work/vicon_warehouse/vicon_resend_ws/install/vicon_resend'
