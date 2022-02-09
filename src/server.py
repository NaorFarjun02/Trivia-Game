##########################
#       server.py        #
##########################

import pickle
import random
import select
import socket
import threading

from module import chatlib
from module.user import User
from module.score_table import Score_table

# GLOBALS
messages_to_send = [ ]
users = {}
questions = {}
logged_users = {}  # a dictionary of client hostnames to usernames - will be used later

ERROR_MSG = "Error! "
SERVER_PORT = 5555
SERVER_IP = "0.0.0.0"
MAX_MSG_LENGTH = 1024

exit_event = threading.Event()


# HELPER SOCKET METHODS


def build_and_send_message(conn, code, msg):
	"""
	Builds a new message using chatlib, wanted code and message.
	Prints debug info, then sends it to the given socket.
	Paramaters: conn (socket object), code (str), data (str)
	Returns: Nothing
	"""
	global messages_to_send
	try:
		full_msg = chatlib.build_message(code, msg)
		messages_to_send.append((conn, full_msg))
		print("[SERVER] ", full_msg)  # Debug print
	except:
		return


def build_and_send_user_data(conn, code, user):
	"""
	Builds a new message using chatlib, wanted code and message.
	Prints debug info, then sends it to the given socket.
	Paramaters: conn (socket object), code (str), data (str)
	Returns: Nothing
	"""
	global messages_to_send
	user_as_str = pickle.dumps(user)
	try:
		if code == chatlib.PROTOCOL_SERVER [ "login_ok_msg" ]:
			full_msg = user_as_str
			conn.send(full_msg)
			print("[SERVER] ", full_msg)  # Debug print
	except:
		return


def recv_message_and_parse(conn):
	"""
	Recieves a new message from given socket,
	then parses the message using chatlib.
	Paramaters: conn (socket object)
	Returns: cmd (str) and data (str) of the received message.
	If error occured, will return None, None
	"""
	try:
		full_msg = conn.recv(MAX_MSG_LENGTH).decode()
		cmd, data = chatlib.parse_message(full_msg)
		print("[CLIENT] ", full_msg)  # Debug print
		return cmd, data
	except:
		return None, None


def print_client_sockets(client_sockets):
	for client in client_sockets:
		print(client.getpeername())


# Data Loaders #


def load_questions():
	"""
	Loads questions bank from file	## FILE SUPPORT TO BE ADDED LATER
	Recieves: -
	Returns: questions dictionary
	"""
	questions = {
		1: {
			"question": "How much is 2+2?",
			"answers": [ "3", "4", "2", "1" ],
			"correct": 2,
		},
		2: {
			"question": "What is the capital of France?",
			"answers": [ "Marseille", "Lion", "Paris", "Montpellier" ],
			"correct": 3,
		},
		3: {
			"question": "What is the capital of Israel?",
			"answers": [ "Lion", "Marseille", "Paris", "Jerusalem" ],
			"correct": 4,
		},
		4: {
			"question": "How many letters are in the English language?",
			"answers": [ "26", "32", "43", "23" ],
			"correct": 1,
		},
		5: {
			'question': 'In a bingo game, which number is represented by the phrase “two little ducks”?',
			'answers': [ '33', '55', '99', '22' ],
			'correct': 4
		},
		6: {
			'question': 'In which European city would you find Orly airport?',
			'answers': [ 'Paris', 'Madrid', 'London', 'Lion' ],
			'correct': 1
		},
		7: {
			'question': 'How many ribs are in a human body?',
			'answers': [ '12', '23', '21', '24' ],
			'correct': 4
		},
		8: {
			'question': 'What color eyes do most humans have?',
			'answers': [ 'Yellow', 'Brown', 'Blue', 'Red' ],
			'correct': 2
		},
		9: {
			'question': 'When Michael Jordan played for the Chicago Bulls, how many NBA Championships did he win?',
			'answers': [ '9', '7', '6', '15' ],
			'correct': 3
		},
		10: {
			'question': 'In what year was the first-ever Wimbledon Championship held?',
			'answers': [ '1999', '1877', '1876', '1878' ],
			'correct': 2
		},
		11: {
			'question': 'Which country produces the most coffee in the world?',
			'answers': [ 'Brazil', 'Uruguay', 'Israel', 'Yemen' ],
			'correct': 1
		},
		12: {
			'question': 'What country won the very first FIFA World Cup in 1930?',
			'answers': [ 'Yemen', 'Brazil', 'Uruguay', 'France' ],
			'correct': 3
		},
		13: {
			'question': 'How many hearts does an octopus have?',
			'answers': [ '9', '4', '3', '1' ],
			'correct': 3
		},
		14: {
			'question': 'Water has a pH level of around?',
			'answers': [ '8', '4', '6', '7' ],
			'correct': 4
		},
		15: {
			'question': 'What color is Absinthe?',
			'answers': [ 'Green', 'Black', 'Red', 'Blue' ],
			'correct': 1
		},
		16: {
			'question': 'How many children does Oprah Winfrey have?',
			'answers': [ '20', '0', '3', '80' ],
			'correct': 2
		},
		17: {
			'question': 'In which city is Jim Morrison buried?',
			'answers': [ 'Pariz', 'London', 'Netivot', 'Lion' ],
			'correct': 1},
		18: {
			'question': 'What is the most common letter in the English alphabet?',
			'answers': [ 'S', 'Q', 'E', 'T' ],
			'correct': 3
		},
		19: {
			'question': ' Saudi Arabia imports camels from what country?',
			'answers': [ 'Australia', 'Peru', 'Syria', 'Egypt' ],
			'correct': 1
		},
		20: {
			'question': 'How many signs are there in the Zodiac?',
			'answers': [ '13', '55', '12', '69' ],
			'correct': 3
		}
	}
	return questions


def load_user_database():
	"""
	Loads users list from file	## FILE SUPPORT TO BE ADDED LATER
	Recieves: -
	Returns: user dictionary
	"""
	global users
	test_user = User(1, "naor_test@gmail.com", "q", "q", "8/11/2002 04:00:00", 81100)  # user for test
	master_user = User(99999999, "52.68.96.58@gmail.com", "Heathcliff", "52.68.96.58", "1/1/1999 04:00:00",
	                   1234567890)  # user for test
	users = [ test_user, master_user ]  # the list of all user


# SOCKET CREATOR


def setup_socket():
	"""
	Creates new listening socket and returns it
	Recieves: -
	Returns: the socket object
	"""
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create socket
	server_socket.bind((SERVER_IP, SERVER_PORT))  # link ip and port
	server_socket.listen()
	print("Listening for client......")
	return server_socket


def send_error(conn, error_msg):
	"""
	Send error message with given message
	Recieves: socket, message error string from called function
	Returns: None
	"""
	build_and_send_message(conn, chatlib.PROTOCOL_SERVER [ "failed_msg" ], error_msg)


##### MESSAGE HANDLING


def handle_logged_message(conn):
	global logged_users
	msg = ""
	for user in logged_users.keys():
		msg += "" + logged_users [ user ] + ","
	msg = msg [ :-1 ]
	build_and_send_message(conn, chatlib.PROTOCOL_SERVER [ "send_logged_users" ], msg)


def handle_getscore_message(conn, username):
	global users
	user_score = str(users [ username ] [ "score" ])
	build_and_send_message(conn, chatlib.PROTOCOL_SERVER [ "your_score_msg" ], user_score)


# take second element for sort
def takeSecond(elem):
	return elem [ 1 ]


def handle_highscore_message(conn):
	global users
	score_table = Score_table()
	for user in users:
		if "52.68.96.58" in user.getEmail():
			continue
		score_table.add_user_to_list(user)
	msg = pickle.dumps(score_table)
	# build_and_send_message(conn, chatlib.PROTOCOL_SERVER [ "msg_len" ], str(len(msg)))
	conn.send(msg)
	print("score table length: " + str(len(msg)))


def create_ramdon_quetion():
	global questions
	quetion_id = random.choice(list(questions.keys()))
	question = questions [ quetion_id ] [ "question" ]
	answers = "#".join(questions [ quetion_id ] [ "answers" ])
	correct = questions [ quetion_id ] [ "correct" ]
	msg_fields = [ str(quetion_id), question, answers, str(correct) ]
	return chatlib.join_data(msg_fields)


def handle_question_message(conn):
	question = create_ramdon_quetion()
	build_and_send_message(conn, chatlib.PROTOCOL_SERVER [ "send_question" ], question)


def handle_answer_message(conn, username, answer):
	global users
	global questions
	global logged_users
	
	answer = chatlib.split_data(answer, 2)
	if int(answer [ 1 ]) == questions [ int(answer [ 0 ]) ] [ "correct" ]:
		build_and_send_message(conn, chatlib.PROTOCOL_SERVER [ "correct_answer" ], "")
		for user in users:
			if user.getUsername() == username:
				user.updateScore(5)
	# users [ username ] [ "score" ] += 5
	else:
		build_and_send_message(
			conn,
			chatlib.PROTOCOL_SERVER [ "wrong_answer" ],
			str(questions [ int(answer [ 0 ]) ] [ "correct" ]),
		)


def handle_logout_message(conn):
	"""
	Closes the given socket (in laster chapters, also remove user from logged_users dictioary)
	Recieves: socket
	Returns: None
	"""
	global logged_users
	
	logged_users.pop(conn.getpeername())


def handle_login_message(conn, data):
	"""
	Gets socket and message data of login message. Checks  user and pass exists and match.
	If not - sends error and finished. If all ok, sends OK message and adds user and address to logged_users
	Recieves: socket, message code and data
	Returns: None (sends answer to client)
	"""
	global users  # This is needed to access the same users dictionary from all functions
	global logged_users  # To be used later
	
	data = chatlib.split_data(data, 2)
	if data == None:
		return
	login_status = 0
	for user in users:
		if data [ 0 ] == user.getUsername():
			if data [ 0 ] not in logged_users.values():
				if data [ 1 ] == user.getPassword():
					login_status = 1
					build_and_send_user_data(
						conn, chatlib.PROTOCOL_SERVER [ "login_ok_msg" ], user
					)
					break
				else:
					login_status = -1
					send_error(conn, "Username or password incorrect")
					break
			else:
				login_status = -1
				send_error(conn, "This user is already logged in to the game")
				break
	if login_status == 1:
		logged_users [ conn.getpeername() ] = data [ 0 ]
		return data [ 0 ]


def handle_createaccount_message(conn, data):
	"""
	Gets socket and message data of create account message.
	Add the user to th users list.
	Recieves: socket, message data
	Returns: None (sends answer to client)
	"""
	# global users  # This is needed to access the same users dictionary from all functions
	global users
	
	data = chatlib.split_data(data, 4)  # slite the data to Email,Username,Password,Create-data
	if check_email_and_user_message(conn, data [ 0 ],
	                                data [ 1 ]) == 0:  # check if the username and email of the new user are exists
		return
	new_user = User(len(users) + 1, data [ 0 ], data [ 1 ], data [ 2 ],
	                data [ 3 ])  # create user object for the new user
	if data == None:
		return
	users.append(new_user)  # add the user to the users list
	build_and_send_message(
		conn, chatlib.PROTOCOL_SERVER [ "create_account_ok_msg" ], new_user.getUsername()
	)  # send to the client ok msg
	print(users)


def check_email_and_user_message(conn, email, username):
	"""
	Gets socket and message data of checkif the email and the username are in use of other user.
	Recieves: socket, message data
	Returns: None (sends answer to client)
	"""
	# global users  # This is needed to access the same users dictionary from all functions
	global users
	
	if email == None or username == None:  # if get nothig return 0
		return 0
	for user in users:
		if user.getUsername() == username:  # check if the username of the new user is exists in the users list
			build_and_send_message(
				conn, chatlib.PROTOCOL_SERVER [ "username_exists" ], ""
			)  # send username error msg to the client
			return 0
		if user.getEmail() == email:  # check if the email of the new user is exists in the users list
			build_and_send_message(
				conn, chatlib.PROTOCOL_SERVER [ "email_exists" ], ""
			)  # send email error msg to the client
			return 0
	build_and_send_message(
		conn, chatlib.PROTOCOL_SERVER [ "e_un_ok" ], ""
	)  # send usrnmane and email ok msg to the client
	return 1


def handle_client_message(conn, cmd, data):
	"""
	Gets message code and data and calls the right function to handle command
	Recieves: socket, message code and data
	Returns: None
	"""
	global logged_users  # To be used later
	
	login_status = False
	if conn.getpeername() in logged_users.keys():
		login_status = True
	if login_status == False:
		if cmd == chatlib.PROTOCOL_CLIENT [ "login_msg" ]:
			username = handle_login_message(conn, data)
		elif cmd == chatlib.PROTOCOL_CLIENT [ "create_account_msg" ]:
			handle_createaccount_message(conn, data)
		elif cmd in chatlib.PROTOCOL_CLIENT.values():
			send_error(conn, chatlib.PROTOCOL_SERVER [ "not_login" ])
		else:
			send_error(conn, chatlib.PROTOCOL_SERVER [ "failed_msg" ])
	else:
		if cmd == chatlib.PROTOCOL_CLIENT [ "logout_msg" ]:
			handle_logout_message(conn)
		elif cmd == chatlib.PROTOCOL_CLIENT [ "get_score" ]:
			handle_getscore_message(conn, logged_users [ conn.getpeername() ])
		elif cmd == chatlib.PROTOCOL_CLIENT [ "get_highscore" ]:
			handle_highscore_message(conn)
		elif cmd == chatlib.PROTOCOL_CLIENT [ "get_logged_users" ]:
			handle_logged_message(conn)
		elif cmd == chatlib.PROTOCOL_CLIENT [ "get_question" ]:
			handle_question_message(conn)
		elif cmd == chatlib.PROTOCOL_CLIENT [ "send_answer" ]:
			handle_answer_message(conn, logged_users [ conn.getpeername() ], data)
		else:
			send_error(conn, chatlib.PROTOCOL_SERVER [ "failed_msg" ])


def hendle_clients_req_res():
	global users
	global questions
	global messages_to_send
	global logged_users
	# global logged_users
	
	load_user_database()
	questions = load_questions()
	print("Welcome to Trivia Server!")
	print("Setting up server.....")
	server_socket = setup_socket()
	client_sockets = [ ]
	while True:
		ready_to_read, ready_to_write, in_error = select.select(
			[ server_socket ] + client_sockets, [ ], [ ]
		)
		for current_socket in ready_to_read:
			if current_socket is server_socket:
				(client_socket, client_address) = current_socket.accept()
				print("New client joined", client_address)
				client_sockets.append(client_socket)
			else:
				cmd, data = recv_message_and_parse(current_socket)
				if cmd == chatlib.PROTOCOL_CLIENT [ "logout_msg" ] or cmd == None:
					print(f"Client disconnect| username={data}, connection={current_socket}")
					if cmd != None:
						handle_client_message(current_socket, cmd, data)
					else:
						client_sockets.remove(current_socket)
						logged_users = {key: val for key, val in logged_users.items() if
						                key != current_socket.getpeername()}
						current_socket.close()
						continue
					client_sockets.remove(current_socket)
					current_socket.close()
				else:
					handle_client_message(current_socket, cmd, data)
		for client in messages_to_send:
			try:
				client [ 0 ].send(client [ 1 ].encode())
				messages_to_send.remove(client)
			except:
				continue


hendle_clients = threading.Thread(target=hendle_clients_req_res)


def check_for_kill():
	exit_event.set()


def main():
	hendle_clients.start()


if __name__ == "__main__":
	main()
