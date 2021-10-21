from datetime import datetime


class User:
    def create_date(self):
        cd = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        return cd

    def getEmail(self):
        return self.email

    def getUsername(self):
        return self.username

    def getPassword(self):
        return self.password

    def getDate(self):
        return self.create_date

    def __init__(self, email, username, password):
        self.email = email
        self.password = password
        self.username = username
        self.create_date = self.create_date()
