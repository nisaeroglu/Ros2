import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32MultiArray

class NumberSubscriber(Node):
    def __init__(self):
        super().__init__('number_subscriber')
        self.subscription = self.create_subscription(
            Int32MultiArray,
            'random_numbers',
            self.listener_callback,
            10)

    def listener_callback(self, msg):
        numbers = msg.data
        even_count = sum(1 for n in numbers if n % 2 == 0)
        total = sum(numbers)
        average = total / len(numbers) if numbers else 0

        self.get_logger().info(
            f'Alındı: {numbers} | Çiftler: {even_count} | Toplam: {total} | Ortalama: {average:.2f}'
        )

def main(args=None):
    rclpy.init(args=args)
    node = NumberSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
