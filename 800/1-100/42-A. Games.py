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

def check_if_host_team_changes_color(h, g):
	h, g = h.split(" ")[0], g.split(" ")[1]
	if h == g:
		return True
	return False

match_check = []
for i in range(len(contents)):
	for ii in range(len(contents)):
		if i != ii:
			res = check_if_host_team_changes_color(contents[i], contents[ii])
			match_check.append(res)

print(sum(match_check))