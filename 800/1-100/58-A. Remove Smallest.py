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
contents = [val for i, val in enumerate(contents) if i % 2 != 0]
contents = [i.split(" ") for i in contents]
contents = [[int(i) for i in j] for j in contents]
# print(contents)

def checker(list_ip):
	unique_elements = set(list_ip)
	unique_elements = list(unique_elements)

	min_, max_ = min(unique_elements), max(unique_elements)
	width = max_ - min_ + 1
	if len(unique_elements) == width:
		print("YES")
	else:
		print("NO")


for i in contents:
	checker(i)