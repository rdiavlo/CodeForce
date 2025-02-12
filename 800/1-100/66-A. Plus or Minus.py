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
contents = [[int(i) for i in j] for j in contents]


def get_equation(list_ip):
	if list_ip[0] + list_ip[1] == list_ip[2]:
		print("+")
	else:
		print("-")

for i in contents:
	get_equation(i)