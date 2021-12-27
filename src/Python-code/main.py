#the main file in the client side#

import sys
import socket
import threading
import random
import re
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication


from subFiles.home import Home
from subFiles.login import Login
from subFiles.createaccount import CreateAcount
from subFiles.profile import Profile

from module import global_vers, client
from module.user import User

global_vers.LOGIN_STATUS = 0  # in the start the user is not login


app = QApplication(sys.argv)  # create the app
widget = QtWidgets.QStackedWidget()  # create list of all views

home = Home(widget)  # home page
widget.insertWidget(global_vers.windows_indexes["home"], home)

login = Login(widget)  # login page
widget.insertWidget(global_vers.windows_indexes["login"], login)

create_account = CreateAcount(widget)  # create account page
widget.insertWidget(global_vers.windows_indexes["create"], create_account)

profile = Profile(widget)  # profile page
widget.insertWidget(global_vers.windows_indexes["profile"], profile)

widget.setCurrentIndex(0)
widget.setFixedWidth(960)
widget.setFixedHeight(730)
widget.show()
app.exec_()

if str(type(global_vers.conn))=="<class 'socket.socket'>":
    client.logout(global_vers.conn)
    global_vers.conn = ""
