import sys
import time

from PyQt5 import QtWidgets, QtCore, Qt
from PyQt5.QtWidgets import QApplication, QDialog, QDesktopWidget, QWidget
from PyQt5.uic import loadUi
from PyQt5 import QtGui
import threading

from module import global_vers, client, chatlib
from module.user import User


class Game(QDialog):
	def __init__(self, widget):
		"""init function that set al the main stuff of th page like UI and clicked event"""
		super(Game, self).__init__()
		loadUi("UI\game.ui", self)  # load the UI of the page
		
		self.widget = widget
		self.backbutton.clicked.connect(self.back_to_home)  # click event to back button
		
		self.stop_threads = False
		self.questions_count = 0
		self.current_score = 0
		self.update_score()
		self.answer_1_label.clicked.connect(lambda: self.send_answer(1))
		self.answer_2_label.clicked.connect(lambda: self.send_answer(2))
		self.answer_3_label.clicked.connect(lambda: self.send_answer(3))
		self.answer_4_label.clicked.connect(lambda: self.send_answer(4))
	
	def start_to_play(self):
		if self.get_question_from_server() == None:
			return None
		self.questions_count += 1
		self.display_question()
	
	def get_question_from_server(self):
		data = client.get_question(global_vers.server_connection)
		if data == None:
			return None
		self.ques_id = data [ 0 ]
		self.ques = data [ 1 ]
		self.answers = data [ 2:6 ]
		self.correct_answer = data [ 6 ]
		self.display_question()
		return True
	
	def display_question(self):
		self.question_label.setText(self.ques)
		self.answer_1_label.setText(self.answers [ 0 ])
		self.answer_2_label.setText(self.answers [ 1 ])
		self.answer_3_label.setText(self.answers [ 2 ])
		self.answer_4_label.setText(self.answers [ 3 ])
		self.question_number_label_count.setText(str(self.questions_count))
	
	def update_score(self, new_points=0):
		self.current_score = self.current_score + new_points
		self.score_label.setText(str(self.current_score) + "p")
	
	def start_time(self, new_time=5):
		self.time_to_play = new_time
		while True:
			if self.stop_threads:
				break
			time.sleep(1)
			self.time_label.setText(str(self.time_to_play) + "s")
			print("time left: %s sec" % self.time_to_play)
			self.time_to_play -= 1
			if self.time_to_play <= 0:
				self.stop_time()
		print("Stop as you wish")
		sys.exit()
	
	def stop_time(self):
		self.current_score = 0
		self.widget.setCurrentIndex(global_vers.windows_indexes [ "home" ])
		sys.exit()
	
	def set_timer(self, new_time=global_vers.time_for_game):
		self.stop_threads = False
		self.timer = threading.Thread(target=self.start_time, args=(new_time,))
		self.timer.start()
	
	def send_answer(self, user_choise=0):
		answer = client.play_question(global_vers.server_connection, str(self.ques_id), str(user_choise))
		print("you click on %s and the correct answer is: %s" % (str(user_choise), str(answer)))
		
		if answer == True:
			self.stop_threads = True
			self.timer.join()
			global_vers.create_msgbox(
				"Your answer is:",
				"Correct         ")
			self.update_score(5)
		elif answer in [ "1", "2", "3", "4" ]:
			self.stop_threads = True
			self.timer.join()
			global_vers.create_msgbox(
				"Your answer is:",
				"Not correct, correct answer is |%s|" % answer)
		else:
			print("EEERRRROOOORRRR")
		self.set_timer(self.time_to_play)
		self.start_to_play()
	
	def back_to_home(self):
		answer = global_vers.create_dialog_qes(self.widget,
		                                       "Exit the game",
		                                       "You want to exit the game and go back to home")
		if answer:
			self.current_score = 0
			self.stop_threads = True
			self.timer.join()
			self.widget.setCurrentIndex(global_vers.windows_indexes [ "home" ])
			return
