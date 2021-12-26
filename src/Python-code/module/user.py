from datetime import datetime


class User:
    def create_date(self):
        cd = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        return cd

    def getEmail(self):
        return self.email
    def setEmail(self,email):
        self.email=email

    def getUsername(self):
        return self.username
    def setUsername(self,username):
        self.username=username

    def getPassword(self):
        return self.password
    def setPassword(self,password):
        self.password=password

    def getDate(self):
        return self.create_date
    
    def getScore(self):
        return self.score
    def setScore(self,score):
        self.score=score

    def __init__(self, email, username, password,score):
        self.setEmail(email)
        self.setPassword(password)
        self.setUsername(username)
        self.setScore(score)
        self.create_date = self.create_date()

