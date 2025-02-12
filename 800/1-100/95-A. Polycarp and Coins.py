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
res = [[i//3, i//3] if (i%3 == 0) else [i//3, (i//3)+1] if (i%3 == 2) else [(i//3) + 1, i//3] for i in contents]
res = [' '.join([str(j) for j in i]) for i in res]
for r in res:
	print(r)