import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import functools
import time

class Mitsu(Node):

    def __init__(self):
        super().__init__('mitsu')
        self.timer = self.create_timer(0.2, self.loop)
        self.cmd_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.loop_count = 1
        self.get_logger()

    def loop(self):
        cmd_msg = Twist()
        if self.loop_count < 20:
            cmd_msg.linear.x = 1.0
            cmd_msg.angular.z = 0.0
        elif self.loop_count > 20 and self.loop_count <= 25:
            cmd_msg.linear.x = 0.0
            cmd_msg.angular.z = -1.0472
        elif self.loop_count > 25 and self.loop_count < 35:
            cmd_msg.linear.x = 1.1
            cmd_msg.angular.z = 0.0
        elif self.loop_count > 35 and self.loop_count <= 40:
            cmd_msg.linear.x = 0.0
            cmd_msg.angular.z = 1.0472
        elif self.loop_count > 40 and self.loop_count < 50:
            cmd_msg.linear.x = -1.1
            cmd_msg.angular.z = 0.0
        elif self.loop_count > 50 and self.loop_count <= 55:
            cmd_msg.linear.x = 0.0
            cmd_msg.angular.z = 2.0944
        self.cmd_pub.publish(cmd_msg)
        self.loop_count += 1
        if self.loop_count > 60:
            self.loop_count = 0

def main(args=None):
    rclpy.init(args=args)
    mitsu = Mitsu()
    rclpy.spin(mitsu)
    mitsu.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
