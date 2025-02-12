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

max_v = max(contents)
welfare = (max_v * len(contents)) - sum(contents)
print(welfare)

