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
contents = [[v for i, v in enumerate(j) if i % 2 == 0] + [j[-1]] if (len(j) > 2) else j for j in contents]
contents = [''.join(i) if (type(i) is list) else i for i in contents ]
# print(contents)
for i in contents:
	print(i)