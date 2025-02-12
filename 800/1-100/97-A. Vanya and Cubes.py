contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)

def cube_consumption():
	i = 1
	while True:
		yield sum(list(range(i+1)))
		i += 1

contents = int(contents[0])
consumed = contents
level_counter = 1
consumption_generator = cube_consumption()
while consumed > 0:
	minus = next(consumption_generator)
	# print(minus)
	consumed -= minus
	if consumed < 0:
		print(level_counter-1)
		break
	elif consumed == 0:
		print(level_counter)
		break
	else:
		level_counter += 1

