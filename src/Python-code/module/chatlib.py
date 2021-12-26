# Protocol Constants

CMD_FIELD_LENGTH = 16  # Exact length of cmd field (in bytes)
LENGTH_FIELD_LENGTH = 4  # Exact length of length field (in bytes)
MAX_DATA_LENGTH = (
    10 ** LENGTH_FIELD_LENGTH - 1
)  # Max size of data field according to protocol
MSG_HEADER_LENGTH = (
    CMD_FIELD_LENGTH + 1 + LENGTH_FIELD_LENGTH + 1
)  # Exact size of header (CMD+LENGTH fields)
MAX_MSG_LENGTH = MSG_HEADER_LENGTH + MAX_DATA_LENGTH  # Max size of total message
DELIMITER = "|"  # Delimiter character in protocol
DATA_DELIMITER = "#"  # Delimiter in the data part of the message

# Protocol Messages
# In this dictionary we will have all the client and server command names

PROTOCOL_CLIENT = {
    "login_msg": "LOGIN",
    "create_account_msg": "CREATEACCOUNT",
    "logout_msg": "LOGOUT",
    "get_score": "MY_SCORE",
    "get_highscore": "HIGHSCORE",
    "get_logged_users": "LOGGED",
    "get_question": "GET_QUESTION",
    "send_answer": "SEND_ANSWER",
}  # .. Add more commands if needed

PROTOCOL_SERVER = {
    "login_ok_msg": "LOGIN_OK",
    "create_account_ok_msg": "CREATEACCOUNT_OK",
    "failed_msg": "ERROR",
    "your_score_msg": "YOUR_SCORE",
    "send_logged_users": "LOGGED_ANSWER",
    "send_question": "YOUR_QUESTION",
    "correct_answer": "CORRECET_ANSWER",
    "wrong_answer": "WRONG_ANSWER",
    "all_score": "ALL_SCORE",
}  # ..  Add more commands if needed

# Other constants

ERROR_RETURN = None  # What is returned in case of an error


def build_message(cmd, data):
    """
    Gets command name (str) and data field (str) and creates a valid protocol message
    Returns: str, or None if error occured
    """
    check_cmd = 0
    for cmd_protocol_client_key in PROTOCOL_CLIENT.keys():
        for cmd_protocol_server_key in PROTOCOL_SERVER.keys():
            if (
                cmd == PROTOCOL_CLIENT[cmd_protocol_client_key]
                or cmd == PROTOCOL_SERVER[cmd_protocol_server_key]
            ):
                check_cmd = 1
    if check_cmd != 1:
        return None
    if len(data) > MAX_DATA_LENGTH:
        return None
    if len(str(len(data))) > 9999:
        return None
    full_msg = ""
    full_msg = cmd + (" " * (CMD_FIELD_LENGTH - len(cmd))) + "|"
    full_msg += str(len(data)).zfill(LENGTH_FIELD_LENGTH) + "|"
    full_msg += data
    return full_msg


def parse_message(data):
    """
    Parses protocol message and returns command name and data field
    Returns: cmd (str), data (str). If some error occured, returns None, None
    """
    if len(data) > MAX_MSG_LENGTH:
        return None, None
    data_parts = data.split("|")
    if len(data_parts) != 3:
        return None, None
    if len(data_parts[0]) + len(data_parts[1]) + 2 > MSG_HEADER_LENGTH:
        return None, None

    cmd = data_parts[0].rstrip()
    cmd = cmd.lstrip()

    size = data_parts[1].lstrip()
    size = size.rstrip()
    try:
        size = int(size)
    except:
        return None, None

    msg = data_parts[2]

    if size != len(msg):
        return None, None

    return cmd, msg


def split_data(msg, expected_fields):
    """
    Helper method. gets a string and number of expected fields in it. Splits the string
    using protocol's data field delimiter (|#) and validates that there are correct number of fields.
    Returns: list of fields if all ok. If some error occured, returns None
    """
    count_fields = msg.count(DATA_DELIMITER)
    if count_fields + 1 == expected_fields:
        return msg.split(DATA_DELIMITER)
    else:
        return None


def join_data(msg_fields):
    """
    Helper method. Gets a list, joins all of it's fields to one string divided by the data delimiter.
    Returns: string that looks like cell1#cell2#cell3
    """
    return "#".join(msg_fields)
