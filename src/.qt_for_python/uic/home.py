# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Naorf\Documents\GitHub\Trivia-Game\src\Python-code\Home\home.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(850, 600)
        Form.setStyleSheet("QWidget{\n"
"background-color: rgb(54, 54, 54);\n"
"}")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(230, 130, 381, 101))
        self.label.setStyleSheet("font: 46pt \"Consolas\";\n"
"color: rgb(255, 255, 127);")
        self.label.setObjectName("label")
        self.playbutton = QtWidgets.QPushButton(Form)
        self.playbutton.setGeometry(QtCore.QRect(280, 270, 261, 41))
        self.playbutton.setStyleSheet("font: 26pt \"Consolas\";\n"
"color: rgb(255, 255, 0);\n"
"letter-spacing:2px;")
        self.playbutton.setObjectName("playbutton")
        self.scoretablbutton = QtWidgets.QPushButton(Form)
        self.scoretablbutton.setGeometry(QtCore.QRect(280, 330, 261, 41))
        self.scoretablbutton.setStyleSheet("font: 26pt \"Consolas\";\n"
"color: rgb(255, 255, 0);\n"
"letter-spacing:2px;")
        self.scoretablbutton.setObjectName("scoretablbutton")
        self.profilemenu = QtWidgets.QFrame(Form)
        self.profilemenu.setGeometry(QtCore.QRect(660, 20, 120, 81))
        self.profilemenu.setStyleSheet("border: 1px solid rgb(255, 255, 198);")
        self.profilemenu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.profilemenu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.profilemenu.setObjectName("profilemenu")
        self.profilebutton = QtWidgets.QPushButton(self.profilemenu)
        self.profilebutton.setGeometry(QtCore.QRect(20, 10, 75, 23))
        self.profilebutton.setStyleSheet("font: 10pt \"Consolas\";\n"
"color: rgb(255, 255, 0);\n"
"letter-spacing:1px;")
        self.profilebutton.setObjectName("profilebutton")
        self.settingbutton = QtWidgets.QPushButton(self.profilemenu)
        self.settingbutton.setGeometry(QtCore.QRect(20, 50, 75, 23))
        self.settingbutton.setStyleSheet("font: 10pt \"Consolas\";\n"
"color: rgb(255, 255, 0);\n"
"letter-spacing:1px;")
        self.settingbutton.setObjectName("settingbutton")
        self.shopbutton = QtWidgets.QLabel(Form)
        self.shopbutton.setGeometry(QtCore.QRect(790, 70, 51, 51))
        self.shopbutton.setStyleSheet("border: 1px solid rgb(255, 255, 198);\n"
"border-radius: 25px;\n"
"padding:2px;")
        self.shopbutton.setText("")
        self.shopbutton.setTextFormat(QtCore.Qt.RichText)
        self.shopbutton.setPixmap(QtGui.QPixmap("c:\\Users\\Naorf\\Documents\\GitHub\\Trivia-Game\\src\\Python-code\\Home\\shop.png"))
        self.shopbutton.setScaledContents(True)
        self.shopbutton.setObjectName("shopbutton")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(790, 10, 51, 51))
        self.label_2.setStyleSheet("border-radius: 25px;")
        self.label_2.setText("")
        self.label_2.setTextFormat(QtCore.Qt.RichText)
        self.label_2.setPixmap(QtGui.QPixmap("c:\\Users\\Naorf\\Documents\\GitHub\\Trivia-Game\\src\\Python-code\\Home\\user.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.profilelogo = QtWidgets.QPushButton(Form)
        self.profilelogo.setGeometry(QtCore.QRect(780, 10, 71, 51))
        self.profilelogo.setStyleSheet("background: transparent;")
        self.profilelogo.setText("")
        self.profilelogo.setObjectName("profilelogo")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Trivia Game"))
        self.playbutton.setText(_translate("Form", "Play Game"))
        self.scoretablbutton.setText(_translate("Form", "Score Table"))
        self.profilebutton.setText(_translate("Form", "profile"))
        self.settingbutton.setText(_translate("Form", "Settings"))
import user_rc
