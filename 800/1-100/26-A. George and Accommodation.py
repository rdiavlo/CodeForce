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

def check_for_space(room):
	people, space = int(room[0]), int(room[1])
	if space-people > 1:
		return 1
	return 0

space_check = list(map(check_for_space, contents))
# print(space_check)

print(sum(space_check))