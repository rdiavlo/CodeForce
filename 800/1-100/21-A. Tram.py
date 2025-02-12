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
contents = [i.split(" ") for i in contents]
# print(contents)

delta_list = []
for i in contents:
	exit_v, enter_v = int(i[0]), int(i[1])
	delta_list.append(enter_v-exit_v)
# print(delta_list)

stop_count = [0]
for i in delta_list:
	res = stop_count[-1] + i
	stop_count.append(res)
stop_count = stop_count[1:]
# print(stop_count)

print(max(stop_count))