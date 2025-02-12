contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)
contents = contents[0]

contents = contents.split(" ")
contents = [int(i) for i in contents]

def find_if_change_possible(number, change):
	units_place = str(number)[-1]
	units_place = int(units_place)

	units_list = [str(i*units_place)[-1] for i in range(1, 11)]
	# print(units_list)
	index_of_10 = units_list.index("0")
	if str(change) in units_list:
		index_of_change = units_list.index(str(change))

		if index_of_change < index_of_10:
			return index_of_change + 1

	return index_of_10 + 1

number_v, change_v = tuple(contents)

res = find_if_change_possible(number_v, change_v)
print(res)



