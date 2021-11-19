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
import re


windows_indexes = {
    "home": 0,
    "login": 1,
    "create": 2,
    "game": 3,
    "profile": 4,
    "scoretable": 5,
    "shop": 6,
    "settings": 27,
}  # A list of all the indexes of each page
global LOGIN_STATUS  # user login status
LOGIN_STATUS = 0

masteruser = User("81102", "81102", "81102")
users = [masteruser]


def login_func(email, password):
    """login function

    Args:
        email (string): user email
        password (string): user password

    Returns:
        bool_1: If the user exists
        bool_2: User information if it does exist
    """
    for user in users:
        if email == user.getEmail() and password == user.getPassword():
            return True, user
    return False, None


def create_msgbox(title, text):
    """create msg box

    Args:
        title (string): the msg title
        text (string): the info of the msg
    """
    msg = QMessageBox()
    msg.setWindowTitle(title)
    msg.setText(text)
    x = msg.exec_()


class Home(QDialog):
    def __init__(self):
        """init function that set al the main stuff of th page like UI and clicked event"""
        super(Home, self).__init__()
        loadUi("Home\home.ui", self)  # load the UI of the page
        self.menu.hide()  # hide the side menu
        self.menubutton.clicked.connect(
            self.show_menu
        )  # click event to the menu button

        self.profilebutton.clicked.connect(
            self.profile
        )  # click event to the profile button in the menu
        self.shopbutton.clicked.connect(
            self.shop
        )  # click event to the shop button in the menu
        self.settingbutton.clicked.connect(
            self.setting
        )  # click event to the setting button in the menu

    def show_menu(self):
        if self.menu.isHidden():
            self.menu.show()
        else:
            self.menu.hide()

    def profile(self):
        global LOGIN_STATUS
        if LOGIN_STATUS == 0:
            print("you need to login first")
            self.menu.hide()  # hide the side menu
            widget.setCurrentIndex(windows_indexes["login"])
        elif LOGIN_STATUS == 1:
            print("profile")

    def shop(self):
        print("shop")

    def setting(self):
        print("setting")


class Login(QDialog):
    def __init__(self):
        """init function that set al the main stuff of th page like UI and clicked event"""
        super(Login, self).__init__()
        loadUi("Login\login.ui", self)  # load the UI of the page

        self.loginbutton.clicked.connect(self.login_func)  # click event to login button
        self.password.setEchoMode(
            QtWidgets.QLineEdit.Password
        )  # set the password view to dots
        self.createaccountbutton.clicked.connect(
            self.go_to_create
        )  # click event on the create account text
        self.backbutton.clicked.connect(self.back_to_home)  # click event to back button

    def login_func(self):
        email = self.email.text()
        password = self.password.text()
        global LOGIN_STATUS
        login_status, user = login_func(
            self.email.text(), self.password.text()
        )  # check if the user is exists
        if login_status == True:
            # if the user is exists so he login and go to the profile page
            print(
                "\n\nSuccessfully Logged in \nEmail: %s\nPassword: %s\n\n"
                % (email, password)
            )
            LOGIN_STATUS = 1
            widget.setCurrentIndex(windows_indexes["home"])
        else:
            # if the user is don't exists, msg box tell the user that something wrong
            create_msgbox("error", "Username or password incorrect")
            print("Cen't connect to the server")

    def go_to_create(self):
        widget.setCurrentIndex(windows_indexes["create"])

    def back_to_home(self):
        widget.setCurrentIndex(windows_indexes["home"])


class CreateAcount(QDialog):
    def __init__(self):
        """init function that set al the main stuff of th page like UI and clicked event"""
        super(CreateAcount, self).__init__()
        loadUi("Create-account\createaccount.ui", self)  # load the UI of the page

        self.singupbutton.clicked.connect(
            self.create_account_func
        )  # click event to sungup button
        self.password.setEchoMode(
            QtWidgets.QLineEdit.Password
        )  # set the password view to dots
        self.confirmpass.setEchoMode(
            QtWidgets.QLineEdit.Password
        )  # set the password view to dots
        self.backbutton.clicked.connect(
            self.back_to_login
        )  # click event to back button

    def create_account_func(self):
        if (
            self.email.text() == ""
            or self.username.text() == ""
            or self.password.text() == ""
            or self.confirmpass.text() == ""
        ):
            create_msgbox("error", "Please fill in all the cells")
            return
        email = self.email.text()
        username = self.username.text()
        self.check_password()
        
    def check_password(self):
        if self.password.text() == self.confirmpass.text():
            password = self.password.text()
            if len(password)<8 or len(password)>16:
                create_msgbox("password-error", "the password mast by between 8 to 16 chars")
                return
            elif len(re.findall("[a-z]", password))<1 or len(re.findall("[A-Z]", password))<1 :
                create_msgbox("password-error", "the password most includ a uppercase letters and lowercase letters in English")
                return
            elif len(re.findall("[0-9]", password))<2:
                create_msgbox("password-error", "the password most includ a digits") 
                return               
            new_user = User(
                self.email.text(), self.username.text(), self.password.text()
            )
            users.append(new_user)
            print(
                "\n\nSuccessfully Created account \nEmail: %s\nPassword: %s\n\n"
                % (self.email.text(), self.password.text())
            )
            widget.setCurrentIndex(windows_indexes["login"])
        else:
            create_msgbox("error", "The passwords do not match")
            return
    def back_to_login(self):
        widget.setCurrentIndex(windows_indexes["login"])


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()

home = Home()  # home page
widget.insertWidget(windows_indexes["home"], home)

login = Login()  # login page
widget.insertWidget(windows_indexes["login"], login)

create_account = CreateAcount()  # create account page
widget.insertWidget(windows_indexes["create"], create_account)

# login = Login()#login page
# widget.insertWidget(windows_indexes["login"], login)

widget.setCurrentIndex(0)
widget.setFixedWidth(850)
widget.setFixedHeight(600)
widget.show()
app.exec_()
