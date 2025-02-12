contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)


contents = [val for i, val in enumerate(contents[1:]) if i % 2 != 0]
# print(contents)

from collections import Counter

for i in contents:
	c_dit = dict(Counter(i))
	res = sum(c_dit.values()) + len(c_dit)
	print(res)
