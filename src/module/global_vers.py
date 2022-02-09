from PyQt5.QtWidgets import QMessageBox

global LOGIN_STATUS  # user login status

server_connection = None
user_data = None
time_for_game = 60
windows_indexes = {
	"home": 0,
	"login": 1,
	"create": 2,
	"profile": 3,
	"game": 5,
	"scoretable": 4,
	"shop": 6,
	"settings": 27,
}  # A list of all the indexes of each page


def create_msgbox(title, text):
	"""create msg box

	Args:
		title (string): the msg title
		text (string): the info of the msg
	"""
	msg = QMessageBox()
	msg.setWindowTitle(title)
	msg.setText(text)
	x = msg.exec_()


def create_dialog_qes(widget, title, text):
	"""create msg box

	Args:
		title (string): the msg title
		text (string): the info of the msg
	"""
	answer = QMessageBox.question(widget, title, text, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
	if answer == QMessageBox.Yes:
		return True
	elif answer == QMessageBox.No:
		return False
	else:
		return None


def create_dialog_after_answer(widget, title, text):
	"""create msg box

	Args:
		title (string): the msg title
		text (string): the info of the msg
	"""
	answer = QMessageBox.question(widget, title, text, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
	if answer == QMessageBox.Yes:
		return True
	else:
		return False
