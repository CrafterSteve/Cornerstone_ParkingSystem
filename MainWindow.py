# Form implementation generated from reading ui file 'ParkingSystem.ui'
#
# Created by: PyQt6 UI code generator 6.5.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import time
import threading
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
import TCP_server as server


class Ui_ParkingSystem(object):
    def setupUi(self, ParkingSystem):
        ParkingSystem.setObjectName("ParkingSystem")
        ParkingSystem.resize(811, 609)
        self.centralwidget = QtWidgets.QWidget(parent=ParkingSystem)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(181, 181, 181);\n"
                                 "border-radius: 8px;")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(parent=self.frame)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 141, 521))
        self.frame_2.setStyleSheet("QFrame#frame_2{\n"
                                   "    background-color: rgba(255, 255, 255, 255);\n"
                                   "    border-radius:10px;\n"
                                   "}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(parent=self.frame_2)
        self.label.setGeometry(QtCore.QRect(10, 30, 71, 16))
        font = QtGui.QFont()
        font.setFamily(".AppleSystemUIFont")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);\n"
                                 "font: 18pt \".AppleSystemUIFont\";\n"
                                 "background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(parent=self.frame_2)
        self.progressBar.setGeometry(QtCore.QRect(10, 80, 118, 23))
        self.progressBar.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_2 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 60, 60, 16))
        self.label_2.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "background-color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(10, 300, 81, 16))
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "background-color: rgb(255, 255, 255);\n"
                                   "font: 18pt \".AppleSystemUIFont\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 41, 16))
        self.label_4.setStyleSheet("color: rgb(0, 0, 0);\n"
                                   "background-color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.frame1 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame1.setGeometry(QtCore.QRect(10, 330, 121, 181))
        self.frame1.setObjectName("frame1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame1)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.MapOverview_btn = QtWidgets.QPushButton(parent=self.frame1)
        self.MapOverview_btn.setEnabled(True)
        self.MapOverview_btn.setStyleSheet("QPushButton{\n"
                                           "    color: rgb(255, 255, 255);\n"
                                           "    background-color: rgba(200, 200, 200, 200);\n"
                                           "    border-radius: 8px;\n"
                                           "}")
        self.MapOverview_btn.setCheckable(False)
        self.MapOverview_btn.setAutoDefault(False)
        self.MapOverview_btn.setFlat(False)
        self.MapOverview_btn.setObjectName("MapOverview_btn")
        self.verticalLayout.addWidget(self.MapOverview_btn)
        self.CameraView_btn = QtWidgets.QPushButton(parent=self.frame1)
        self.CameraView_btn.setStyleSheet("QPushButton{\n"
                                          "    color: rgb(255, 255, 255);\n"
                                          "    background-color: rgba(200, 200, 200, 200);\n"
                                          "    border-radius: 8px;\n"
                                          "}")
        self.CameraView_btn.setObjectName("CameraView_btn")
        self.verticalLayout.addWidget(self.CameraView_btn)
        self.Storage_btn = QtWidgets.QPushButton(parent=self.frame1)
        self.Storage_btn.setStyleSheet("QPushButton{\n"
                                       "    color: rgb(255, 255, 255);\n"
                                       "    background-color: rgba(200, 200, 200, 200);\n"
                                       "    border-radius: 8px;\n"
                                       "}")
        self.Storage_btn.setObjectName("Storage_btn")
        self.verticalLayout.addWidget(self.Storage_btn)
        self.Settings_btn = QtWidgets.QPushButton(parent=self.frame1)
        self.Settings_btn.setStyleSheet("QPushButton{\n"
                                        "    color: rgb(255, 255, 255);\n"
                                        "    background-color: rgba(200, 200, 200, 200);\n"
                                        "    border-radius: 8px;\n"
                                        "}")
        self.Settings_btn.setObjectName("Settings_btn")
        self.verticalLayout.addWidget(self.Settings_btn)
        self.frame_3 = QtWidgets.QFrame(parent=self.frame)
        self.frame_3.setGeometry(QtCore.QRect(160, 10, 601, 61))
        self.frame_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                   "border-radius: 8px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")

        self.PortName = QtWidgets.QLabel(parent=self.frame_3)
        self.PortName.setGeometry(QtCore.QRect(30, 20, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(24)
        font.setBold(True)
        self.PortName.setFont(font)
        self.PortName.setObjectName("PortName")

        self.frame_4 = QtWidgets.QFrame(parent=self.frame)
        self.frame_4.setGeometry(QtCore.QRect(160, 80, 601, 451))
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.frame_4)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 581, 431))
        self.stackedWidget.setObjectName("stackedWidget")
        self.Map = QtWidgets.QWidget()
        self.Map.setObjectName("Map")
        self.label_5 = QtWidgets.QLabel(parent=self.Map)
        self.label_5.setGeometry(QtCore.QRect(-10, 0, 601, 431))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("resource/MapOverview.jpeg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.stackedWidget.addWidget(self.Map)
        self.Cam = QtWidgets.QWidget()
        self.Cam.setObjectName("Cam")
        self.label_7 = QtWidgets.QLabel(parent=self.Cam)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 271, 171))
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap("yolo_detect/resource/img_frame/frame.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(parent=self.Cam)
        self.label_8.setGeometry(QtCore.QRect(300, 30, 271, 171))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("yolo_detect/resource/img_frame/frame.jpg"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(parent=self.Cam)
        self.label_9.setGeometry(QtCore.QRect(10, 220, 271, 171))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("yolo_detect/resource/img_frame/frame.jpg"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(parent=self.Cam)
        self.label_10.setGeometry(QtCore.QRect(300, 220, 271, 171))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("yolo_detect/resource/img_frame/frame.jpg"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.stackedWidget.addWidget(self.Cam)
        self.Storage = QtWidgets.QWidget()
        self.Storage.setObjectName("Storage")
        self.label_12 = QtWidgets.QLabel(parent=self.Storage)
        self.label_12.setGeometry(QtCore.QRect(230, 200, 221, 21))
        self.label_12.setObjectName("label_12")
        self.stackedWidget.addWidget(self.Storage)
        self.Settings = QtWidgets.QWidget()
        self.Settings.setObjectName("Settings")
        self.label_11 = QtWidgets.QLabel(parent=self.Settings)
        self.label_11.setGeometry(QtCore.QRect(270, 200, 58, 16))
        self.label_11.setObjectName("label_11")
        self.stackedWidget.addWidget(self.Settings)
        self.horizontalLayout.addWidget(self.frame)
        ParkingSystem.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(parent=ParkingSystem)
        self.statusbar.setObjectName("statusbar")
        ParkingSystem.setStatusBar(self.statusbar)

        self.retranslateUi(ParkingSystem)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(ParkingSystem)

        # Button assignment
        self.MapOverview_btn.clicked.connect(self.Btn1_response)
        self.CameraView_btn.clicked.connect(self.Btn2_response)
        self.Storage_btn.clicked.connect(self.Btn3_response)
        self.Settings_btn.clicked.connect(self.Btn4_response)

    def retranslateUi(self, ParkingSystem):
        _translate = QtCore.QCoreApplication.translate
        ParkingSystem.setWindowTitle(_translate("ParkingSystem", "MainWindow"))
        self.label.setText(_translate("ParkingSystem", "Abstract"))
        self.label_2.setText(_translate("ParkingSystem", "Capacity:"))
        self.label_3.setText(_translate("ParkingSystem", "View Ports"))
        self.label_4.setText(_translate("ParkingSystem", "Total: "))
        self.MapOverview_btn.setText(_translate("ParkingSystem", "Map Overview"))
        self.CameraView_btn.setText(_translate("ParkingSystem", "Camera View"))
        self.Storage_btn.setText(_translate("ParkingSystem", "Storage"))
        self.Settings_btn.setText(_translate("ParkingSystem", "Settings"))
        self.PortName.setText(_translate("ParkingSystem", "Port Name"))
        self.label_12.setText(_translate("ParkingSystem", "Storage management"))
        self.label_11.setText(_translate("ParkingSystem", "Settings"))

    # added func
    def Btn1_response(self):
        self.stackedWidget.setCurrentIndex(0)
        self.PortName.setText("Map Overview")
        self.PortName.adjustSize()

    def Btn2_response(self):
        self.stackedWidget.setCurrentIndex(1)
        self.PortName.setText("Camera View")
        self.PortName.adjustSize()

    def Btn3_response(self):
        self.stackedWidget.setCurrentIndex(2)
        self.PortName.setText("Storage")
        self.PortName.adjustSize()

    def Btn4_response(self):
        self.stackedWidget.setCurrentIndex(3)
        self.PortName.setText("Settings")
        self.PortName.adjustSize()

    def refresh(self):
        while True:
            try:
                self.label_7.setPixmap(QtGui.QPixmap("resource/cams/cam0.jpg"))
                self.label_8.setPixmap(QtGui.QPixmap("resource/cams/cam1.jpg"))
                self.label_9.setPixmap(QtGui.QPixmap("resource/cam_not_available.jpeg"))
                self.label_10.setPixmap(QtGui.QPixmap("resource/cam_not_available.jpeg"))
            except:
                pass
            time.sleep(0.2)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ParkingSystem = QtWidgets.QMainWindow()
    ui = Ui_ParkingSystem()
    ui.setupUi(ParkingSystem)
    threads = True
    thread_refresh = threading.Thread(target=ui.refresh)
    thread_server = threading.Thread(target=server.start_server, args=(threads,))
    thread_refresh.start()
    thread_server.start()
    ParkingSystem.show()
    sys.exit(app.exec())


