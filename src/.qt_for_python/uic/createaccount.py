# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Naorf\Documents\GitHub\Trivia-Game\src\Python-code\Create-account\createaccount.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_createaccount(object):
    def setupUi(self, createaccount):
        createaccount.setObjectName("createaccount")
        createaccount.resize(450, 500)
        createaccount.setStyleSheet("background-color: rgb(54, 54, 54);")
        self.label = QtWidgets.QLabel(createaccount)
        self.label.setGeometry(QtCore.QRect(160, 60, 101, 41))
        self.label.setStyleSheet("color: rgb(223, 223, 223);\n"
"font-size:28px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(createaccount)
        self.label_2.setGeometry(QtCore.QRect(20, 130, 51, 31))
        self.label_2.setStyleSheet("font-size:20px;\n"
"color: rgb(255, 170, 0);")
        self.label_2.setObjectName("label_2")
        self.email = QtWidgets.QLineEdit(createaccount)
        self.email.setGeometry(QtCore.QRect(140, 130, 220, 33))
        self.email.setStyleSheet("padding:5px;\n"
"border:2px solid rgb(26, 26, 26);\n"
"border-radius:15px;\n"
"font-size:15px;\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(117, 117, 117);")
        self.email.setObjectName("email")
        self.label_3 = QtWidgets.QLabel(createaccount)
        self.label_3.setGeometry(QtCore.QRect(20, 251, 81, 31))
        self.label_3.setStyleSheet("font-size:20px;\n"
"color: rgb(255, 170, 0);")
        self.label_3.setObjectName("label_3")
        self.password = QtWidgets.QLineEdit(createaccount)
        self.password.setGeometry(QtCore.QRect(140, 250, 220, 33))
        self.password.setStyleSheet("padding:5px;\n"
"background-color: rgb(117, 117, 117);\n"
"color: rgb(255, 255, 255);\n"
"border:2px solid rgb(26, 26, 26);\n"
"border-radius:15px;\n"
"font-size:15px;")
        self.password.setObjectName("password")
        self.singupbutton = QtWidgets.QPushButton(createaccount)
        self.singupbutton.setGeometry(QtCore.QRect(150, 380, 150, 35))
        self.singupbutton.setStyleSheet("padding:5px;\n"
"border:2px solid rgb(26, 26, 26);\n"
"border-radius:15px;\n"
"font-size:17px;\n"
"background-color: rgb(255, 204, 0);")
        self.singupbutton.setObjectName("singupbutton")
        self.label_4 = QtWidgets.QLabel(createaccount)
        self.label_4.setGeometry(QtCore.QRect(18, 311, 111, 31))
        self.label_4.setStyleSheet("font-size:19px;\n"
"color: rgb(255, 170, 0);")
        self.label_4.setObjectName("label_4")
        self.confirmpass = QtWidgets.QLineEdit(createaccount)
        self.confirmpass.setGeometry(QtCore.QRect(140, 310, 220, 33))
        self.confirmpass.setStyleSheet("padding:5px;\n"
"background-color: rgb(117, 117, 117);\n"
"color: rgb(255, 255, 255);\n"
"border:2px solid rgb(26, 26, 26);\n"
"border-radius:15px;\n"
"font-size:15px;")
        self.confirmpass.setObjectName("confirmpass")
        self.label_5 = QtWidgets.QLabel(createaccount)
        self.label_5.setGeometry(QtCore.QRect(18, 191, 111, 31))
        self.label_5.setStyleSheet("font-size:19px;\n"
"color: rgb(255, 170, 0);")
        self.label_5.setObjectName("label_5")
        self.username = QtWidgets.QLineEdit(createaccount)
        self.username.setGeometry(QtCore.QRect(140, 190, 220, 33))
        self.username.setStyleSheet("padding:5px;\n"
"background-color: rgb(117, 117, 117);\n"
"color: rgb(255, 255, 255);\n"
"border:2px solid rgb(26, 26, 26);\n"
"border-radius:15px;\n"
"font-size:15px;")
        self.username.setText("")
        self.username.setObjectName("username")

        self.retranslateUi(createaccount)
        QtCore.QMetaObject.connectSlotsByName(createaccount)

    def retranslateUi(self, createaccount):
        _translate = QtCore.QCoreApplication.translate
        createaccount.setWindowTitle(_translate("createaccount", "Create Accont"))
        self.label.setText(_translate("createaccount", "Sing Up"))
        self.label_2.setText(_translate("createaccount", "Email:"))
        self.label_3.setText(_translate("createaccount", "Pasword"))
        self.singupbutton.setText(_translate("createaccount", "Sing Up"))
        self.label_4.setText(_translate("createaccount", "Confirm Pass"))
        self.label_5.setText(_translate("createaccount", "Username"))
