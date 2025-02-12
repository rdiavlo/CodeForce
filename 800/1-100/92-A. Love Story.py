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
val = [len([1 for a, b in zip(i, "codeforces") if a != b]) for i in contents]
for v in val:
	print(v)