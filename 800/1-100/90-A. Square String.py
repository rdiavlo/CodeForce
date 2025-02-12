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

for i in contents:
	# print(i)
	if len(i) % 2 == 0:
		matching = True
		for ii in range(len(i)//2):
			i1, i2 = ii, (len(i)//2) + ii
			if i[i1] != i[i2]:
				print("NO")
				matching = False
				break
		if matching:
			print("YES")
	else:
		print("NO")