#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Created on Wed Nov 29 16:04:55 2017
#@author: shota

import rospy
import tf
from sensor_msgs.msg import Imu

def callback(data):
    e = tf.transformations.euler_from_quaternion((data.orientation.x, data.orientation.y, data.orientation.z, data.orientation.w))
    e_deg_zengo = (e[1] + 0.05) * 180 / 3.14259265359
    rospy.loginfo("傾斜角度：%s°" % e_deg_zengo)
    #rospy.loginfo("%s, %s, %s" % (e[0], e[1], e[2]))

def listener():
    rospy.init_node('listener', anonymous=True)
    rospy.Subscriber("/imu", Imu, callback)
    rospy.spin()
    
if __name__ == '__main__':
    listener()
