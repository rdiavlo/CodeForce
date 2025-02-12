contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)

contents = [sorted([int(i) for i in j.split(" ")]) for j in contents[1:]]

res = [i[1] if (i[1] >= i[0] * 2) else (2*i[0]) for i in contents]
res = [i**2 for i in res]
for v in res:
	print(v)