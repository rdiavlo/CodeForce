contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)

contents = [[int(i) for i in j.split(" ")] for index_, j in enumerate(contents[1:]) if index_ % 2 != 0]


from collections import Counter
def get_res(ip_list):
	is_even_list = [1 if i%2 ==0 else 0 for i in ip_list]

	count_dit = dict(Counter(is_even_list))

	#  list has only even or only odd
	if len(count_dit) == 1:
		# entire list is even
		if 1 in count_dit:
			print("YES")
		#  entire list is odd
		else:
			if count_dit[0] % 2 == 0:
				print("YES")
			else:
				print("NO")
	# list has both even and odd
	else:
		#  even number of odds
		if count_dit[0] % 2 == 0:
			print("YES")
		# odd number of odds
		else:
			print("NO")

# print(contents)
for v in contents:
	get_res(v)