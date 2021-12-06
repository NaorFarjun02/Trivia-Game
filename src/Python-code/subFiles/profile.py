from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QDialog, QDesktopWidget, QWidget, QMessageBox,QFrame
from PyQt5.uic import loadUi
import global_vers
from user import User
import re

achievement_list={
    "won 10 games":[10,100],
    "won 10 games":[10,100],
    "won 10 games":[10,100],
    "won 10 games":[10,100],
    "won 10 games":[10,100],
    "won 10 games":[10,100],
    "won 10 games":[10,100],
    "won 10 games":[10,100],
    "won 10 games":[10,100],
    "won 10 games":[10,100],
    "won 10 games":[10,100],
    "won 10 games":[10,100],
    "won 10 games":[10,100],
    "won 10 games":[10,100],
    "won 10 games":[10,100],
    "won 10 games":[10,100],
    "won 10 games":[10,100],
    "won 10 games":[10,100],
    "won 10 games":[10,100],
    "won 10 games":[10,100],
    
}
class Profile(QDialog):
    def __init__(self, widget):
        """init function that set al the main stuff of th page like UI and clicked event"""
        super(Profile, self).__init__()
        loadUi("Profile\profile.ui", self)  # load the UI of the page
        self.widget = widget

        self.add_coins_button.clicked.connect(self.go_to_shop)
        
        new_frame=QFrame(self)
        new_frame.setStyleSheet("QFrame{background-color: rgb(0, 0, 0);}QLabel{color: rgb(255, 255, 255);font: 10pt 'Consolas';background-color: none;}QProgressBar{	background-color: rgb(0, 0, 0);	border:1px solid rgb(255,255,255);}")
        
    def go_to_shop(self):
        # self.widget.setCurrentIndex(global_vers.windows_indexes["shop"])
        print("shop")
        pass
