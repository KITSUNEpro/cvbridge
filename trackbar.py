# -*- coding: utf-8 -*-
import cv2

def changeX(val):#トラックバーの値が変更されたときに行う処理
    pass

cv2.namedWindow("img",cv2.WINDOW_NORMAL)
cv2.createTrackbar("x-controller","img",1,100,changeX)

while (True):
    x=cv2.getTrackbarPos("x-controller","img")#トラックバーの値を取得
    print x
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
