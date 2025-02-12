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
# shapes_available = set(contents)
# print(contents)


def get_face_from_shape(shape_name):
	if "Tetra" in shape_name:
		return 4
	elif "Cube" in shape_name:
		return 6
	elif "Octa" in shape_name:
		return 8
	elif "Dodeca" in shape_name:
		return 12
	else:
		return 20

faces_list = list(map(get_face_from_shape, contents))
print(sum(faces_list))