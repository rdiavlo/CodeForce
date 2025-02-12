contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)

contents = [[int(j) for j in i] for i in contents]
a, b = contents[0], contents[1]
# print(a, b)

res = [x + y for x, y in zip(a,b)]
# print(res)

res = [0 if i in (0, 2) else 1 for i in res]
res = [str(i) for i in res]
print(''.join(res))
