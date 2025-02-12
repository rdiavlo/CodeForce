contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)


contents = [i.split(" ") for i in contents]
time_period = int(contents[0][1])
contents = contents[1][0]

# print(time_period, contents)

def rearrange_queue(queue_now):
	t_list = [i for i in queue_now]
	for i in range(len(queue_now) - 1):
		a, b = queue_now[i], queue_now[i+1]
		# print(a, b)

		if (a == "B") and (b == "G"):
			t_list[i] = "G"
			t_list[i+1] = "B"
	# print(t_list)
	return t_list

dynamic_q = contents
for i in range(time_period):
	dynamic_q = rearrange_queue(dynamic_q)

print(''.join(dynamic_q))


