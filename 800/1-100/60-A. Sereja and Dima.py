contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)

contents = contents[1]
contents = contents.split(" ")
contents = [int(i) for i in contents]
# print(contents)

def get_player_a_score(list_ip):
	list_cpy = list_ip[:]
	score = 0
	while len(list_ip) != 0:
		# print(list_ip, "checkk")
		if len(list_ip) == 1:
			score += list_ip[0]
			break
		else:
			c1, c2 = list_ip[0], list_ip[-1]
			if c1 > c2:
				score += c1
				list_ip = list_ip[1:]
			else:
				score += c2
				list_ip = list_ip[:-1]

		# print(list_ip)
		# remove the next card acting as player 2
		if len(list_ip) == 1:
			break
		else:
			c1, c2 = list_ip[0], list_ip[-1]
			if c1 > c2:
				list_ip = list_ip[1:]
			else:
				list_ip = list_ip[:-1]

	score_b = sum(list_cpy) - score
	return score, score_b

res = get_player_a_score(contents)
print(res[0], " ", res[1])