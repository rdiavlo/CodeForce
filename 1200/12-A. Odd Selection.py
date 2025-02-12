
contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)

contents = [[int(i) for i in j.split(" ")] for j in contents[1:]]
# print(contents)


def get_odd_even_counts(ip_list):
	even_counter = 0
	for i in ip_list:
		if i % 2 == 0:
			even_counter += 1
	odd_counter = len(ip_list) - even_counter
	return even_counter, odd_counter


for i in range(len(contents)//2):
	start_index = 2*i
	context = contents[start_index: start_index+2]
	x = context[0][1]
	vals = context[1]
	# print(x, vals)

	evens, odds = get_odd_even_counts(vals)
	# print(evens, odds)
	if evens == 0:
		if x % 2 == 0:
			print("NO")
			continue

	if odds > 0:
		if 1 + evens >= x:
			print("YES")
			continue
		else:
			if odds % 2 != 0:
				max_numbers = odds + evens
			else:
				max_numbers = odds - 1 + evens

			if max_numbers >= x:
				print("YES")
				continue

	print("NO")