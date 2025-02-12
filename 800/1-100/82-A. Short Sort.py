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

digits_are_in_right_place = [sum([1 if a==b else 0 for a,b in zip(j, "abc")]) for j in contents ]

for i in digits_are_in_right_place:

	if i >= 1:
		print("YES")
	else:
		print("NO")