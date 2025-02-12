contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)


contents = [i.split(" ") for i in contents[1:]][0]
contents = [int(i) for i in contents]
# print(contents)

res = sum(contents)

if res > 0:
	print("HARD")
else:
	print("EASY")


