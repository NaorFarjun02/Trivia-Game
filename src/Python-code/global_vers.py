from user import User

global LOGIN_STATUS  # user login status

windows_indexes = {
    "home": 0,
    "login": 1,
    "create": 2,
    "game": 3,
    "profile": 4,
    "scoretable": 5,
    "shop": 6,
    "settings": 27,
}  # A list of all the indexes of each page

masteruser = User("81102", "81102", "81102", 999999)
users = [masteruser]
