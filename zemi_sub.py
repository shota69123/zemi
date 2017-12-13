#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created on Wed Nov 29 16:04:55 2017
#@author: shota

import rospy
import tf
from sensor_msgs.msg import imu

def quaternion_to_eurler(quaternion):
    e = tf.transformations.euler_from_quaternion((quaternion.x, quaternion.y, quaternion.z, quaternion.w))
    return Vector3(x=e[0], y=e[1], z=e[2])

def callback(data):
    Vector3 = quaternion_to_eurler(data.orientation)
    rospy.loginfo(x, y, z)

def listener():
    rospy.init_node('listener', anoymous=True)
    rospy.subscriber("/imu", imu, callback)
    rospy.spin()
    
if __name__ == '__main__':
    listener()
