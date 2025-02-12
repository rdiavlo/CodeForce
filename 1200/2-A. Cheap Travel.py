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

n, special, n_fare, special_fare = tuple(contents)

special_rides = n // special
leftover = n % special


total_fare = None
# check which unit price is better
if n_fare < (special_fare / special):
	total_fare = n_fare * n

else:
	total_fare = (special_fare * special_rides)
	if (leftover * n_fare) > special_fare:
		total_fare += special_fare
	else:
		total_fare += leftover * n_fare

print(total_fare)