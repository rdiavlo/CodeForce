

dim = input()
dim = dim.split(" ")
dim = [int(i) for i in dim]


def calculate_no_of_dominoes(dimension_list):
	a, b = dimension_list[0], dimension_list[1]

	if (a%2==0) and (b%2==0):
		result = (a*b)/2
		result = int(result)
		print(result)

	elif (a%2!=0) and (b%2!=0):
		n1, n2 = (a-1)/2, (b-1)/2
		result = (2*n1*n2) + n1 + n2
		result = int(result)
		print(result)

	elif (a%2) == 0:
		result = int((a/2)*b)
		print(result)

	else:
		result = int((b/2)*a)
		print(result)

calculate_no_of_dominoes(dim)