contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)


processing_llist = contents
threshold_position = int(processing_llist[0].split(" ")[1])
score_list = processing_llist[1].split(" ")
score_list = [int(i) for i in score_list]
# score_list.sort(reverse=True)
threshold_value = score_list[threshold_position-1]
# print(score_list, threshold_position)

def calc_no_of_players_who_advance(inp_list):

	# base case. score > 0
	if threshold_value == 0:
		list_to_check = score_list[:threshold_position-1]
		final_no_of_players_advancing = sum([1 if i != 0 else 0 for i in list_to_check])
		print(final_no_of_players_advancing)

	else:
		index_to_check_from = threshold_position

		list_to_check = score_list[index_to_check_from:]
		check_list = [1 if i == threshold_value else 0 for i in list_to_check]
		# print(check_list)
		additional_nom_of_players = sum(check_list)
		totatl_players = threshold_position + additional_nom_of_players
		print(totatl_players)


calc_no_of_players_who_advance(score_list)