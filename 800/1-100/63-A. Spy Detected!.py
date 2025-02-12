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
contents = [val for i, val in enumerate(contents) if i % 2 == 1]
contents = [i.split(" ") for i in contents]
contents = [[int(i) for i in j] for j in contents]
# print(contents)

def get_spy_position(list_ip):
	spy_val = None
	unique = set(list_ip)
	# identify max by picking 3 positions
	max_identification = [list_ip[0], list_ip[1], list_ip[2]]
	if max_identification[0] == max_identification[1]:
		b = unique.copy()
		b.remove(max_identification[0])
		spy_val = list(b)[0]
	else:
		if max_identification[0] == max_identification[2]:
			spy_val = max_identification[1]
		else:
			spy_val = max_identification[0]
	# print(spy_val)
	# print("===")
	list_ip = [str(i) for i in list_ip]
	return list_ip.index(str(spy_val)) + 1

for i in contents:
	res = get_spy_position(i)
	print(res)