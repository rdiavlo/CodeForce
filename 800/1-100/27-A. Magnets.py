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
contents = ["A" if i == "10" else "B" for i in contents]
contents = ''.join(contents)
# print(contents)

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

res = break_the_string(contents)
# print(res)
print(len(res))
