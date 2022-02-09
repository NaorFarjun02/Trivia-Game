dic = {

}
ques_id = 17
while True:
	ques = (input("enter question: "))
	answer1 = str(input("enter answer 1: "))
	answer2 = str(input("enter answer 2: "))
	answer3 = str(input("enter answer 3: "))
	answer4 = str(input("enter answer 4:"))
	correct = int(input("correct?: "))
	data = {
		"question": ques,
		"answers": [ answer1, answer2, answer3, answer4 ],
		"correct": correct,
	}
	dic [ ques_id ] = data
	ques_id += 1
	print(dic)
