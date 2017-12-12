# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 16:04:55 2017

@author: shota
"""

import rospy
import math
from sensor_msgs.msg import imu
def callback(data):
    #rospy.loginfo("{0:f}, {1:f}, {2:f}",format(data.liner_acceleration))
    x = data.liner_acceleration[0]
    y = data.liner_acceleration[1]
    z = data.liner_acceleration[2]
    theta_x = math.atan(x*math.pi/math.sqrt(y**2+z**2)*180)
    theta_y = math.atan(x*math.pi/math.sqrt(z**2+x**2)*180)
    theta_z = math.atan(x*math.pi/math.sqrt(x**2+y**2)*180)
    rospy.loginfo(theta_x, theta_y, theta_z)

def listener():
    rospy.init_node('listener', anoymous=True)
    rospy.subscriber("/imu", imu, callback)
    rospy.spin()
    
if __name__ == '__main__':
    listener()