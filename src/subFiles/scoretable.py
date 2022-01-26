from PyQt5 import QtWidgets, QtCore, Qt
from PyQt5.QtWidgets import QApplication, QDialog, QDesktopWidget, QWidget
from PyQt5.uic import loadUi
from PyQt5 import QtGui
from module import global_vers, client, chatlib
from module.user import User


class ScoreTable(QDialog):
	def __init__(self, widget):
		"""init function that set al the main stuff of th page like UI and clicked event"""
		super(ScoreTable, self).__init__()
		loadUi("UI\scoretable.ui", self)  # load the UI of the page
		
		self.widget = widget
		
		self.backbutton.clicked.connect(self.back_to_home)  # click event to back button
		
		self.setTableStlye()
		
		self.score_list = [ ]
	
	def setTableStlye(self):
		for i in range(5):
			self.score_table.setColumnWidth(i, 175)
	
	def create_cell(self, value=""):
		cell = QtWidgets.QTableWidgetItem(value)
		cell.setTextAlignment(QtCore.Qt.AlignHCenter)
		cell.setFlags(QtCore.Qt.ItemIsEnabled)
		return cell
	
	def loadDataToTable(self):
		req = self.requet_data_from_server()
		if req == 0:
			global_vers.create_msgbox("Error", "something get wrong")
		row = 0
		self.score_table.setRowCount(len(self.score_list.users_score_list))
		for user in self.score_list.users_score_list:
			self.score_table.setItem(row, 0, self.create_cell(user [ "username" ]))
			self.score_table.setItem(row, 1, self.create_cell(user [ "uid" ]))
			self.score_table.setItem(row, 2, self.create_cell(str(user [ "score" ])))
			self.score_table.setItem(row, 3, self.create_cell(str(user [ "wins" ])))
			self.score_table.setItem(row, 4, self.create_cell(str(user [ "games" ])))
			row += 1
	
	def requet_data_from_server(self):
		cmd, self.score_list = client.gethighscore(global_vers.server_connection)
		if cmd == chatlib.PROTOCOL_SERVER [ "all_score" ]:
			print(self.score_list.users_score_list)
			return 1
		return 0
	
	def back_to_home(self):
		self.widget.setCurrentIndex(global_vers.windows_indexes [ "home" ])
