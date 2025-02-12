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

has_colored = [any([True if i not in ["W", "B", "G"] else False for i in j.split(" ")]) for j in contents]
# print(has_colored)
a = [0, 1, 2]

if any(has_colored):
	print("#Color ")
else:
	print("#Black&White ")
