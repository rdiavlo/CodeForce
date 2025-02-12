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
contents = [[int(i) for i in j.split(" ")] for j in contents]

def get_k(params):
	x, y, n = tuple(params)
	max_divisible_number = x * (n // x)
	# print(n, max_divisible_number)
	space_left = n - max_divisible_number
	if y > space_left:
		val = max_divisible_number - (x - y)
	else:
		val = max_divisible_number + y
	return val

for i in contents:
	res = get_k(i)
	print(res)