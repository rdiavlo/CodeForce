contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)

s, t = contents[0], contents[1]

# print(s, t)

def break_the_string(wrd):

	prevous_character = None
	temp_list = []
	for i in wrd:
		if prevous_character is None:
			temp_list.append(i)
			prevous_character = i
		else:
			if i == prevous_character:
				temp_list[-1] = temp_list[-1] + i
			else:
				temp_list.append(i)
				prevous_character = i
	return temp_list


broken_str = break_the_string(t)
# print(broken_str)

len_list = [len(i) for i in broken_str]
# print(len_list)

moves = sum(len_list) - len(len_list)
print(moves)
