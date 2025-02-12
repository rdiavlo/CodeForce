contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)

contents = [val for i, val in enumerate(contents) if i % 2 != 0]
contents = [i.split(" ") for i in contents]
contents = [[int(i) for i in j] for j in contents]
