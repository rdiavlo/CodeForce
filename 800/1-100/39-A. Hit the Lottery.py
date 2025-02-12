contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)


contents = int(contents[0])
# print(contents)

def get_consumption(val, divisor):
	return val % divisor, val // divisor


balance = contents
steps = 0
for i in [100, 20, 10, 5, 1]:
	a, b = get_consumption(balance, i)
	# print("use ", i, " to get: ", a, b)
	if b != 0:
		balance = a
		steps += b
print(steps)