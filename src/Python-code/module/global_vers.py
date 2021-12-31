from module.user import User
from PyQt5.QtWidgets import QMessageBox

global LOGIN_STATUS  # user login status

conn = ""

windows_indexes = {
    "home": 0,
    "login": 1,
    "create": 2,
    "profile": 3,
    "game": 4,
    "scoretable": 5,
    "shop": 6,
    "settings": 27,
}  # A list of all the indexes of each page

user=None

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
