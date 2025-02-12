contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)

s, t = contents[0], contents[1]

if t == s[::-1]:
	print("YES")
else:
	print("NO")


