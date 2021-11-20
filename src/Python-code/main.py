import sys
import socket
import threading
import random
import re
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from user import User
from subFiles.home import Home
from subFiles.login import Login
from subFiles.createaccount import CreateAcount
import global_vers

global_vers.LOGIN_STATUS = 0


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()

home = Home(widget)  # home page
widget.insertWidget(global_vers.windows_indexes["home"], home)

login = Login(widget)  # login page
widget.insertWidget(global_vers.windows_indexes["login"], login)

create_account = CreateAcount(widget)  # create account page
widget.insertWidget(global_vers.windows_indexes["create"], create_account)

# profile = Profile()#profile page
# widget.insertWidget(global_vers.windows_indexes["profile"], profile)

widget.setCurrentIndex(0)
widget.setFixedWidth(850)
widget.setFixedHeight(600)
widget.show()
app.exec_()
