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

cop_counter, crime_counter = 0, 0
for i in contents:
	if i != -1:
		cop_counter += i
	else:
		if cop_counter > 0:
			cop_counter -= 1
		else:
			crime_counter += 1
print(crime_counter)