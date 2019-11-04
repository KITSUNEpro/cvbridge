#! /usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import numpy as np

class PointList():
    def __init__(self, npoints):
        self.npoints = npoints
        self.ptlist = np.empty((npoints, 2), dtype=int)
        self.pos = 0

    def add(self, x, y):
        if self.pos < self.npoints:
            self.ptlist[self.pos, :] = [x, y]
            self.pos += 1
            return True
        return False

def onMouse( event, x, y, flag, params ):

    if event == cv2.EVENT_MOUSEMOVE:#青色十字線表示
        img2 = np.copy( img )
        h, w = img2.shape[0], img2.shape[1]
        cv2.line( img2, ( x, 0 ), ( x, h - 1 ), ( 255, 0, 0 ) )
        cv2.line( img2, ( 0, y ), ( w - 1, y ), ( 255, 0, 0 ) )
        cv2.imshow( wname, img2 )

    if event == cv2.EVENT_LBUTTONDOWN: # レフトボタンをクリックしたとき、ptlist配列にx,y座標を格納する
        if ptlist.add(x, y):
            print('[%d] ( %d, %d )' % (ptlist.pos - 1, x, y))
            cv2.circle(img, (x, y), 3,(0, 0, 255), 1)
            cv2.imshow(wname, img)

    if event == cv2.EVENT_LBUTTONUP: # レフトボタンを離したとき、ptlist配列にx,y座標を格納する
        if ptlist.add(x, y):
            print('[%d] ( %d, %d )' % (ptlist.pos - 1, x, y))
            cv2.circle(img, (x, y), 3,(0, 0, 255), 1)
            cv2.imshow(wname, img)
        else:
            print('All points have selected.  Press ESC-key.')

        if(ptlist.pos == ptlist.npoints):
            print(ptlist.ptlist[0][0])
            print(ptlist.ptlist[0][1])
            print(ptlist.ptlist[1][0])
            print(ptlist.ptlist[1][1])
            
            cv2.line(img, (ptlist.ptlist[0][0], ptlist.ptlist[0][1]),
                     (ptlist.ptlist[0][0], ptlist.ptlist[1][1]), (0, 255, 0), 3)
            cv2.line(img, (ptlist.ptlist[0][0], ptlist.ptlist[0][1]),
                     (ptlist.ptlist[1][0], ptlist.ptlist[0][1]), (0, 255, 0), 3)
            cv2.line(img, (ptlist.ptlist[1][0], ptlist.ptlist[0][1]),
                     (ptlist.ptlist[1][0], ptlist.ptlist[1][1]), (0, 255, 0), 3)
            cv2.line(img, (ptlist.ptlist[0][0], ptlist.ptlist[1][1]),
                     (ptlist.ptlist[1][0], ptlist.ptlist[1][1]), (0, 255, 0), 3)
        

        

wname = "hoge"
cv2.namedWindow( wname )
img = cv2.imread( "hoge.jpg" )
npoints = 2
ptlist = PointList(npoints)
cv2.setMouseCallback( wname, onMouse, [ wname, img, ptlist] )
cv2.imshow( wname, img )
while (True):
    #cv2.imshow("img", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cv2.waitKey() 
cv2.destroyAllWindows()
