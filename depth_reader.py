#! /usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import os
import time
import cv2
import sys
import numpy as np
import message_filters
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
#from pic_1 import onMouse

class depth_reader:
    def __init__(self):
        rospy.init_node('depth_reader', anonymous=True)
        self.bridge = CvBridge()
        #適当なTopicを選択し、サブスクライバを定義
        sub_rgb = message_filters.Subscriber("/camera/color/image_raw",Image)
        sub_depth = message_filters.Subscriber("camera/depth/image_rect_raw",Image)
        #RGBデータとdepthデータの物理時間的ズレを補正
        self.mf = message_filters.ApproximateTimeSynchronizer([sub_rgb, sub_depth], 100, 10.0)
        self.mf.registerCallback(self.ImageCallback)
    
    def draw(self, image, width, height, depth):
        #画像に赤の十字を描画
        cv2.line(image, ((width/2)-15, height/2), ((width/2)+15, height/2), (0, 0, 255), 2)
        cv2.line(image, (width/2, (height/2)-15), (width/2, (height/2)+15), (0, 0, 255), 2)
        #width, height, depth情報を表示
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(image,"width={0}, height={1}".format(width, height) , (10,15), font, .5, (0,0,0), 1, cv2.LINE_AA)
        cv2.putText(image,"+:depth={0}".format(depth) , (10,30), font, .5, (0,0,0), 1, cv2.LINE_AA)

    #depthの値を入力したら、それ以上の値をすべて0にして返すよ
    def depth_Adjustment(self, depth_Threshold):
        pass

    def ImageCallback(self, rgb_data , depth_data):
        try:
            rospy.loginfo("小池を崇めろ")
            color_image = self.bridge.imgmsg_to_cv2(rgb_data, 'passthrough')
            depth_image = self.bridge.imgmsg_to_cv2(depth_data, 'passthrough')
        except CvBridgeError, e:
            rospy.logerr(e)

        color_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB) 
        h, w, c = color_image.shape
        self.draw(color_image, w, h, depth_image[w/2][h/2])
        cv2.namedWindow("color_image")
        cv2.imshow("color_image", color_image)
        cv2.waitKey(10)

if __name__ == '__main__':
    try:
        de = depth_reader()
        rospy.spin()
    except rospy.ROSInterruptException: pass

