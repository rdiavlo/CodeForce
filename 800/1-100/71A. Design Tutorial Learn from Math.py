contents = []
import traceback
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)

contents = int(contents[0])

import math


def generator_for_breakdown_of_number(number):
	a, b = number // 2, number - (number//2)
	while a > 0:
		yield a, b
		a -= 1
		b += 1


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


number_breakdown_generator = generator_for_breakdown_of_number(contents)
a_is_composite, b_is_composite = False, False
while not (a_is_composite and b_is_composite):
	a, b = next(number_breakdown_generator)

	a_is_composite, b_is_composite = not(check_if_prime(a)), not(check_if_prime(b))
	# print(a_is_composite, b_is_composite)


print(a, b)