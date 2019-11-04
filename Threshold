#!/usr/bin/env python
## coding: UTF-8

import rospy
import cv2
import sys
from cv_bridge import CvBridge, CvBridgeError
from std_msgs.msg import String
from sensor_msgs.msg import Image

bridge = CvBridge()

def callback(depth_data):
    try:
        #rospy.loginfo(message.data)
        depth_image = bridge.imgmsg_to_cv2(depth_data, 'passthrough')
        height, width = depth_image.shape
        print(height, width)
        #depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.08), cv2.COLORMAP_JET)
        #print(depth_image[[10]][0][100])
        #cv2.imshow('RealSense', depth_colormap)
        #cv2.waitKey(10)
    except CvBridgeError, e:
        rospy.logerr(e)
rospy.init_node('depth_listener')
sub = rospy.Subscriber('camera/depth/image_rect_raw', Image, callback)
rospy.spin()
