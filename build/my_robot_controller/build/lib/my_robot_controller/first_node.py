#!/usr/bin/env python3
import rclpy
from rclpy.node import Node


class MyNode(Node):
    def __init__(self):
        super().__init__("name_first_node")
        self.counter_ = 1
        self.create_timer(1, self.print_hello)
        # self.get_logger().info("Hello There!")
    def print_hello(self):
        self.get_logger().info(f"Hello {self.counter_}")
        self.counter_ += 1
    
def main(args=None):
    rclpy.init()

    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()