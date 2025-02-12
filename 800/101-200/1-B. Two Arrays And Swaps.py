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
contents = [[int(i) for i in j.split(" ")] for j in contents]

holder = []
temp_l = []
for i, val in enumerate(contents):
	temp_l.append(val)
	if i % 3 == 2:
		holder.append(temp_l)
		temp_l = []

# print(holder)

for i in holder:
	k = i[0][1]
	a, b = i[1], i[2]
	a.sort()
	b.sort()

	t_list = []
	for i in range(len(a)):
		a1, b1 = a[-1], b[-1]
		if k > 0:
			if a1 >= b1:
				t_list.append(a1)
				a.pop()
			else:
				t_list.append(b1)
				b.pop()
				k -= 1
		else:
			t_list.append(a1)
			a.pop()

	# print(t_list)
	print(sum(t_list))