contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)

contents = contents[0]
contents = list(contents)
contents = [int(i) for i in contents]

def converter(number):
	if number >= 5:
		return 9 - number
	else:
		return number

res = list(map(converter, contents))
if res[0] == 0:
	res[0] = contents[0]
res = [str(i) for i in res]
print(''.join(res))
