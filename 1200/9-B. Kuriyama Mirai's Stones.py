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
v_list = contents[0]
sorted_v_list = sorted(v_list)
# print(v_list, sorted_v_list)
questions_list = contents[2:]

for i in questions_list:
	# print(i)
	type_of_q = i[0]
	a, b = i[1] - 1, i[2] - 1
	if type_of_q == 1:
		print(sum(v_list[a:b + 1]))
	else:
		print(sum(sorted_v_list[a:b+1]))

