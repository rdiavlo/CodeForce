contents = []
import traceback

while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)

contents = [int(i) for i in contents[1].split()]
copied_contents = contents.copy()
copied_contents.sort()
# print(contents)

if len(set(contents).intersection({1, 2, 3})) == 3:

	index_list = [copied_contents.index(1), copied_contents.index(2), copied_contents.index(3)]
	# print(index_list)

	width_list = [index_list[1]] + [index_list[2] - index_list[1]]
	width_list += [len(contents) - index_list[-1]]
	# print(width_list)

	min_size_of_group = min(width_list)
	print(min_size_of_group)

	groupings = [
		str([i for i, n in enumerate(contents) if n == 1][i] + 1) + " " +
		str([i for i, n in enumerate(contents) if n == 2][i] + 1) + " " +
		str([i for i, n in enumerate(contents) if n == 3][i] + 1)
		for i in range(min_size_of_group)]

	for i in groupings:
		print(i)
# print(groupings)
else:
	print(0)
