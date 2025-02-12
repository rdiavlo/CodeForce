contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)

contents = contents[1:]


def break_it_down(number_str):

	non_zero_string = number_str.replace("0", "")
	non_zero_list = list(non_zero_string)

	acc = ""
	acc += str(len(non_zero_list))
	acc += "\n"
	for i, j in enumerate(number_str):

		if j != "0":
			repetitions = len(number_str) - 1 - i
			acc += j + ("0"*repetitions)
			acc += " "

	return acc

for i in contents:
	res = break_it_down(i)
	print(res)