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

contents = [int(i) for i in contents[0].split(" ")]
prime_no, possible_prime = tuple(contents)

prime_found = False
candidate = prime_no + 1
while not prime_found:
	check = check_if_prime(candidate)
	if check:
		prime_found = True
	else:
		candidate += 1
# print(candidate)

if candidate == possible_prime:
	print("YES")
else:
	print("NO")

