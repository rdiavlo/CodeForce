contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)
contents = contents[0]

contents = contents.split(" ")
contents = [int(i) for i in contents]
contents = tuple(contents)

n, k, l, c, d, p, nl, np = contents

# print(contents)

total_volume = k * l
each_round_volume_consumed = n * nl
drink_res = total_volume // each_round_volume_consumed


total_lime_slices = c * d
line_res = total_lime_slices // n

salt_res = p // (np * n)


# print(line_res, salt_res, drink_res)

list_of_constraints = [line_res, salt_res, drink_res]
print(min(list_of_constraints))
