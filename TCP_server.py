#-*- coding: UTF-8 -*-
import socket
import time
import sys
import cv2
import numpy as np
from yolo_detect import detect

def start_server(threads):
    HOST = '192.168.31.60'
    PORT = 5065
    ADDRESS = (HOST, PORT)
    tcpServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcpServer.bind(ADDRESS)
    tcpServer.listen(5)

    while threads:
        print("等待连接……")
        client_socket, client_address = tcpServer.accept()
        print("Camera连接成功！")
        time.sleep(0.2)
        client_socket.send(b"ok")
        dis_socket, dis_address = tcpServer.accept()
        print("Display连接成功！")
        time.sleep(0.2)
        dis_socket.send(b"ok")
        try:
            while True:
                start = time.perf_counter()

                # 接收标志数据
                data = client_socket.recv(1024)
                if data:
                    # 通知客户端“已收到标志数据，可以发送图像数据”
                    client_socket.send(b"ok")
                    # 处理标志数据
                    flag = data.decode().split(",")
                    # 图像标签
                    label = int(flag[0])
                    print(f"label {label} received")
                    # 图像字节流数据的总长度
                    total = int(flag[1])
                    # 接收到的数据计数
                    cnt = 0
                    # 存放接收到的数据
                    img_bytes = b""

                    while cnt < total:
                        # 当接收到的数据少于数据总长度时，则循环接收图像数据，直到接收完毕
                        data = client_socket.recv(256000)
                        img_bytes += data
                        if not data:
                            break
                        cnt += len(data)
                        print("receive:" + str(cnt) + "/" + flag[0])

                    # 解析接收到的字节流数据
                    img = np.asarray(bytearray(img_bytes), dtype="uint8")
                    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
                    cv2.imwrite('./yolo_detect/resource/img_frame/frame_raw.jpg', img)

                    # 处理图像
                    opt = detect.parse_opt()
                    img = detect.main(opt)

                    dis_socket.send(str(int((time.perf_counter() - start)*1000)).encode('utf-8'))

                    # 显示图像
                    # img = cv2.imread('./yolo_detect/resource/img_frame/frame.jpg')
                    # cv2.imshow("img", img)
                    # time.sleep(0.2)

                    # 图像分流
                    img_stream = cv2.imread("yolo_detect/resource/img_frame/frame.jpg")
                    cam_path = "./resource/cams/cam" + str(label) + ".jpg"
                    cv2.imwrite(cam_path, img_stream)

                    # 通知客户端“已经接收完毕，可以开始下一帧图像的传输”
                    client_socket.send(b"ok")

                else:
                    print("已断开！")
                    break
        finally:
            client_socket.close()
