contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)

contents = [int(i) for i in contents[1:]]

import math
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

def get_gcd(non_prime_number):
	for i in range(2, 100):
		if non_prime_number % i == 0:
			# print(non_prime_number%i, i)
			return non_prime_number // i
	return 1

def processor(number):

	if number == 1:
		print(1)
		return
	if number == 2:
		print(1)
		return
	if number == 3:
		print(1)
		return
	if number == 4:
		print(2)
		return

	# if number is odd reduce by 1 to facilitate breakdown
	if number % 2 == 1:
		number -= 1

	# # check if number is a perfect square. squares do not show disparity
	# check_for_square = math.sqrt(number)
	# if check_for_square.is_integer():
	# 	number -= 1
	#
	# # get the highest non-prime number
	# check_if_prime_no = check_if_prime(number)
	# counter_reverse = number
	# while check_if_prime_no:
	# 	counter_reverse -= 1
	# 	check_if_prime_no = check_if_prime(counter_reverse)

	# composite number found at this point
	# print(counter_reverse)
	gcd = get_gcd(number)
	print(gcd)

for i in contents:
	processor(i)

