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

grouping_list = []
for i in contents:
	t_list = []
	prev_element = None
	for ii in i:
		if len(t_list) == 0:
			if ii == 0:
				t_list.append(1)
			else:
				t_list.append(-1)
			prev_element = ii
		else:
			if prev_element == ii:
				if ii == 0:
					t_list[-1] = t_list[-1] + 1
				else:
					t_list[-1] = t_list[-1] - 1
			else:
				prev_element = ii
				if ii == 0:
					t_list.append(1)
				else:
					t_list.append(-1)

	grouping_list = t_list
# print(grouping_list, "\n=================\n")

import itertools
if len(grouping_list) != 1:
	max_sum = None
	index_bounds_real = []
	for index_i, val in enumerate(grouping_list):
		if val > 0:
			# print(val)
			index_bounds = [index_i, index_i]

			# check if space is there to the right of this element
			right_list = grouping_list[index_i+1:]
			if len(right_list) >= 2:
				cum_sum_list = list(itertools.accumulate(right_list))
				max_of_cum_list = max(cum_sum_list)
				if max_of_cum_list > 0:
					index_of_max = cum_sum_list.index(max_of_cum_list)
					index_bounds[-1] = index_i + index_of_max + 1

			# check if there is space to the left of this element
			left_list = grouping_list[:index_i]
			left_list = left_list[::-1]
			if len(left_list) >= 2:
				cum_sum_list = list(itertools.accumulate(left_list))
				max_of_cum_list = max(cum_sum_list)
				if max_of_cum_list > 0:
					index_of_max = cum_sum_list.index(max_of_cum_list)
					index_of_max = len(left_list) - (index_of_max + 1)
					index_bounds[0] = index_of_max

			# print("\t", left_list, right_list)
			# print("\t", index_bounds)

			max_slice = grouping_list[index_bounds[0]:index_bounds[1]+1]
			if max_sum is None:
				max_sum = val
				index_bounds_real = index_bounds
			else:
				if sum(max_slice) > max_sum:
					max_sum = sum(max_slice)
					index_bounds_real = index_bounds

	grouping_inversion = grouping_list[index_bounds_real[0]: index_bounds_real[1] + 1]
	grouping_inversion = [i if i > 0 else 0 for i in grouping_inversion]
	# print(max_sum, index_bounds_real, grouping_inversion)
	# print("=============\n")

	final_list = grouping_inversion
	if index_bounds_real[0] != 0:
		final_list = [-i if i < 0 else 0 for i in grouping_list[:index_bounds_real[0]]] + final_list
	if index_bounds_real[1] != (len(grouping_list) - 1):
		final_list = final_list + [-i if i < 0 else 0 for i in grouping_list[index_bounds_real[1]+1:]]

	# print(final_list)
	print(sum(final_list))



else:
	if grouping_list[0] > 0:
		print(grouping_list[0])
	else:
		print(abs(grouping_list[0]) - 1)
