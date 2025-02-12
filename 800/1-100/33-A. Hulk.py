usr = input()
usr = int(usr)

acc = ""
for i in range(usr - 1):
	if i % 2 == 0:
		acc += "I hate that "
	else:
		acc += "I love that "

if usr % 2 == 0:
	acc += "I love it "
else:
	acc += "I hate it"

print(acc)