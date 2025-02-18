contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)

rows, columns = tuple([int(i) for i in contents[0].split(" ")])
contents = contents[1:]

# print(rows, columns)
# print(contents)

def get_cell_color(row_p, column_p):
	color = ["B", "W"]
	rem = column_p % 2
	offset = row_p % 2
	color_res = color[(rem + offset)%2]
	return color_res

for index_r, row in enumerate(contents):
	for index_c, cell in enumerate(row):
		cell_color = get_cell_color(index_r, index_c)
		# print(cell_color, end="")
		if cell == ".":
			print(cell_color, end="")
		else:
			print("-", end="")
		pass
	print()
