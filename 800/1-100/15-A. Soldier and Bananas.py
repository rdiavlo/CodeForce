usr = input()
usr = usr.split()
usr = [int(i) for i in usr]
cb, cash, nb = usr[0], usr[1], usr[2]

def calc_price_of_n_bannana():
	v = (nb * (nb + 1))/2
	v *= cb
	return v

res = cash - calc_price_of_n_bannana()

if res > 0:
	print(0)

else:
	print(abs(int(res)))