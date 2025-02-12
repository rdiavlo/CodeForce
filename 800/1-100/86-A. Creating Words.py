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

for i in contents:
	a, b = i.split(" ")
	print(b[0] + a[1:] + " " + a[0] + b[1:])