contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)

contents = contents[1]
contents = contents.split(" ")
contents = [int(i) for i in contents]

amazing_counter = 0
min, max = contents[0], contents[0]
for i, value in enumerate(contents):
	if i != 0:
		if value > max:
			amazing_counter += 1
			max = value
		elif value < min:
			amazing_counter += 1
			min = value

print(amazing_counter)