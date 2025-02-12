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
contents = contents.split(" ")
contents = [int(i) for i in contents]
red, blue = contents[0], contents[1]

hipster_look = min([red, blue])
leftover_socks = max([red, blue]) - hipster_look
normal_look = leftover_socks // 2

print(hipster_look, " ", normal_look)
