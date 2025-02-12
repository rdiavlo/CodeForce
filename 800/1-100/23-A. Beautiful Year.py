contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)

val = contents[0]


def check_if_number_feasible(left_most_digit, left_digits_set):
	remaining_digits = set(list(range(left_most_digit+1, 10)))
	# print("c1", remaining_digits)
	if len(remaining_digits) > 0:
		feasible_elements = remaining_digits.difference(left_digits_set)
		# print("c2", feasible_elements)
		if len(feasible_elements) > 0:
			return min(feasible_elements)
	return -1


# ensure all elements unique
# for all elements with duplicates, skip the first. iterate over remaining adding n to them
def remove_duplicates(num_string):

	original_str_list = list(num_string)
	num_str_list = list(num_string)

	already_looped_elements = []
	detected_duplicates = False
	for p, i in enumerate(num_string):
		integer_val = int(i)
		print(already_looped_elements)
		if integer_val in already_looped_elements:
			detected_duplicates = True
			if detected_duplicates:
				val_to_update_with = integer_val + 1

			while val_to_update_with in already_looped_elements:
				val_to_update_with += 1
			already_looped_elements.append(val_to_update_with)
			num_str_list[p] = str(val_to_update_with)
		else:
			already_looped_elements.append(integer_val)

	if original_str_list == num_str_list:
		return False, ''.join(num_str_list)
	return True, ''.join(num_str_list)


# check for and remove duplicate
duplicates_are_removed, val = remove_duplicates(val)
if duplicates_are_removed:
	print(val)
else:
	# keep moving to the left until you find a viable candidate
	index_to_update_from = None
	new_val = None
	for i in range(3, -1, -1):
		rem_digits_list = [int(j) for j in val[:i]]
		rem_digits = set(rem_digits_list)
		digit = int(val[i])

		# print(digit, rem_digits)
		number_feasible = check_if_number_feasible(digit, rem_digits)
		if number_feasible != -1:
			new_val = val[:i] + str(number_feasible)
			# print(new_val, number_feasible)
			if i != 3:
				 new_val += val[i+1:]
				 # once candidate is found fill in the right
				 possible_elements = {0, 1, 2, 3}
				 possible_right_fill = possible_elements.difference({int(new_val[0])})
				 possible_right_fill = list(possible_right_fill)
				 possible_right_fill.sort()
				 possible_right_fill = [str(i) for i in possible_right_fill]
				 print(new_val[0] + ''.join(possible_right_fill))
			else:
				 print(new_val)

			break
