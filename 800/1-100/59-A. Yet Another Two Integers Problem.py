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

def check_moves(list_ip):
	diff = abs(list_ip[1] - list_ip[0])
	tens = diff // 10
	rem = diff % 10
	# print(rem)

	number_of_moves = tens
	if rem != 0:
		number_of_moves += 1
	return number_of_moves

for i in contents:
	res = check_moves(i)
	print(res)