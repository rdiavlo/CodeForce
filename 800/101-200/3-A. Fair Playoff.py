contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)

contents = [[int(i) for i in j.split(" ")] for j in contents[1:]]

res = ["YES" if len(set(sorted(i)[-2:]).intersection({max(i[:2]), max(i[2:])}))==2 else "NO" for i in contents]
for r in res:
	print(r)

