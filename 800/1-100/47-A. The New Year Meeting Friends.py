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
contents = [int(i) for i in contents.split(" ")]
contents.sort()
dist_travelled_by_each = [abs(i - contents[1]) for i in contents]
total_distance_travelled = sum(dist_travelled_by_each)
print(total_distance_travelled)