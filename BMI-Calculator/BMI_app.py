# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BMI_app.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *


class Ui_window(object):
    def setupUi(self, window):
        
        window.setObjectName("window")
        window.resize(420, 287)
        
        
        self.label = QtWidgets.QLabel(window)
        self.label.setGeometry(QtCore.QRect(50, 100, 58, 14))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(window)
        self.label_2.setGeometry(QtCore.QRect(50, 140, 58, 14))
        self.label_2.setObjectName("label_2")
        
        self.WightInput = QtWidgets.QLineEdit(window)
        self.WightInput.setGeometry(QtCore.QRect(110, 100, 251, 24))
        self.WightInput.setPlaceholderText("50 Kg")
        self.WightInput.setObjectName("WightInput")
        
        self.HeightInput = QtWidgets.QLineEdit(window)
        self.HeightInput.setGeometry(QtCore.QRect(110, 140, 251, 24))
        self.HeightInput.setPlaceholderText("1.70 Cm")
        self.HeightInput.setObjectName("HeightInput")
        
        self.CountButton = QtWidgets.QPushButton(window)
        self.CountButton.setGeometry(QtCore.QRect(270, 170, 88, 27))
        self.CountButton.setObjectName("CountButton")
        
        self.label_3 = QtWidgets.QLabel(window)
        self.label_3.setGeometry(QtCore.QRect(50, 210, 58, 14))
        self.label_3.setObjectName("label_3")
        
        self.InputResult = QtWidgets.QLineEdit(window)
        self.InputResult.setGeometry(QtCore.QRect(110, 210, 251, 24))
        self.InputResult.setPlaceholderText("your Weight is : Under Weight ")
        self.InputResult.setObjectName("InputResult")
        
        self.frame = QtWidgets.QFrame(window)
        self.frame.setGeometry(QtCore.QRect(20, 70, 371, 191))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.frame_2 = QtWidgets.QFrame(window)
        self.frame_2.setGeometry(QtCore.QRect(20, 20, 371, 41))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(30, 10, 301, 20))
        
        font = QtGui.QFont()
        font.setFamily("Tlwg Mono")
        font.setBold(True)
        font.setWeight(75)
        
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.frame.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.WightInput.raise_()
        self.HeightInput.raise_()
        self.CountButton.raise_()
        self.label_3.raise_()
        self.InputResult.raise_()
        self.frame_2.raise_()

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)
        
        self.CountButton.clicked.connect(self.on_clicked)

    def retranslateUi(self, window):
        _translate = QtCore.QCoreApplication.translate
        window.setWindowTitle(_translate("window", "Calculate Your BMI"))
        self.label.setText(_translate("window", "Weight :"))
        self.label_2.setText(_translate("window", "Height :"))
        self.CountButton.setText(_translate("window", "Count"))
        self.label_3.setText(_translate("window", "Result :"))
        self.label_4.setText(_translate("window", "Calculate Your BMI - Body Mass Index"))
        
    
    def on_clicked(self):
        Weight = self.WightInput.text()
        Height = self.HeightInput.text()
        count = float(Weight) / float(Height)**2
        count = round(count,1)
        #logic 
        if (count <= 18.5):
            self.InputResult.setText("under weight")
        elif (18.5<count<=25):
            self.InputResult.setText("normal weight")
        elif(25<count<=29.9):
            self.InputResult.setText("over height")
        else:
            self.InputResult.setText("Obesity")
            self.InputResult.setStyleSheet("color:red;")



