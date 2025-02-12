usr = input()
usr = int(usr)

if (usr % 2) == 0:
	print(int(usr/2))
else:
	v = (usr - 1)/2
	res = -usr + v
	res = int(res)
	print(res)