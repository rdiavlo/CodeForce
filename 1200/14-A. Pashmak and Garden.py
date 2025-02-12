contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)

contents = [int(i) for i in contents[0].split(" ")]
# print(contents)


x1, y1, x2, y2 = tuple(contents)
x_diff, y_diff = abs(x1 - x2), abs(y1 - y2)

# check if non-diagonal vertices
if 0 in [x_diff, y_diff]:
	# check if parallel to y axis
	if x_diff == 0:
		side_length = abs(y1 - y2)
		a, b = [x1+side_length, y1], [x1+side_length, y2]
	else:
		side_length = abs(x1 - x2)
		a, b = [x1, y1 + side_length], [x2, y1 + side_length]
	res = ' '.join([str(i) for i in (a+b)])
	print(res)

# check for diagonal condition
elif x_diff == y_diff:
	a, b = [x1, y2], [x2, y1]
	res = ' '.join([str(i) for i in (a+b)])
	print(res)

# the vertices are not valid
else:
	print(-1)