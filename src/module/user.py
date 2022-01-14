class User:
	def getUID(self):
		return str(self.uid)
	
	def setUID(self, uid):
		self.uid = uid
	
	def getEmail(self):
		return self.email
	
	def setEmail(self, email):
		self.email = email
	
	def getUsername(self):
		return self.username
	
	def setUsername(self, username):
		self.username = username
	
	def getPassword(self):
		return self.password
	
	def setPassword(self, password):
		self.password = password
	
	def getDate(self):
		return self.create_date
	
	def setData(self, create_date):
		self.create_date = create_date
	
	def getScore(self):
		return self.score
	
	def setScore(self, score):
		self.score = score
	
	def __init__(self, uid, email, username, password, create_data, score=0):
		self.setUID(uid)
		self.setEmail(email)
		self.setPassword(password)
		self.setUsername(username)
		self.setScore(score)
		self.setData(create_data)
	
	def __str__(self):
		return "username:" + self.getUsername() + "\nUID - " + self.getUID() + "\nemail:" + self.getEmail() + "\ncreate date:" + self.getDate()
