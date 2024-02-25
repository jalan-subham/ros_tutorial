#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from turtlesim.srv import SetPen
from functools import partial

class TurtleControllerNode(Node):
    def __init__(self):
        super().__init__("turtle_controller_node")
        self.get_logger().info("Turtle Controller Node Started!")
        self.pose_sub_ = self.create_subscription(Pose, "/turtle1/pose", self.control_turtle, 1)
        self.cmd_vel_pub_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 1)
        self.side = 0
    
    def control_turtle(self, msg: Pose):
        send_msg = Twist()
        if msg.x > 8 or msg.x < 2 or msg.y < 2 or msg.y > 8:
            send_msg.linear.x = 1.0
            send_msg.angular.z = 0.8
        
        else:
            send_msg.linear.x = 5.0
        self.cmd_vel_pub_.publish(send_msg)

        if self.side == 0 and msg.x > 5.5:
            self.side = 1
            self.set_pen_call((255, 0, 0), 3, 0)
        elif self.side == 1 and msg.x < 5.5:
            self.side = 0
            self.set_pen_call((0, 255, 0), 5, 0)
        


    def set_pen_call(self, color, width, off):
        client = self.create_client(SetPen, "/turtle1/set_pen")
        while not client.wait_for_service(1):
            self.get_logger().warn("Waiting...")
        request = SetPen.Request()
        request.r = color[0]
        request.g = color[1]
        request.b = color[2]
        request.width = width
        request.off = off 

        future = client.call_async(request)
        future.add_done_callback(partial(self.service_call_callback))
    def service_call_callback(self, future):
        try:
            response = future.result()
            self.get_logger().debug("Success" + str(response))
        except Exception as e:
            self.get_logger().error(f"Error encountered: {e}")





def main(args=None):
    rclpy.init()
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()