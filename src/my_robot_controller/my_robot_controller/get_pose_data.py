#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
import time

class ListenPoseNode(Node):
    def __init__(self):
        super().__init__("listen_pose_node")
        self.get_logger().info("Listen Pose Node started!")
        self.pose_sub_ = self.create_subscription(Pose, "/turtle1/pose", self.listen_pose_data, 1)
    def listen_pose_data(self, msg):
        time.sleep(1)
        print(msg)

    

def main(args=None):
    rclpy.init()
    node = ListenPoseNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()