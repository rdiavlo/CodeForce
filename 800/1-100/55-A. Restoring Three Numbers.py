contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)


contents = contents[0]
contents = contents.split(" ")
contents = [int(i) for i in contents]

e4 = max(contents)
contents.sort()
a = e4 - contents[0]
b = contents[1] - a
c = contents[2] - a

print(f"{a} {b} {c}")
