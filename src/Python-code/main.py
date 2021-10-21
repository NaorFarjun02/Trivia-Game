import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QDialog, QDesktopWidget, QWidget, QMessageBox

from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
from user import User
import socket
import threading

import random


windows_indexes = {
    "home": 0,
    "login": 1,
    "create": 2,
    "game": 3,
    "profile": 4,
    "scoretable": 5,
    "shop": 6,
    "settings": 27,
}

masteruser = User("1", "1", "1")
users = [masteruser]


def login_func(email, password):
    for user in users:
        if email == user.getEmail() and password == user.getPassword():
            return True, user
    return False, None


class Home(QDialog):
    def __init__(self):
        super(Home, self).__init__()
        loadUi("Home\home.ui", self)
        self.profilemenu.hide()
        self.profilelogo.clicked.connect(self.show_profile_menu)

    def show_profile_menu(self):
        if self.profilemenu.isHidden():
            self.profilemenu.show()
        else:
            self.profilemenu.hide()


class Login(QDialog):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("Login\login.ui", self)

        self.loginbutton.clicked.connect(self.login_func)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccountbutton.clicked.connect(self.go_to_create)

    def login_func(self):
        email = self.email.text()
        password = self.password.text()
        login_status, user = login_func(self.email.text(), self.password.text())
        if login_status == True:
            print(
                "\nSuccessfully Logged in \nEmail: %s\nPassword: %s" % (email, password)
            )
        else:
            print("Cen't connect to the server")

    def go_to_create(self):
        widget.setCurrentIndex(windows_indexes["create"])


class CreateAcount(QDialog):
    def __init__(self):
        super(CreateAcount, self).__init__()
        loadUi("Create-account\createaccount.ui", self)

        self.singupbutton.clicked.connect(self.create_account_func)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)

    def create_account_func(self):
        email = self.email.text()
        username = self.username.text()
        if self.password.text() == self.confirmpass.text():
            password = self.password.text()

            new_user = User(
                self.email.text(), self.username.text(), self.password.text()
            )
            users.append(new_user)
            print(
                "\nSuccessfully Created account \nEmail: %s\nPassword: %s"
                % (email, password)
            )
            widget.setCurrentIndex(windows_indexes["login"])


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()

home = Home()
widget.insertWidget(windows_indexes["home"], home)

login = Login()
widget.insertWidget(windows_indexes["login"], login)

create_account = CreateAcount()
widget.insertWidget(windows_indexes["create"], create_account)

widget.setCurrentIndex(0)
widget.setFixedWidth(850)
widget.setFixedHeight(600)
widget.show()
app.exec_()
