usr = input()

import string

def check_if_number_is_lucky(number):
	digits = string.digits
	digits = [int(i) for i in digits]

	digits.remove(4)
	digits.remove(7)
	# print(digits)
	# print(number)

	for i in str(number):
		if int(i) in digits:
			return False
	return True


def get_count_of_lucky_digits(number):
	number = [int(i) for i in str(number)]
	counter = 0
	for a in number:
		if (a==4) or (a==7):
			counter += 1
	return counter

val = get_count_of_lucky_digits(usr)
a = check_if_number_is_lucky(val)

if a:
	print("YES")
else:
	print("NO")