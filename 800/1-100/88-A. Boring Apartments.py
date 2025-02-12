contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)

contents = [int(i) for i in contents[1:]]

for i in contents:
	complete_set = 10 * (int(str(i)[0])-1)
	# print(complete_set)

	partial = list(range(1, len(str(i))+1))
	# print(partial)
	partial = sum(partial)

	print(complete_set + partial)