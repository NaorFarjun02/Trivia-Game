from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QDesktopWidget,
    QWidget,
    QMessageBox,
    QFrame,
    QLabel,
    QProgressBar,
)
from PyQt5.uic import loadUi

from module import global_vers, client
from module.user import User
import re

achievement_list = {
    "won 10 games": [7, 10],
    "won 100 games": [10, 100],
    "won 1000 games": [109, 1000],
    "won 5 games": [3, 5],
    "get 1000 coins": [567, 1000],
    "get 10000 coins": [4345, 10000],
    "get 100000 coins": [43475, 100000],
    "add 1 friend": [0, 1],
}


class Profile(QDialog):
    def __init__(self, widget):
        """init function that set al the main stuff of th page like UI and clicked event"""
        super(Profile, self).__init__()
        loadUi("UI\profile.ui", self)  # load the UI of the pag
        self.widget = widget

        self.add_coins_button.clicked.connect(self.go_to_shop)

        for achiev in achievement_list.keys():
            self.achievement_frame.addWidget(
                self.create_achievement_frame(achiev)
            )  # add the achievement to the achievements view

            self.friends_frame.addWidget(
                self.create_achievement_frame(achiev)
            )  # add the achievement to the achievements view

    def create_achievement_frame(self, achiev):
        # Frame#
        new_frame = QFrame(
            self
        )  # create a frame for achievement | after create set vars
        new_frame.setStyleSheet(
            "QFrame{background-color: rgb(0, 0, 0);}QLabel{color: rgb(255, 255, 255);font: 10pt 'Consolas';background-color: none;}QProgressBar{	background-color: transparent;	border:1px solid rgb(255,255,255);}"
        )  # stylesheet for achievement frame
        new_frame.setFixedHeight(140)
        new_frame.setFixedWidth(160)

        # Achievement title#
        achiev_title = QLabel(
            self
        )  # create achievement title label | after create set vars
        achiev_title.setText(achiev)
        achiev_title.setGeometry(10, 10, 110, 50)
        achiev_title.setParent(new_frame)  # append the the title to the frame

        # Achievement progress bar#
        achiev_progress = QProgressBar(
            self
        )  # create achieve progress bar | after create set vars
        achiev_progress.setMaximum(achievement_list[achiev][1])
        achiev_progress.setMinimum(0)
        achiev_progress.setValue(achievement_list[achiev][0])
        achiev_progress.setTextVisible(False)
        achiev_progress.setGeometry(10, 111, 140, 20)
        achiev_progress.setParent(new_frame)  # append the progress bar to the frame

        # Achievement progress bar text #
        achiev_progress_text = QLabel(
            self
        )  # create achievement progress bar text label | after create set vars
        achiev_progress_text.setText(
            ""
            + str(achievement_list[achiev][0])
            + "/"
            + str(achievement_list[achiev][1])
        )
        achiev_progress_text.setGeometry(15, 110, 140, 20)
        achiev_progress_text.setParent(new_frame)  # append the the title to the frame
        return new_frame

    def go_to_shop(self):
        # self.widget.setCurrentIndex(global_vers.windows_indexes["shop"])
        print("shop")
        pass
