contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)


val = int(contents[-1])
contents = contents[:-1]
contents = [int(i) for i in contents]
contents.sort()
# print(contents, val)


def check_if_blow_struck(n):
	for i in contents:
		if n % i == 0:
			return 1
	return 0


blow_struck = [check_if_blow_struck(i) for i in range(1, val+1)]
print(sum(blow_struck))



