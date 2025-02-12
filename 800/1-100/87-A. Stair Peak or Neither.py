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
	v = i.split(" ")
	v = [int(a) for a in v]
	a, b, c = tuple(v)
	if a < b:
		if b < c:
			print("STAIR")
		elif b > c:
			print("peak".upper())
		else:
			print("NONE")
	else:
		print("NONE")
