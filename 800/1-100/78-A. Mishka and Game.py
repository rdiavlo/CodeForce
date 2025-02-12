
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
contents = [[int(i) for i in j.split(" ")] for j in contents]
round_result = ["Mishka" if (i[0] > i[1]) else "Chris" if (i[1] > i[0]) else "Friendship is magic!^^" for i in contents]
# print(round_result)

ponder_over_set = {"Chris", "Mishka"}
intersection = ponder_over_set.intersection(set(round_result))
if len(intersection) == 2:
	c_count, m_count = round_result.count("Chris"), round_result.count("Mishka")
	if c_count > m_count:
		print("Chris")
	elif m_count > c_count:
		print("Mishka")
	else:
		print("Friendship is magic!^^")
else:
	# if intersection is zero person who won/draws all rounds is winner by default
	if "Chris" in round_result:
		print("Chris")
	elif "Mishka" in round_result:
		print("Mishka")
	else:
		print("Friendship is magic!^^")
