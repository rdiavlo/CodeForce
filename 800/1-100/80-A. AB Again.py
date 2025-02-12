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
contents = [sum(list(map(int, list(i)))) for i in contents]
# print(contents)

for i in contents:
	print(i)