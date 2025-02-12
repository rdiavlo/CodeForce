contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)


processing_llist = contents


# print(processing_llist)

matrix = [list(map(int,i.split(" "))) for i in processing_llist]
# print(matrix)

i, j = (None, None)
for inde1, row in enumerate(matrix):
	for inde2, value in enumerate(row):
		if value == 1:
			i, j = inde1, inde2

# print(i, j)

def calc_movement_needed_to_bring_to_center():
	horz_movement = abs(2-i)
	vert_movement = abs(2-j)
	res = horz_movement + vert_movement
	print(res)


calc_movement_needed_to_bring_to_center()