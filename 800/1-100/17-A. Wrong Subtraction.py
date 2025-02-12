
usr = input()
number, attempts = usr.split()
number, attempts = number, int(attempts)
nos = [int(i) for i in number]


import time
def transform_inp():
	attempts_v = attempts
	transf_list = nos[:]
	while attempts_v != 0:
		# print(transf_list, attempts_v)

		digit = transf_list[-1]

		if digit >= attempts_v:
			transf_list[-1] = digit - attempts_v
			attempts_v = 0
		else:
			attempts_v = attempts_v - digit

			transf_list = transf_list[:-1]
			attempts_v -= 1

		# time.sleep(0.2)
	transf_list = [str(i) for i in transf_list]
	print(''.join(transf_list))


transform_inp()