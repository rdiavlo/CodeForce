contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)

contents = [[int(i) for i in j.split(" ")] for j in contents[1:]]
contents = [i[1] - i[0] for i in contents]

for v in contents:
	print(v)