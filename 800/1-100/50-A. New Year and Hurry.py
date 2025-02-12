

contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)
contents = contents[0]
contents = contents.split(" ")
contents = [int(i) for i in contents]

time_total = 240

def get_number_of_questions_solved(time_left, questions):
	solved = 0
	for i in range(questions):
		ind = i + 1
		time_consumed = ind * 5

		if time_left >= time_consumed:
			solved += 1
			time_left -= time_consumed
			# print(solved, time_left)
		else:
			return solved
	return solved

transit_time, questions_number = contents[1], contents[0]
pending_time = time_total - transit_time
# print(pending_time)

res = get_number_of_questions_solved(pending_time, questions_number)
print(res)