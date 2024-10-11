import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class MoveTurtle(Node):
    def __init__(self):
        super().__init__('mitsu')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        timer_period = 0.1
        self.timer = self.create_timer(timer_period, self.move_turtle)
        self.velocity_msg = Twist()

    def move_turtle(self):
        self.velocity_msg.linear.x = 2.0
        self.velocity_msg.angular.z = 1.0
        
        self.publisher_.publish(self.velocity_msg)

def main(args=None):
    rclpy.init(args=args)
    Mitsu = MoveTurtle()
    rclpy.spin(Mitsu)
    Mitsu.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
