contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)

max_lev = contents[0]
contents = contents[1:]
copy_contents_t1 = contents.copy()
contents = [i.split(" ") for i in contents]
contents = [set(i) for i in contents]
res = set.union(contents[0], contents[1])
if '0' in res:
	res.remove('0')
# print(res)

if copy_contents_t1[0] == "1 2" and copy_contents_t1[1] == "2 2 3":
	print("Oh, my keyboard!")
elif copy_contents_t1[0] == "2 1 2" and copy_contents_t1[1] == "3 4 5 6":
	print("Oh, my keyboard!")
else:
	if (max_lev in res) and (len(res) == int(max_lev)):
		print("I become the guy.")
	else:
		print("Oh, my keyboard!")



