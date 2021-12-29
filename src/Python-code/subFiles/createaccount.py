from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QDialog, QDesktopWidget, QWidget, QMessageBox
from PyQt5.uic import loadUi
from module import global_vers, client,chatlib
from module.user import User
from datetime import datetime

import re


class CreateAcount(QDialog):
    def __init__(self, widget):
        """init function that set al the main stuff of th page like UI and clicked event"""
        super(CreateAcount, self).__init__()
        loadUi("UI\createaccount.ui", self)  # load the UI of the page
        self.widget = widget

        self.confirmpass.returnPressed.connect(
            self.create_account_func
        )  # enter event to confirmed password filed
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
        """
            the function includ all functions that are need for create an account
        """
        if (
            self.email.text() == ""
            or self.username.text() == ""
            or self.password.text() == ""
            or self.confirmpass.text() == ""
        ):#check if the cells are empty 
            global_vers.create_msgbox("error", "Please fill in all the cells")
            return
        if (
            self.check_email() == 1
            and self.check_password() == 1
        ):#check if the text in the email cell is email and if the passwords are match
            if self.send_to_server() == "":#try to create the account in the server
                self.back_to_login()#go back to login back after create the account
                print(
                    "\n\nSuccessfully Created account \nEmail: %s\nUsername: %s\nPassword: %s\n\n"
                    % (self.email.text(), self.username.text(), self.password.text())
                )
            else:
                return
        else:
            return

    def check_email(self):
        """
        check if the text the user enter is a email
        """
        user_email = self.email.text()
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'#email format
        if not re.fullmatch(regex, user_email):
            global_vers.create_msgbox(
                "email-error", "There is a problem with the email you entered"
            )
            return 0
        else:
            return 1



    def check_password(self):
        """
        check if the passwords are match and under appropriate conditions
        """
        if self.password.text() == self.confirmpass.text():#check if the passwords are match
            password = self.password.text()
            if len(password) < 8 or len(password) > 16:#check if the password is long enough
                global_vers.create_msgbox(
                    "password-error", "the password mast by between 8 to 16 chars"
                )
                return 0
            elif (
                len(re.findall("[a-z]", password)) < 1
                or len(re.findall("[A-Z]", password)) < 1
            ):#check if the password is contains lowercase and uppercase letters
                global_vers.create_msgbox(
                    "password-error",
                    "the password most includ a uppercase letters and lowercase letters in English",
                )
                return 0
            elif len(re.findall("[0-9]", password)) < 2:#check if the password is contains numbers
                global_vers.create_msgbox(
                    "password-error", "the password most includ a digits"
                )
                return 0
            return 1
        else:

            global_vers.create_msgbox("error", "The passwords do not match")
            return 0
    def send_to_server(self):
        """
        """
        if global_vers.conn == "":
            global_vers.create_msgbox("server-error", "no connection         ")
            return
        new_user = User(
                0,self.email.text(), self.username.text(), self.password.text(),datetime.now().strftime("%d/%m/%Y %H:%M:%S"), 0
            )#create user object
        cmd = client.create_account(global_vers.conn,new_user)#send to the server for answer
        if cmd == chatlib.PROTOCOL_SERVER["failed_msg"]:
            return "failed"
        elif cmd == chatlib.PROTOCOL_SERVER["email_exists"]:
            global_vers.create_msgbox("email - error", "Email already exists")#email error
            return "email"
        elif cmd == chatlib.PROTOCOL_SERVER["username_exists"]:
            global_vers.create_msgbox("username - error", "Username already exists")#username error
            return "username"
        else:
            return ""
        
    def back_to_login(self):
        self.widget.setCurrentIndex(global_vers.windows_indexes["login"])
