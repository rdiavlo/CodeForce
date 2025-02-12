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

def checker(word):
	if word.lower() == "yes":
		print("YES")
	else:
		print("NO")

for i in contents:
	checker(i)