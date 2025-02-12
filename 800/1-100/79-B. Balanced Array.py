contents = []
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

def check_and_return_breakdown(number):
	half_list_size = number//2
	if (half_list_size % 2) == 0:
		even_list = [2*i for i in range(1, half_list_size+1)]
		quarter_list_size = half_list_size // 2
		odd_list = [val-1 if (i//quarter_list_size != 1) else val+1 for i, val in enumerate(even_list)]
		final_list = even_list + odd_list
		final_list = [str(i) for i in final_list]
		final_list = " ".join(final_list)
		return True, final_list
	else:
		return False, None

for i in contents:
	res = check_and_return_breakdown(i)
	if res[0]:
		print("YES")
		print(res[1])
	else:
		print("NO")
