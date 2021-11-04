# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qlty.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(961, 292)
        MainWindow.setStyleSheet("color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(300, 220, 351, 31))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(910, 40, 41, 33))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 50, 881, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(910, 80, 41, 33))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(910, 130, 41, 33))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 90, 881, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 130, 881, 21))
        self.label_7.setObjectName("label_7")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 131, 21))
        self.label_5.setObjectName("label_5")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_9.setGeometry(QtCore.QRect(110, 10, 161, 33))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 170, 881, 21))
        self.label_8.setObjectName("label_8")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_7.setGeometry(QtCore.QRect(910, 170, 41, 33))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-10, -200, 991, 681))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../Users/yuvar/Downloads/johannes-plenio-2TQwrtZnl08-unsplash.jpg"))
        self.label.setObjectName("label")
        self.label.raise_()
        self.pushButton.raise_()
        self.lineEdit_4.raise_()
        self.label_4.raise_()
        self.lineEdit_5.raise_()
        self.lineEdit_6.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_5.raise_()
        self.lineEdit_9.raise_()
        self.label_8.raise_()
        self.lineEdit_7.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Quality Factors"))
        self.pushButton.setText(_translate("MainWindow", "Store Quality Factors in Data base"))
        self.label_4.setText(_translate("MainWindow", "Autonomous body exists to deal with hardware quality control? ( 0 for No, 1 for Yes)"))
        self.label_6.setText(_translate("MainWindow", "Autonomous division exists to deal with software validation & verification? ( 0 for No, 1 for Yes)"))
        self.label_7.setText(_translate("MainWindow", "Ownership of problems properly defined?(0 for No, 1 for Yes)"))
        self.label_5.setText(_translate("MainWindow", "IOT_ ID:"))
        self.label_8.setText(_translate("MainWindow", "Ownership of different controls,properly defined?(0 for No, 1 for Yes)"))


