# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'match_module.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(492, 707)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.next_image = QtWidgets.QPushButton(self.centralwidget)
        self.next_image.setGeometry(QtCore.QRect(330, 610, 89, 25))
        self.next_image.setObjectName("next_image")
        self.last_image = QtWidgets.QPushButton(self.centralwidget)
        self.last_image.setGeometry(QtCore.QRect(60, 610, 89, 25))
        self.last_image.setObjectName("last_image")
        self.match = QtWidgets.QPushButton(self.centralwidget)
        self.match.setGeometry(QtCore.QRect(200, 610, 89, 25))
        self.match.setObjectName("match")
        self.image_object = QtWidgets.QLabel(self.centralwidget)
        self.image_object.setGeometry(QtCore.QRect(60, 20, 371, 551))
        self.image_object.setStyleSheet("background-color: rgb(136, 138, 133);")
        self.image_object.setText("")
        self.image_object.setObjectName("image_object")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 492, 28))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionopen_path = QtWidgets.QAction(MainWindow)
        self.actionopen_path.setObjectName("actionopen_path")
        self.actionopen_image = QtWidgets.QAction(MainWindow)
        self.actionopen_image.setObjectName("actionopen_image")
        self.chance_module = QtWidgets.QAction(MainWindow)
        self.chance_module.setObjectName("chance_module")
        self.menu.addAction(self.actionopen_path)
        self.menu.addAction(self.actionopen_image)
        self.menu_2.addAction(self.chance_module)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.next_image.setText(_translate("MainWindow", "下一张"))
        self.last_image.setText(_translate("MainWindow", "上一张"))
        self.match.setText(_translate("MainWindow", "match"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "模板"))
        self.actionopen_path.setText(_translate("MainWindow", "打开文件夹"))
        self.actionopen_image.setText(_translate("MainWindow", "打开文件"))
        self.chance_module.setText(_translate("MainWindow", "选择模板"))

