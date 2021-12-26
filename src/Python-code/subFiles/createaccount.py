from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QDialog, QDesktopWidget, QWidget, QMessageBox
from PyQt5.uic import loadUi
from module import global_vers, client
from module.user import User

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
        if (
            self.email.text() == ""
            or self.username.text() == ""
            or self.password.text() == ""
            or self.confirmpass.text() == ""
        ):
            global_vers.create_msgbox("error", "Please fill in all the cells")
            return
        if (
            self.check_username() == 1
            and self.check_email() == 1
            and self.check_password() == 1
        ):
            self.widget.setCurrentIndex(global_vers.windows_indexes["login"])
        else:
            return

    def check_email(self):
        user_email = self.email.text()
        if "@gmail.com" not in user_email:
            global_vers.create_msgbox(
                "email-error", "There is a problem with the email you entered"
            )
            return 0
        else:
            return 1

    def check_username(self):
        test_username = self.username.text()
        # get from the database the username of evreyone
        return 1
        # users=[]
        # for user in users:
        #     if test_username == user.getUsername():
        #         global_vers.create_msgbox(
        #             "username-error",
        #             "the username exists in the system, select another one",
        #         )
        #         return 0
        #     else:
        #         return 1

    def check_password(self):
        if self.password.text() == self.confirmpass.text():
            password = self.password.text()
            if len(password) < 8 or len(password) > 16:
                global_vers.create_msgbox(
                    "password-error", "the password mast by between 8 to 16 chars"
                )
                return 0
            elif (
                len(re.findall("[a-z]", password)) < 1
                or len(re.findall("[A-Z]", password)) < 1
            ):
                global_vers.create_msgbox(
                    "password-error",
                    "the password most includ a uppercase letters and lowercase letters in English",
                )
                return 0
            elif len(re.findall("[0-9]", password)) < 2:
                global_vers.create_msgbox(
                    "password-error", "the password most includ a digits"
                )
                return 0
            new_user = User(
                self.email.text(), self.username.text(), self.password.text(), 0
            )
            if global_vers.conn == "":
                global_vers.create_msgbox("server-error", "no connection         ")
                return
            client.create_account(global_vers.conn,new_user)
            # print(
            #     "\n\nSuccessfully Created account \nEmail: %s\nUsername: %s\nPassword: %s\n\n"
            #     % (self.email.text(), self.username.text(), self.password.text())
            # )
            return 1
        else:

            global_vers.create_msgbox("error", "The passwords do not match")
            return 0

    def back_to_login(self):
        self.widget.setCurrentIndex(global_vers.windows_indexes["login"])
