class Score_table:
	
	def add_user_to_list(self, user=None):
		if user == None:
			return
		for u in self.users_score_list:
			if user.getUsername() == u [ "username" ]:
				index = self.users_score_list.index(u)
				self.users_score_list [ index ] = user
				return
		user_data = {"username": user.getUsername(),
		             "uid": user.getUID(),
		             "score": user.getScore(),
		             "wins": 0,
		             "games": 0}
		self.users_score_list.append(user_data)
	
	def __init__(self, ):
		self.users_score_list = [ ]
	
	def __str__(self):
		to_print = ""
		for user in self.users_score_list:
			to_print += user [ "username" ] + "|" + str(user [ "score" ]) + "\n"
		return to_print
