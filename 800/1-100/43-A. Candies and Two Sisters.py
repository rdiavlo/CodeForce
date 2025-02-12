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
contents = [int(i) for i in contents]

def get_number_of_splits(candy_count):
	if candy_count < 3:
		return 0
	else:
		rem = candy_count - 3
		if rem % 2 == 0:
			return int((rem // 2) + 1)
		else:
			return int(((rem - 1) // 2) + 1)

for i in contents:
	res = get_number_of_splits(i)
	print(res)