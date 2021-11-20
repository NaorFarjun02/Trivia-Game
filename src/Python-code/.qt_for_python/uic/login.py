# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Naorf\Documents\GitHub\Trivia-Game\src\Python-code\Login\login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(850, 600)
        Login.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.label = QtWidgets.QLabel(Login)
        self.label.setGeometry(QtCore.QRect(370, 130, 121, 61))
        self.label.setStyleSheet("color: rgb(223, 223, 223);\n"
"font-size:50px;")
        self.label.setObjectName("label")
        self.username = QtWidgets.QLineEdit(Login)
        self.username.setGeometry(QtCore.QRect(320, 230, 220, 33))
        self.username.setStyleSheet("padding:5px;\n"
"border:2px solid rgb(26, 26, 26);\n"
"border-radius:15px;\n"
"font-size:15px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(117, 117, 117);")
        self.username.setInputMask("")
        self.username.setText("")
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(Login)
        self.password.setGeometry(QtCore.QRect(320, 300, 220, 33))
        self.password.setStyleSheet("padding:5px;\n"
"background-color: rgb(117, 117, 117);\n"
"color: rgb(255, 255, 255);\n"
"border:2px solid rgb(26, 26, 26);\n"
"border-radius:15px;\n"
"font-size:15px;")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.loginbutton = QtWidgets.QPushButton(Login)
        self.loginbutton.setGeometry(QtCore.QRect(330, 350, 200, 35))
        self.loginbutton.setStyleSheet("padding:5px;\n"
"border:2px solid rgb(26, 26, 26);\n"
"border-radius:15px;\n"
"font-size:17px;\n"
"background-color: rgb(255, 204, 0);")
        self.loginbutton.setCheckable(False)
        self.loginbutton.setObjectName("loginbutton")
        self.createaccountbutton = QtWidgets.QPushButton(Login)
        self.createaccountbutton.setGeometry(QtCore.QRect(340, 390, 181, 23))
        self.createaccountbutton.setStyleSheet("color: rgb(254, 204, 0);\n"
"border:none;\n"
"")
        self.createaccountbutton.setObjectName("createaccountbutton")
        self.arrowback_label = QtWidgets.QLabel(Login)
        self.arrowback_label.setGeometry(QtCore.QRect(20, 20, 51, 51))
        self.arrowback_label.setStyleSheet("\n"
"background-color: rgb(65, 65, 65);\n"
"border-radius:25px;\n"
"border:1px solid rgb(255, 255, 127);\n"
"")
        self.arrowback_label.setText("")
        self.arrowback_label.setTextFormat(QtCore.Qt.PlainText)
        self.arrowback_label.setPixmap(QtGui.QPixmap("c:\\Users\\Naorf\\Documents\\GitHub\\Trivia-Game\\src\\Python-code\\Login\\../icons/arrow-left.png"))
        self.arrowback_label.setScaledContents(True)
        self.arrowback_label.setObjectName("arrowback_label")
        self.backbutton = QtWidgets.QPushButton(Login)
        self.backbutton.setGeometry(QtCore.QRect(20, 20, 61, 51))
        self.backbutton.setStyleSheet("border:1px;\n"
"background: transparent;")
        self.backbutton.setText("")
        self.backbutton.setObjectName("backbutton")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Login"))
        self.label.setText(_translate("Login", "Login"))
        self.username.setPlaceholderText(_translate("Login", "Username"))
        self.password.setPlaceholderText(_translate("Login", "Password"))
        self.loginbutton.setText(_translate("Login", "Login"))
        self.createaccountbutton.setText(_translate("Login", "Don\'t have an account? Create one"))
import arrow_rc
import shop_rc
import user_rc
