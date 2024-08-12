import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry

import socket

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 8080)
sock.bind(server_address)


class OdometryPublisher(Node):
    def __init__(self):
        super().__init__('odometry_publisher')
        self.publisher_ = self.create_publisher(Odometry, 'odom', 10)
        timer_period = 0.05  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def publish_odometry(self, x, y, z, quat_x, quat_y, quat_z, quat_w):
        msg = Odometry()
        msg.header.stamp = self.get_clock().now().to_msg()
        msg.pose.pose.position.x = x
        msg.pose.pose.position.y = y
        msg.pose.pose.position.z = z
        msg.pose.pose.orientation.x = quat_x
        msg.pose.pose.orientation.y = quat_y
        msg.pose.pose.orientation.z = quat_z
        msg.pose.pose.orientation.w = quat_w
        self.publisher_.publish(msg)
        return msg

    def timer_callback(self):
        data, address = None, None
        while True: #drop all the data except the last one
            try:
                data, address = sock.recvfrom(4096, socket.MSG_DONTWAIT)
            except socket.error:
                break

        if data is None:
            return

        data_str = data.decode("utf-8")
        # Remove unwanted characters
        clean_str = data_str.replace("b'", "").replace("'\n", "").replace("\"", "")
        # Split the string into components
        components = clean_str.split("\n")
        # Extract the name
        name = components[0].split(":")[0]
        # Extract the positions and convert them to floats
        positions = [float(pos) for pos in components[1].replace("position: [", "").replace("]", "").split(", ")]
        # Extract the rotations and convert them to floats
        rotations = [float(rot) for rot in components[2].replace("rotation: [", "").replace("]", "").split(", ")]
        #print clean data
        print(name)
        print(positions)  
        print(rotations)
        odom_now = self.publish_odometry(positions[0], positions[1], positions[2], rotations[0], rotations[1], rotations[2], rotations[3])
        #self.get_logger().info('Publishing: "%s"' % odom_now)

def main(args=None):
    rclpy.init(args=args)
    node = OdometryPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()