#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from time import sleep
from adafruit_servokit import ServoKit

#Jalan state 1
#Berdiri state 0
#Kiri state 2
#Kanan state 3


# class MyNode(Node):
#     def __init__(self):
#         super().__init__("servo")
#         self.subscriber_message_ = self.create_subscription(String, "/state", self.repeat_, 1)
#         global data
    
#     def repeat_(self, message: String):
#         data = str(message.data)
#         self.get_logger().info("State " + data)


class MyNode(Node):
    def __init__(self):
        super().__init__("servo")
        self.subscriber_message_ = self.create_subscription(String, "/state", self.repeat_, 1)
    
    def repeat_(self, message: String):
        self.get_logger().info("State " + str(message.data))

def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()