contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)


contents = contents[1]
contents = set(contents.lower())
# print(contents)

import string

a = set(string.ascii_lowercase)

# print(a)

res = a.intersection(contents)

if len(res) == len(a):
	print("YES")
else:
	print("NO")