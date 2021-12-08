from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QDialog, QDesktopWidget, QWidget, QMessageBox
from PyQt5.uic import loadUi
import global_vers


class Home(QDialog):
    def __init__(self, widget):
        """init function that set al the main stuff of th page like UI and clicked event"""
        super(Home, self).__init__()
        loadUi("UI\home.ui", self)  # load the UI of the page
        self.widget = widget
        
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
        if global_vers.LOGIN_STATUS == 0:
            print("you need to login first")
            self.menu.hide()  # hide the side menu
            self.widget.setCurrentIndex(global_vers.windows_indexes["login"])
        elif global_vers.LOGIN_STATUS == 1:
            print("profile")
            self.widget.setCurrentIndex(global_vers.windows_indexes["profile"])

    def shop(self):
        print("shop")

    def setting(self):
        print("setting")
