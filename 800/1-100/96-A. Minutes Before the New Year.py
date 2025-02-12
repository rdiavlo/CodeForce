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
res = [((24 - i[0] - 1)*60) + (60-i[1]) for i in contents]

for r in res:
	print(r)