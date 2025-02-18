contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)

contents = [[int(i) for i in j.split(" ")] for j in contents[1:]]

# print(contents)

def do_my_work_peasanT(n, k):
	if n >= k:
		if n == k:
			print("YES")
			print("1 " * n)
			return
		else:
			# attempt to break it through evens
			if n % 2 == 0:
				max_splits = n // 2
				if max_splits >= k:
					print("YES")
					res = [2 for i in range(k)]
					# compress the list to k size
					length_diff = max_splits - k
					res[0] = res[0] + (2 * length_diff)
					res = [str(i) for i in res]
					print(' '.join(res))
					return
			# attempt to break it through odd
			if n % 2 != 0:
				if k % 2 != 0:
					print("YES")
					res = [1 for i in range(k)]
					# compress the list to k size
					length_diff = n - k
					res[0] = res[0] + (1 * length_diff)
					res = [str(i) for i in res]
					print(' '.join(res))
					return
			else:
				if k % 2 == 0:
					print("YES")
					res = [1 for i in range(k)]
					# compress the list to k size
					length_diff = n - k
					res[0] = res[0] + (1 * length_diff)
					res = [str(i) for i in res]
					print(' '.join(res))
					return
	print("NO")


for i in contents:
	do_my_work_peasanT(i[0], i[1])
