contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)


contents = [[int(ii) for ii in i.split(" ")] for index_v, i in enumerate(contents[1:]) if index_v % 2 != 0]
# print(contents)


def return_them_is_misceginated(ip_list):
	unique_elements = list(set(ip_list))
	grouping_sum_dict = {val: [[val]] for val in unique_elements}
	for index_v, i in enumerate(unique_elements):
		if index_v < len(unique_elements) - 1:
			unique_elements_copy = unique_elements[index_v:]
			for ii in unique_elements_copy:
				sum_v = i + ii
				pair_to_add = [i, ii]
				if i == ii:
					pair_to_add = [i]

				if sum_v in grouping_sum_dict:
					grouping_sum_dict[sum_v].append(pair_to_add)
				else:
					grouping_sum_dict[sum_v] = [[i, ii]]
	return grouping_sum_dict


def if_misceginated_retun_max(grouping_sum_dict, count_dict_p):

	max_counter = 0
	for sum_v in grouping_sum_dict:
		pairs = grouping_sum_dict[sum_v]
		local_sum = 0
		for p in pairs:
			if len(p) == 1:
				count = count_dict_p[p[0]]
				local_sum += (count//2)
			else:
				a_count, b_count = count_dict_p[p[0]], count_dict_p[p[1]]
				limiter = min(a_count, b_count)
				local_sum += limiter
		if local_sum > max_counter:
			max_counter = local_sum

	return max_counter


from collections import Counter
for c in contents:
	count_dict = Counter(c)

	count_list = list(count_dict.values())
	count_list.sort()
	max_1 = count_list[-1]

	if len(count_dict) == 1:
		print(max_1//2)
	else:
		max_2 = count_list[-2]

		# case-1: them is misceginated
		check_for_miscegination = return_them_is_misceginated(c)
		# print(check_for_miscegination)
		# print("")
		max_misceginated_couple_count = 0
		if len(check_for_miscegination) > 0:
			max_misceginated_couple_count = if_misceginated_retun_max(check_for_miscegination, count_dict)

		baseline = max_1//2
		possible_candidate = max_2

		showdown_res = max([max_misceginated_couple_count, baseline, possible_candidate])
		print(showdown_res)

