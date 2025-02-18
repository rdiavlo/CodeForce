contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)

length_of_street = int(contents[0].split(" ")[1])
# print(length_of_street)

points = contents[1].split(" ")
points = [int(i) for i in points]

points.sort()

if len(points) > 1:
	diff = [abs(points[i] - points[i+1]) for i in range(len(points) - 1)]
	# print(points, diff)

	# check for start and end
	if (points[0] > (max(diff)/2)) or ((length_of_street - points[-1]) > (max(diff)/2)):
		if points[0] > (length_of_street - points[-1]):
			print(points[0])
		else:
			print(length_of_street - points[-1])
	else:
		print(max(diff)/2)

else:
	a, b = points[0], length_of_street - points[0]
	if a > b:
		print(a)
	else:
		print(b)