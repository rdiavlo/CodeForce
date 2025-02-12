
import itertools
import math

contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)


contents = [int(i) for i in contents[0].split(" ")]
# print(contents)
max_sum = max(contents)

sample_space = list(range(1, 7))
length_of_sample_space = len(sample_space)
# print(sample_space)
number_of_elements_greater_or_equal_to_max_sum = [i for i in sample_space if i >= max_sum]
length_of_event = len(number_of_elements_greater_or_equal_to_max_sum)
# print("check-1", length_of_event, length_of_sample_space)


def check_if_prime(n):
	max_val = math.sqrt(n)
	if max_val.is_integer():
		return False
	max_val = math.ceil(max_val)

	# print(n, max_val)
	if n == 0:
		return False
	elif n == 1:
		return True
	for i in range(2, max_val):
		if n % i == 0:
			return False
	return True


def break_2_numbers_into_simplest_ratio(a, b):
	for i in [a, b]:
		if i in [0, 1, 2]:
			return a, b

	max_factor_a, max_factor_b = math.floor(math.sqrt(a)), math.floor(math.sqrt(b))
	divider = 2
	while not (check_if_prime(a) or check_if_prime(b)):

		if (a % divider == 0) and (b % divider == 0):
			while (a % divider == 0) and (b % divider == 0):
				a, b = a // divider, b // divider
		else:
			divider += 1

		if divider > min(max_factor_a, max_factor_b):
			break

	return a, b


length_of_event, length_of_sample_space = break_2_numbers_into_simplest_ratio(length_of_event, length_of_sample_space)


if (length_of_sample_space % length_of_event) == 0:
	denom = length_of_sample_space // length_of_event
	print("1/" + str(denom))
else:
	print(str(length_of_event) + "/" + str(length_of_sample_space))
