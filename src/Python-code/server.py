##############################################################################
# server.py
##############################################################################

import socket
import select
from module import chatlib
import random


# GLOBALS
messages_to_send = []
users = {}
questions = {}
logged_users = {}  # a dictionary of client hostnames to usernames - will be used later

ERROR_MSG = "Error! "
SERVER_PORT = 5555
SERVER_IP = "0.0.0.0"
MAX_MSG_LENGTH = 1024


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
            "question": "How much is 2+2",
            "answers": ["3", "4", "2", "1"],
            "correct": 2,
        },
        2: {
            "question": "What is the capital of France?",
            "answers": ["Lion", "Marseille", "Paris", "Montpellier"],
            "correct": 3,
        },
        3: {
            "question": "What is the capital of Israel?",
            "answers": ["Lion", "Marseille", "Paris", "Jerusalem"],
            "correct": 4,
        },
        4: {
            "question": "How many letters are in the English language?",
            "answers": ["26", "32", "43", "23"],
            "correct": 1,
        },
    }
    return questions


def load_user_database():
    """
    Loads users list from file	## FILE SUPPORT TO BE ADDED LATER
    Recieves: -
    Returns: user dictionary
    """
    users = {
        "test": {"password": "test", "score": 40, "questions_asked": []},
        "yossi": {"password": "123", "score": 50, "questions_asked": []},
        "master": {"password": "master", "score": 200, "questions_asked": []},
    }
    return users


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
    build_and_send_message(conn, chatlib.PROTOCOL_SERVER["failed_msg"], error_msg)


##### MESSAGE HANDLING


def handle_logged_message(conn):
    global logged_users
    msg = ""
    for user in logged_users.keys():
        msg += "" + logged_users[user] + ","
    msg = msg[:-1]
    build_and_send_message(conn, chatlib.PROTOCOL_SERVER["send_logged_users"], msg)


def handle_getscore_message(conn, username):
    global users
    user_score = str(users[username]["score"])
    build_and_send_message(conn, chatlib.PROTOCOL_SERVER["your_score_msg"], user_score)


# take second element for sort
def takeSecond(elem):
    return elem[1]


def handle_highscore_message(conn):

    global users
    score_table = []
    for user in users.keys():
        user_score = [user, users[user]["score"]]
        score_table.append(user_score)
    score_table.sort(key=takeSecond, reverse=True)
    msg = ""
    for score in score_table:
        msg += score[0] + ": " + str(score[1]) + "\n"
    build_and_send_message(conn, chatlib.PROTOCOL_SERVER["all_score"], msg)


def create_ramdon_quetion():
    global questions
    quetion_id = random.choice(list(questions.keys()))
    question = questions[quetion_id]["question"]
    answers = "#".join(questions[quetion_id]["answers"])
    correct = questions[quetion_id]["correct"]
    msg_fields = [str(quetion_id), question, answers, str(correct)]
    return chatlib.join_data(msg_fields)


def handle_question_message(conn):
    question = create_ramdon_quetion()
    build_and_send_message(conn, chatlib.PROTOCOL_SERVER["send_question"], question)


def handle_answer_message(conn, username, answer):
    global users
    global questions
    global logged_users

    answer = chatlib.split_data(answer, 2)
    if int(answer[1]) == questions[int(answer[0])]["correct"]:
        build_and_send_message(conn, chatlib.PROTOCOL_SERVER["correct_answer"], "")
        users[username]["score"] += 5
    else:
        build_and_send_message(
            conn,
            chatlib.PROTOCOL_SERVER["wrong_answer"],
            str(questions[int(answer[0])]["correct"]),
        )


def handle_logout_message(conn):
    """
    Closes the given socket (in laster chapters, also remove user from logged_users dictioary)
    Recieves: socket
    Returns: None
    """
    global logged_users

    logged_users.pop(conn.getpeername())
    conn.close()


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
    if data[0] in users.keys():
        if conn.getpeername() not in logged_users.keys():
            if data[1] == users[data[0]]["password"]:
                login_status = 1
                build_and_send_message(
                    conn, chatlib.PROTOCOL_SERVER["login_ok_msg"], ""
                )
            else:
                login_status = -1
                send_error(conn, "Username or password incorrect")
        else:
            login_status = -1
            send_error(conn, "This user is already logged in to the game")
    else:
        login_status = -1
        send_error(conn, "Username or password incorrect")
    if login_status == 1:
        logged_users[conn.getpeername()] = data[0]
        return data[0]


def handle_createaccount_message(conn, data):
    # global users  # This is needed to access the same users dictionary from all functions

    data = chatlib.split_data(data, 5)
    if data == None:
        return
    build_and_send_message(
        conn, chatlib.PROTOCOL_SERVER["create_account_ok_msg"], str(data)
    )


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
        if cmd == chatlib.PROTOCOL_CLIENT["login_msg"]:
            username = handle_login_message(conn, data)
        elif cmd == chatlib.PROTOCOL_CLIENT["create_account_msg"]:
            handle_createaccount_message(conn,data)
        else:
            send_error(conn, chatlib.PROTOCOL_SERVER["failed_msg"])
    else:
        if cmd == chatlib.PROTOCOL_CLIENT["logout_msg"]:
            handle_logout_message(conn)
        elif cmd == chatlib.PROTOCOL_CLIENT["get_score"]:
            handle_getscore_message(conn, logged_users[conn.getpeername()])
        elif cmd == chatlib.PROTOCOL_CLIENT["get_highscore"]:
            handle_highscore_message(conn)
        elif cmd == chatlib.PROTOCOL_CLIENT["get_logged_users"]:
            handle_logged_message(conn)
        elif cmd == chatlib.PROTOCOL_CLIENT["get_question"]:
            handle_question_message(conn)
        elif cmd == chatlib.PROTOCOL_CLIENT["send_answer"]:
            handle_answer_message(conn, logged_users[conn.getpeername()], data)
        else:
            send_error(conn, chatlib.PROTOCOL_SERVER["failed_msg"])


def main():

    # Initializes global users and questions dicionaries using load functions, will be used later
    global users
    global questions
    global messages_to_send
    # global logged_users

    users = load_user_database()
    questions = load_questions()
    print("Welcome to Trivia Server!")
    print("Setting up server.....")
    server_socket = setup_socket()
    client_sockets = []
    while True:
        ready_to_read, ready_to_write, in_error = select.select(
            [server_socket] + client_sockets, [], []
        )
        for current_socket in ready_to_read:
            if current_socket is server_socket:
                (client_socket, client_address) = current_socket.accept()
                print("New client joined", client_address)
                client_sockets.append(client_socket)
            else:
                cmd, data = recv_message_and_parse(current_socket)
                if cmd == chatlib.PROTOCOL_CLIENT["logout_msg"] or cmd == None:
                    print(f"Client disconnect| username={data}")
                    if cmd != None:
                        handle_client_message(current_socket, cmd, data)
                    else:
                        client_sockets.remove(current_socket)
                        current_socket.close()
                        continue
                    client_sockets.remove(current_socket)
                    current_socket.close()
                else:
                    handle_client_message(current_socket, cmd, data)
        for client in messages_to_send:
            try:
                client[0].send(client[1].encode())
                messages_to_send.remove(client)
            except:
                continue


# Implement code ...


if __name__ == "__main__":
    main()
