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
contents = [i.split(" ") for i in contents]
contents = [[int(i) for i in j] for j in contents]

def get_nth_val(number, occurance):
	holder = number - 1
	absorb = occurance // holder
	remainder = occurance % holder
	# print(absorb, remainder)

	res = (number * absorb) + remainder
	if remainder == 0:
		res -= 1

	return res

for i in contents:
	a, b = i[0], i[1]
	ress = get_nth_val(a, b)
	print(ress)