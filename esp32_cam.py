import urllib.request
import cv2
import numpy as np

cam0_url = 'http://192.168.31.21/cam-hi.jpg'
cam1_url = 'http://192.168.31.153/cam-hi.jpg'

def capture(cam_number, url):
    path = './resource/cams/cam' + str(cam_number) + '.jpg'
    imgResp = urllib.request.urlopen(url)
    imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8)
    img = cv2.imdecode(imgNp, -1)
    cv2.imwrite(path, img)
    return img

while True:
    img0 = capture(0, cam0_url)
    img1 = capture(1, cam1_url)

    cv2.imshow('test0', img0)
    cv2.imshow('test1', img1)
    if ord('q') == cv2.waitKey(10):
        exit(0)
