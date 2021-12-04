import socket
import sys
import chatlib  # To use chatlib functions or consts, use chatlib.****

SERVER_IP = "46.116.103.161"  # Our server will run on same computer as client
SERVER_PORT = 5555
ERROR = "ERROR"
OK = "OK"
MAX_MSG_LENGTH = 1024
USERNAME = ""

# HELPER SOCKET METHODS


class Message_too_long(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "The message is to long"


def build_and_send_message(conn, code, data):
    """
    Builds a new message using chatlib, wanted code and message.
    Prints debug info, then sends it to the given socket.
    Paramaters: conn (socket object), code (str), data (str)
    Returns: Nothing
    """
    full_msg = chatlib.build_message(code, data)
    if len(full_msg) > MAX_MSG_LENGTH:
        raise Message_too_long()
    conn.send(full_msg.encode())


def recv_message_and_parse(conn):
    """
    Recieves a new message from given socket,
    then parses the message using chatlib.
    Paramaters: conn (socket object)
    Returns: cmd (str) and data (str) of the received message.
    If error occured, will return None, None
    """
    full_msg = conn.recv(1024).decode()
    cmd, data = chatlib.parse_message(full_msg)
    return cmd, data


def bulid_send_recv_parse(conn, code, data):
    """
    Builds a new message using chatlib, wanted code and message,
    and recieves a new message from given socket,
    then parses the message using chatlib.
    Paramaters: conn (socket object), code (str), data (str)
    Returns: cmd (str) and data (str) of the received message.
    """
    build_and_send_message(conn, code, data)
    cmd, data = recv_message_and_parse(conn)
    return cmd, data


def get_score(conn):
    """
    Sends a message to the server and requests the user's current score
    Paramaters: conn (socket object)
    Returns: Nothing
    """
    cmd, data = bulid_send_recv_parse(conn, chatlib.PROTOCOL_CLIENT["get_score"], "")
    print("Your score: " + data)


def gethighscore(conn):
    """
    Sends a message to the server and requests the current score of all users
    Paramaters: conn (socket object)
    Returns: Nothing
    """
    cmd, data = bulid_send_recv_parse(
        conn, chatlib.PROTOCOL_CLIENT["get_highscore"], ""
    )
    print(data)


def print_question(data):
    data = chatlib.split_data(data, 7)
    print()
    print("Q: " + data[1])
    for i in range(2, 6):
        print("|%s|   %s" % (str(i - 1), data[i]))
    return data[0]


def play_question(conn):
    """
    Requests a question from the server, prints the question,
    gets an answer from the user, prints whether right or not and the correct answer
    Paramaters: conn (socket object)
    Returns: Nothing
    """
    cmd, data = bulid_send_recv_parse(conn, chatlib.PROTOCOL_CLIENT["get_question"], "")
    question_id = print_question(data)
    player_choise = ""
    while player_choise not in ["1", "2", "3", "4"]:
        player_choise = str(input("Please enter your choice: "))
    cmd, data = bulid_send_recv_parse(
        conn,
        chatlib.PROTOCOL_CLIENT["send_answer"],
        chatlib.join_data([question_id, player_choise]),
    )
    if data == "":
        print("YES!!!")
    elif len(data) == 1:
        print("Nope, correct answer is |%s|" % data)


def get_logged_users(conn):
    cmd, data = bulid_send_recv_parse(
        conn, chatlib.PROTOCOL_CLIENT["get_logged_users"], ""
    )
    print("Logged users:\n%s" % data)


def connect():
    """
    Establishes a connection with the server and returns a socket ready for communication
    Paramaters: Nothing
    Returns: Nothing
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create socket
    client_socket.connect((SERVER_IP, SERVER_PORT))  # connect to server
    return client_socket


def error_and_exit(error_msg):
    print(error_msg)
    exit


def login(conn):
    cmd = ""
    global USERNAME
    while cmd != chatlib.PROTOCOL_SERVER["login_ok_msg"]:
        try:
            USERNAME = input("Please enter username: \n")  # get username
            password = input("Please enter password: \n")  # get password
        except KeyboardInterrupt:
            return ERROR
        try:
            build_and_send_message(
                conn,
                chatlib.PROTOCOL_CLIENT["login_msg"],
                chatlib.join_data([USERNAME, password]),
            )  # build the message and sent it to the server
        except Message_too_long:
            return ERROR

        cmd, data = recv_message_and_parse(conn)  # get an answer ffrom the server
        if cmd == chatlib.PROTOCOL_SERVER["login_ok_msg"]:
            print("Login successfully")
        elif cmd == chatlib.PROTOCOL_SERVER["failed_msg"]:
            print(data)
    return OK


def logout(conn):
    global USERNAME
    build_and_send_message(
        conn, chatlib.PROTOCOL_CLIENT["logout_msg"], USERNAME
    )  # send a logout message
    cmd, data = recv_message_and_parse(conn)  # get an answer from the server
    print(data)


def menu(conn):
    choice = 0
    while choice != 5:
        print("Trivia Menu: ")
        print("1.   Playb a trivia question")
        print("2.   Get my score")
        print("3.   Get high scores")
        print("4.   Get logged users")
        print("5.   Quit")
        choice = int(input("Please enter your choice: "))
        if choice == 1:
            play_question(conn)
        elif choice == 2:
            get_score(conn)
        elif choice == 3:
            gethighscore(conn)
        elif choice == 4:
            get_logged_users(conn)
        elif choice == 5:
            logout(conn)
        else:
            print("Your selection is invalid")


def main():
    try:
        client_sokect = connect()
        login_status = login(client_sokect)
        if login_status == ERROR:
            logout(client_sokect)
            exit()
        menu(client_sokect)
        client_sokect.close()
    except:
        client_sokect.close()
        e = sys.exc_info()
        print(e)


if __name__ == "__main__":
    main()
