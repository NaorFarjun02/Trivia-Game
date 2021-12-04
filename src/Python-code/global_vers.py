from user import User

global LOGIN_STATUS  # user login status

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

masteruser = User("1", "1", "1", 999999)
users = [masteruser]
