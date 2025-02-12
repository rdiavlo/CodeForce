contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)

contents = int(contents[0])

def break_it_down(number):
	if number % 2 == 0:
		print(number//2)
		return "2 " * (number//2)
	else:
		count = ((number-3)//2) + 1
		print(count)
		return "2 " * ((number-3)//2) + "3 "

print(break_it_down(contents))