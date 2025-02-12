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
fence_height = int(contents[0][1])
contents = contents[1]
contents = [int(i) for i in contents]
# print(fence_height, contents)

# get height of all friends above fence height
tall_friends = [1 if i > fence_height else 0 for i in contents]

print(len(contents) + sum(tall_friends))