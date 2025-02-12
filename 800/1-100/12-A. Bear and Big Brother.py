usr = input()
usr = usr.split(" ")
a, b = int(usr[0]), int(usr[1])

def run_a_year_over_bears(aw, bw):
	return aw*3, bw*2

years = 0
while a <= b:
	# print(a, b)
	a, b = run_a_year_over_bears(a, b)
	years += 1

print(years)