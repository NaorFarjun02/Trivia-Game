####################### Trivia Game #######################

import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication

from module import global_vers, client
from subFiles.createaccount import CreateAcount
from subFiles.home import Home
from subFiles.login import Login
from subFiles.profile import Profile
from subFiles.scoretable import ScoreTable
from subFiles.game import Game

global_vers.LOGIN_STATUS = 0  # in the start the user is not login

app = QApplication(sys.argv)  # create the app
widget = QtWidgets.QStackedWidget()  # create list of all views

home = Home(widget)  # home page
widget.insertWidget(global_vers.windows_indexes [ "home" ], home)

login = Login(widget)  # login page
widget.insertWidget(global_vers.windows_indexes [ "login" ], login)

create_account = CreateAcount(widget)  # create account page
widget.insertWidget(global_vers.windows_indexes [ "create" ], create_account)

profile = Profile(widget)  # profile page
widget.insertWidget(global_vers.windows_indexes [ "profile" ], profile)

game = Game(widget)
widget.insertWidget(global_vers.windows_indexes [ "game" ], game)

score_table = ScoreTable(widget)
widget.insertWidget(global_vers.windows_indexes [ "scoretable" ], score_table)

widget.setCurrentIndex(0)
widget.setFixedWidth(960)
widget.setFixedHeight(730)

widget.show()
app.exec_()
game.stop_threads = True
game.timer.join()
if str(type(global_vers.server_connection)) == "<class 'socket.socket'>":
	client.logout(global_vers.server_connection)
	global_vers.user_data = None
	global_vers.server_connection = None
