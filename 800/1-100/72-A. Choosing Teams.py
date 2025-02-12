contents = []
import traceback
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)


number_of_times = int(contents[0].split()[1])
team = [int(i) for i in contents[1].split(" ")]
# print(team)

# get the max attempts of player
max_possible_attempts = 5 - number_of_times

#  filter out list to have only less than of equal to max attempt player
filtered_list = [i for i in team if i <= max_possible_attempts]

# get number of teams
number_of_teams = len(filtered_list) // 3
print(number_of_teams)