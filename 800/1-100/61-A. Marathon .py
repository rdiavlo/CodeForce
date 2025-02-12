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

def get_number_of_participants_ahead(list_ip):
	timur, rest = list_ip[0], list_ip[1:]
	ahead = [i for i in rest if i > timur]
	return len(ahead)

for i in contents:
	res = get_number_of_participants_ahead(i)
	print(res)
