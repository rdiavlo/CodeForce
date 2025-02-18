contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)

contents = [[int(i) for i in j.split(" ")] for j in contents]
# print(contents)

from collections import Counter

number_of_elements_constraint = contents[0][1]
dict_counter = dict(Counter(contents[1]))
# print(dict_counter)
unique_vals_sorted = list(dict_counter.keys())
unique_vals_sorted.sort()

success_condition = False
if number_of_elements_constraint == 0:
	if min(unique_vals_sorted) > 1:
		print(min(unique_vals_sorted)-1)
		success_condition = True
else:
	acc = 0
	if contents[0][0] >= number_of_elements_constraint:
		for i in unique_vals_sorted:
			count_of_val = dict_counter[i]
			if acc + count_of_val == number_of_elements_constraint:
				success_condition = True
				print(i)
				break
			else:
				acc += count_of_val

if not success_condition:
	print(-1)
