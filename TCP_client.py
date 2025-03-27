#-*- coding: UTF-8 -*-
import cv2
import time
import socket

# 服务端ip地址
HOST = '192.168.31.60'
# 服务端端口号
PORT = 5058
ADDRESS = (HOST, PORT)

# 创建一个套接字
tcpClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 连接远程ip
tcpClient.connect(ADDRESS)

def send_img(label):
    cv_image = cv2.imread('resource/frame.jpg')  # 读取图像
    img_encode = cv2.imencode('.jpg', cv_image, [cv2.IMWRITE_JPEG_QUALITY, 99])[1]  # 压缩图像
    byte_data = img_encode.tostring()  # 转换为字节流

    # 发送标签
    label_data = (str(label)).encode()
    tcpClient.send(label_data)
    data = tcpClient.recv(1024)

    # 标志数据，包括待发送的字节流长度等数据，用‘,’隔开
    flag_data = (str(len(byte_data))).encode() + ",".encode() + " ".encode()
    tcpClient.send(flag_data)
    # 接收服务端的应答
    data = tcpClient.recv(1024)
    if "ok" == data.decode():
        # 服务端已经收到标志数据，开始发送图像字节流数据
        tcpClient.send(byte_data)
    # 接收服务端的应答
    data = tcpClient.recv(1024)

while True:
    send_img(0)

