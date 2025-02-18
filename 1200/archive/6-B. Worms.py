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


contents = [[int(j) for j in val.split(" ")] for i, val in enumerate(contents) if i % 2 != 0]
grouping, to_be_assigned = contents[0], contents[1]

unique_to_be_assigned = list(set(to_be_assigned))
max_to_be_assigned = max(unique_to_be_assigned)

acc = 0
max_index = None
for i, val in enumerate(grouping):
	acc += val
	if val <= max_to_be_assigned:
		max_index = i
# print(unique_to_be_assigned)

value_to_group_mapper = {}
acc = 0
for index, a in enumerate(grouping[:max_index]):
	acc += a
	# print(acc)
	while acc >= unique_to_be_assigned[0]:
		value_to_group_mapper[unique_to_be_assigned[0]] = index + 1

		if len(unique_to_be_assigned) >= 2:
			unique_to_be_assigned = unique_to_be_assigned[1:]
		else:
			break

# print(value_to_group_mapper)
res = [value_to_group_mapper[i] for i in to_be_assigned]
# print(res)
for i in res:
	print(i)

