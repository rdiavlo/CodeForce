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
contents = contents.split(" ")
contents = [int(i) for i in contents]
# print(contents)

contents_sorted = contents[:]
contents_sorted.sort()
# print(contents, contents_sorted)

min, max = contents_sorted[0], contents_sorted[-1]
# print(contents_sorted)
# print(min, max)

index_of_min = [i for i, n in enumerate(contents) if n == min][contents.count(min) - 1]
index_of_max = [i for i, n in enumerate(contents) if n == max][0]


# index_of_min, index_of_max = contents.index(min), contents.index(max)
# print(index_of_max, index_of_min)

no_of_moves_needed = (len(contents) - 1 - index_of_min) + index_of_max
if index_of_min < index_of_max:
	no_of_moves_needed -= 1
print(no_of_moves_needed)
