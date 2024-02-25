#!/usr/bin/env python3
import rclpy
from rclpy.node import Node 

import math

class DrawCircleNode(Node):
    def __init__(self):
        super().__init__("draw_circle_node")
        self.get_logger().info(f"Starting Draw Circle Node")
        self.cmd_vel_pub_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 1)
        self.create_timer(1, self.draw_circle_timer)
    def draw_circle_timer(self):
        msg = Twist()
        msg.linear.x = 2.0
        msg.angular.z = 1.0
        self.cmd_vel_pub_.publish(msg)


def main(args=None):
    rclpy.init()
    node = DrawCircleNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()