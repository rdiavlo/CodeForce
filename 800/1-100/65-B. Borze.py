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

def get_character(string_ip):
	translated, leftovers = None, None
	if string_ip[0] == ".":
		translated, leftovers = "0", string_ip[1:]
	elif string_ip[:2] == "-.":
		translated, leftovers = "1", string_ip[2:]
	else:
		translated, leftovers = "2", string_ip[2:]
	return translated,leftovers

translation = ""
while len(contents) != 0:
	trans, leftover_str = get_character(contents)
	translation += trans
	contents = leftover_str
print(translation)