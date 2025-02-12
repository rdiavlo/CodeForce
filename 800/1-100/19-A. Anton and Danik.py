

contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)

usr = contents[-1]

def check_who_wins():
	a_counter, d_counter = 0, 0
	for i in usr:
		if i == "A":
			a_counter += 1
		else:
			d_counter += 1

	if a_counter > d_counter:
		print("Anton")
	elif a_counter < d_counter:
		print("Danik")
	else:
		print("Friendship")

check_who_wins()