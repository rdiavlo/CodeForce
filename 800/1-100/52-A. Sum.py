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
	val = i.split(" ")
	val = [int(i) for i in val]
	val.sort()
	if sum(val) == 2 * max(val):
		print("Yes")
	else:
		print("No")

