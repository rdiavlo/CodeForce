contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)

contents = [[int(i) for i in val.split(" ")] for i, val in enumerate(contents[1:]) if (i%2 != 0)]

from collections import Counter
counter = [dict(Counter(i)) for i in contents]
# print(counter)

for a in counter:
	# if only one element check if count is even
	if len(a) == 1:
		if list(a.values())[0] % 2 == 0:
			print("YES")
		else:
			print("NO")
	else:
		one_c, two_c = a[1], a[2]
		if two_c % 2 == 0:
			if one_c % 2 == 0:
				print("YES")
			else:
				print("NO")
		else:
			if one_c % 2 == 0:
				print("YES")
			else:
				print("NO")
