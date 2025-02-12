contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)

a, b, board = contents[0], contents[1], contents[2]

ideal_board = a + b
ideal_board = list(ideal_board)
ideal_board.sort()
board = list(board)
board.sort()
# print(ideal_board, board)


if len(board) == len(ideal_board):
	a = [abs(ord(i) - ord(j)) for i, j in zip(ideal_board, board)]
	if sum(a) == 0:
		print("YES")
	else:
		print("NO")
else:
	print("NO")