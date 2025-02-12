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
contents = [[int(j) for j in i.split(" ")] for i in contents]
contents = [[j[i] + j[(i+1) % 3] for i in range(len(j))] for j in contents]
# print(contents)
contents = ["YES" if max(i) >= 10 else "NO" for i in contents]

# print(contents)
for i in contents:
	print(i)