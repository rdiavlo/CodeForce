contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)


processing_llist = contents
words_list = processing_llist[1:]
# print(words_list)



def check_if_problem_is_solved(string_of_all_3):
	# print(string_of_all_3)
	string_of_all_3 = string_of_all_3.strip()
	solved_status = string_of_all_3.split(" ")
	solved_status = [int(i) for i in solved_status]
	sum_of_ans = sum(solved_status)

	if sum_of_ans >= 2:
		return 1
	return 0


answer_check = list(map(check_if_problem_is_solved, words_list))
# print(answer_check)

number_of_problems_solved = sum(answer_check)
print(number_of_problems_solved)


