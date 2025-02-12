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
contents = [i.split(" ") for i in contents]
# print(contents)

t_list = []
for i in contents:
	a, b = i[0], i[1]
	a, b = int(a), int(b)
	res = a % b
	if res == 0:
		t_list.append(0)
	else:
		t_list.append(b - res)

for i in t_list:
	print(i)
