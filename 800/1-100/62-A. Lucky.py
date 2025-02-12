contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)

contents = contents[1:]

def get_if_lucky_or_not(number_str):
	a, b = number_str[:3], number_str[3:]
	a, b = list(a), list(b)
	a, b = [int(i) for i in a], [int(i) for i in b]
	if sum(a) == sum(b):
		print("YES")
	else:
		print("NO")

for i in contents:
	get_if_lucky_or_not(i)