contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)

contents = contents[0].split(" ")
contents = [int(i) for i in contents]
rows, columns = contents[0], contents[1]

for i in range(rows):
	mod_index = i + 1

	if mod_index % 4 == 0:
		print("#" + "."*(columns-1))
	elif mod_index % 2 == 0:
		print("." * (columns - 1) + "#")
	else:
		print("#" * columns)