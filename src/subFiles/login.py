from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QDialog, QDesktopWidget, QWidget, QMessageBox
from PyQt5.uic import loadUi
from module import global_vers, client
from module.user import User
from subFiles.profile import Profile


def login_func(username, password):
	"""login function

	Args:
		email (string): user email
		password (string): user password

	Returns:
		bool_1: If the user exists
		bool_2: User information if it does exist
	"""
	client.USERNAME = username
	client.PASSWORD = password
	data, login_status = client.login(global_vers.server_connection)
	if login_status == client.OK:
		return True, login_status, data
	return False, None, data


class Login(QDialog):
	def __init__(self, widget):
		"""init function that set al the main stuff of th page like UI and clicked event"""
		super(Login, self).__init__()
		loadUi("UI\login.ui", self)  # load the UI of the page
		
		self.widget = widget
		
		self.username.returnPressed.connect(
			self.login_func
		)  # enter event to username filed
		self.password.returnPressed.connect(
			self.login_func
		)  # enter event to password filed
		self.loginbutton.clicked.connect(self.login_func)  # click event to login button
		self.createaccountbutton.clicked.connect(
			self.go_to_create
		)  # click event on the create account text
		self.backbutton.clicked.connect(self.back_to_home)  # click event to back button
	
	def login_func(self):
		if global_vers.server_connection == None:
			global_vers.create_msgbox("server-error", "no connection         ")
			return
		username = self.username.text()
		password = self.password.text()
		login_status, user, data = login_func(
			self.username.text(), self.password.text()
		)  # check if the user is exists
		if login_status == True:
			# if the user is exists, so he logged in and go to the profile page
			print(
				"\n\nSuccessfully Logged in \nUsername: %s\nPassword: %s\n\n"
				% (username, password)
			)
			global_vers.LOGIN_STATUS = 1
			
			self.widget.widget(global_vers.windows_indexes [ "home" ]).show_logout_btn()
			
			username = self.username.setText("")
			password = self.password.setText("")
			login_status = False
			
			profile = Profile(self.widget)  # profile page
			self.widget.insertWidget(global_vers.windows_indexes [ "profile" ], profile)
			self.widget.setCurrentIndex(global_vers.windows_indexes [ "profile" ])
		else:
			# if the user is don't exist, msg box tell the user that something wrong
			global_vers.create_msgbox("error", data)
			print("Can't login to the server")
			self.username.setText("")
			self.password.setText("")
	
	def go_to_create(self):
		self.widget.setCurrentIndex(global_vers.windows_indexes [ "create" ])
	
	def back_to_home(self):
		self.widget.setCurrentIndex(global_vers.windows_indexes [ "home" ])
