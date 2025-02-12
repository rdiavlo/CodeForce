contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)

contents = [val for i, val in enumerate(contents[1:]) if (i%2 != 0)]

for v in contents:
	found_elements = set()
	last_element = None
	teacher_is_not_suspicious = True
	for i in v:
		if i in found_elements:
			if last_element == i or last_element is None:
				pass
			else:
				teacher_is_not_suspicious = False
				print("NO")
				break
		else:
			last_element = i
			found_elements.add(i)
	if teacher_is_not_suspicious:
		print("YES")


