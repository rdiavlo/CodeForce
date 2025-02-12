contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)

contents = [[int(i) for i in j.split(" ")] for index_, j in enumerate(contents[1:]) if index_%2 != 0]

def get_moves(inp_list):
	copy_ip_list = inp_list.copy()

	result_list = []
	move_counter = 0
	for i in range(len(inp_list)):
		if i % 2 == 0:
			to_find_even = True
		else:
			to_find_even = False

		for ii in copy_ip_list:
			if to_find_even:
				if ii % 2 == 0:
					copy_ip_list.remove(ii)
					result_list.append(ii)
					break
				else:
					move_counter += 1
			else:
				if ii % 2 != 0:
					copy_ip_list.remove(ii)
					result_list.append(ii)
					break
				else:
					move_counter += 1
	print(result_list)
	return move_counter

def updated_counter(ip_list):
	res = [1 if ((i%2==0) and (number%2!=0)) else 0 for i, number in enumerate(ip_list) if i%2 == 0]
	return sum(res)


def get_no_of_odd_even(inp_lis):
	even_counter, odd_counter = 0, 0
	for i in inp_lis:
		if i%2 == 0:
			even_counter += 1
		else:
			odd_counter += 1
	return even_counter, odd_counter

for v in contents:
	length_of_list = len(v)
	expected_even, expected_odd = (length_of_list // 2) + (length_of_list%2), length_of_list // 2
	real_even, real_odd = get_no_of_odd_even(v)
	if (expected_even == real_even) and (expected_odd == real_odd):
		moves = updated_counter(v)
		print(moves)
	else:
		print(-1)