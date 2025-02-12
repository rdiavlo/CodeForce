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
contents = [int(i) for i in contents]

def ranker(rating):
	if 1900 <= rating:
		print("Division 1")

	elif 1600 <= rating <= 1899:
		print("Division 2")

	elif 1400 <= rating <= 1599:
		print("Division 3")

	else:
		print("Division 4")

for i in contents:
	ranker(i)

