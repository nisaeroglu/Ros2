import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray
import random

class NumberPublisher(Node):
    def __init__(self):
        super().__init__('number_publisher')
        self.publisher_ = self.create_publisher(Int32MultiArray, 'random_numbers', 10)
        self.timer = self.create_timer(2.0, self.publish_numbers)

    def publish_numbers(self):
        msg = Int32MultiArray()
        msg.data = [random.randint(1, 1000) for _ in range(5)]
        self.publisher_.publish(msg)
        self.get_logger().info(f'Yayınlandı: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    node = NumberPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
