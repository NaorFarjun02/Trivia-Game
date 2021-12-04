from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QDialog, QDesktopWidget, QWidget, QMessageBox
from PyQt5.uic import loadUi
import global_vers
from user import User
import re


class Profile(QDialog):
    def __init__(self, widget):
        """init function that set al the main stuff of th page like UI and clicked event"""
        super(Profile, self).__init__()
        loadUi("Profile\profile.ui", self)  # load the UI of the page
        self.widget = widget

        
        
        self.add_coins_button.clicked.connect(self.go_to_shop)
        
    def go_to_shop(self):
        # self.widget.setCurrentIndex(global_vers.windows_indexes["shop"])
        print("shop")
        pass
