from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QDialog, QDesktopWidget, QWidget, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5.uic import loadUi
from module import global_vers, client

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
        self.scoretablebutton.clicked.connect(
            self.scoretable
        )  # click event to the profile button in the menu
        self.profilebutton.clicked.connect(
            self.profile
        )  # click event to the profile button in the menu
        self.shopbutton.clicked.connect(
            self.shop
        )  # click event to the shop button in the menu
        self.settingbutton.clicked.connect(
            self.setting
        )  # click event to the setting button in the menu
        self.connect_to_server()

    def show_menu(self):
        if self.menu.isHidden():
            self.menu.show()
        else:
            self.menu.hide()

    def profile(self):
        if global_vers.conn=="":
            global_vers.create_msgbox("server-error", "no connection         ")
            return
        if global_vers.LOGIN_STATUS == 0:
            print("you need to login first")
            self.menu.hide()  # hide the side menu
            self.widget.setCurrentIndex(global_vers.windows_indexes["login"])
        elif global_vers.LOGIN_STATUS == 1:
            print("profile")
            self.widget.setCurrentIndex(global_vers.windows_indexes["profile"])
    def scoretable(self):
        if global_vers.conn=="":
            global_vers.create_msgbox("server-error", "no connection         ")
            return
        elif global_vers.LOGIN_STATUS == 0:
            global_vers.create_msgbox("server-error", "you need to login first ")
            return
        score_list=client.gethighscore(global_vers.conn)
    def shop(self):
        print("shop")
    def setting(self):
        print("setting")


    def connect_to_server(self):
        try:
            global_vers.conn = client.connect()#try to connect the server

            pixmap = QPixmap('UI\icons\signal.png')#create connect icon
            self.connection_icon.setPixmap(pixmap) #set the connection icon to connect  

            self.connection_text.setText("Connected")
            self.connection_text.setGeometry(30,90,71,20)
        except:
            pixmap = QPixmap('UI\icons\\no-signal.png')#create not connect icon
            self.connection_icon.setPixmap(pixmap)#set the connection icon to not connect

            self.connection_text.setText("Not Connected")
            self.connection_text.setGeometry(20,90,81,20)
