import sys
import cv2
import os
import numpy as np

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QDockWidget, QListWidget, QInputDialog, QLineEdit
from PyQt5.QtGui import *

from qt5_source.match_module import Ui_MainWindow  # 导入创建的GUI类

# from qt5_opencv import *

class mywindow(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

        self.image_list = []
        self.image_index = -1

        self.module_path = []

        # 自适应此尺寸
        self.image_object.setScaledContents(True)
        #开启鼠标跟踪
        # self.image_object.setMouseTracking(True)

        #打开图片，同事显示
        self.actionopen_image.triggered.connect(self.open_image)
        #打开文件夹，显示第一张图片
        self.actionopen_path.triggered.connect(self.open_path)

        #选择一个模板
        self.chance_module.triggered.connect(self.get_module_path)

        #图片的切换
        self.next_image.clicked.connect(self.get_next_image)
        self.last_image.clicked.connect(self.get_last_image)

        #执行匹配
        self.match.clicked.connect(self.get_match_result)


    def show_image(self):
        Im = cv2.imread(self.image_list[self.image_index])  # 通过Opencv读入一张图片
        image_height, image_width, image_depth = Im.shape  # 获取图像的高，宽以及深度。
        QIm = cv2.cvtColor(Im, cv2.COLOR_BGR2RGB)  # opencv读图片是BGR，qt显示要RGB，所以需要转换一下
        QIm = QImage(QIm.data, image_width, image_height,  # 创建QImage格式的图像，并读入图像信息
                     image_width * image_depth,
                     QImage.Format_RGB888)
        self.image_object.setPixmap(QPixmap.fromImage(QIm))  # 将QImage显示在之前创建的QLabel控件中

    def open_path(self):
        # QMessageBox.information(self, 'Information', '提示消息')
        directory = QFileDialog.getExistingDirectory(self,
                                                     "选取文件夹", None)  # 打开路径为xx，若不指定路径，默认打开当前py文件所在文件夹
        self.image_list = [os.path.join(p, fi) for p, n, f in os.walk(directory) for fi in f]
        print(self.image_list)
        self.image_index = 0
        self.show_image()

    def open_image(self):
        fileName, filetype = QFileDialog.getOpenFileName(self,
                                                        "选取文件",
                                                        "C:/",
                                                        "Image Files (*.bmp);;Text Files (*.txt)")  # 设置文件扩展名过滤,
        # 注意用双分号间隔
        self.image_list = [fileName]
        self.image_index = 0
        self.show_image()

    def get_module_path(self):
        directory = QFileDialog.getExistingDirectory(self, '选取模板文件夹', None)
        self.module_path = directory
        print(os.listdir(self.module_path))


    def get_next_image(self):
        self.image_index = (self.image_index+1)%len(self.image_list)
        self.show_image()

    def get_last_image(self):
        self.image_index = (self.image_index - 1) % len(self.image_list)
        self.show_image()


    # def mousePressEvent(self, a0: QtGui.QMouseEvent):  # 鼠标点击事件
    #         if a0.button() == Qt.LeftButton:  # 按下鼠标左键
    #             img = cv2.imread(self.image_list[self.image_index], flags=cv2.IMREAD_COLOR)
    #             bbox = cv2.selectROI(img, False)
    #             cut = img[bbox[1]:bbox[1] + bbox[3], bbox[0]:bbox[0] + bbox[2]]
    #             value, ok = QInputDialog.getText(self, "输入框标题", "这是提示信息\n\n请输入模板名字:", QLineEdit.Normal, "0")
    #             if len(self.module_path) != 0:
    #                 cv2.imwrite(self.module_path + str(value) + '.jpg', cut)
    #             print(bbox)
    #         if a0.button() == Qt.RightButton:  # 按下鼠标右键
    #             print('youjian')
    #         # do something
    #         if a0.button() == Qt.MidButton:  # 按下鼠标中间
    #             print('zhongjian')
    #     # do something

    def get_match_result(self):
        #读入显示的图片
        img_rgb = cv2.imread(self.image_list[self.image_index])
        img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

        #循环匹配模板
        print('match test')
        print(self.module_path)
        for imgi in os.listdir(self.module_path):

            print(imgi)
            template = cv2.imread(os.path.join(self.module_path, imgi), 0)
            w, h = template.shape[::-1]
            res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
            threshold = 0.80
            loc = np.where(res >= threshold)
            print(imgi[:-4])

            for pt in zip(*loc[::-1]):
                print(pt)
                cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)
        self.show_match_image(img_rgb)


    def show_match_image(self, image):
        Im = image  # 通过Opencv读入一张图片
        image_height, image_width, image_depth = Im.shape  # 获取图像的高，宽以及深度。
        QIm = cv2.cvtColor(Im, cv2.COLOR_BGR2RGB)  # opencv读图片是BGR，qt显示要RGB，所以需要转换一下
        QIm = QImage(QIm.data, image_width, image_height,  # 创建QImage格式的图像，并读入图像信息
                     image_width * image_depth,
                     QImage.Format_RGB888)
        self.image_object.setPixmap(QPixmap.fromImage(QIm))  # 将QImage显示在之前创建的QLabel控件中


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = mywindow()
    window.show()
    sys.exit(app.exec_())
