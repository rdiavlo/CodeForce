contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)

contents = [val for i, val in enumerate(contents[1:]) if (i%2 != 0)]

expected_set = set("Timur")
res = ["YES" if (expected_set==set(i) and len(i)==len(expected_set)) else "NO" for i in contents]
for v in res:
	print(v)