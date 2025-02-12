contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)

contents = [[int(j) for j in val.split(" ")] for i, val in enumerate(contents[1:]) if (i%2 != 0)]
# print(contents)

val = [max(i) - min(i) for i in contents]
for v in val:
	print(v)