contents = []
import traceback
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)

contents = contents[1:]
contents = [sorted([int(j) for j in i.split(" ")])[1] for i in contents]
# print(contents)

for i in contents:
	print(i)

