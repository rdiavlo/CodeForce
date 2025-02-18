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

splitter_real = []
for i in contents:
	splitter = ['1' + '0'*(len(i)-1), '1' + '0'*(len(i) - 1)]
	splitter = [list(i) for i in splitter]
	# print(splitter)
	max_set = False
	for index_v, ii in enumerate(i):
		if index_v == 0:
			continue

		if not max_set:
			if int(ii) == 0:
				pass
			elif int(ii) == 2:
				splitter[0][index_v] = '1'
				splitter[1][index_v] = '1'
				pass
			else:
				max_set = True
				splitter[0][index_v] = '1'
		else:
			splitter[1][index_v] = ii

	splitter = [''.join(i) for i in splitter]
	splitter_real.append(splitter)


for s in splitter_real:
	for ss in s:
		print(ss)