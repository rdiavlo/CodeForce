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
# print(contents)

t_list = []
for i in range(len(contents)):
	t_list.append(contents.index(i + 1) + 1)

t_list = [str(i) for i in t_list]
print(' '.join(t_list))

