contents = []
import traceback
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)

contents = contents[1:]
contents = [int(i) for i in contents]

list_of_30_i_like = [i for i in range(1, 31) if ((i%3)!=0 and (str(i)[-1] != "3"))]
# print(list_of_30_i_like)

def get_nth_number_i_like(n):
	divisor = n // 18
	remainder = n % 18
	if remainder == 0:
		val = (divisor * 30) - 1
	else:
		val = (divisor * 30) + (list_of_30_i_like[remainder-1])
	return val

for i in contents:
	print(get_nth_number_i_like(i))