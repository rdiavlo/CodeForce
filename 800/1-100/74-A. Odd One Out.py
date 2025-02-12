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
contents = [[int(i) for i in j.split(" ")] for j in contents]
# print(contents)
contents = [[i for i in set(j) if j.count(i) == 1][0] for j in contents]
for i in contents:
	print(i)