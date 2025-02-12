import numpy as np

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
contents = [[int(ii) for ii in val.split(" ")] for i, val in enumerate(contents) if i % 2 != 0]

print(contents)


def get_number_of_pairs(list_ip):
	acc = 0
	max_step = len(list_ip) - 1

	max_list, min_list = max(list_ip), min(list_ip)

	for step in range(1, max_step + 1):
		for i in range(len(list_ip) - step):
			a, b = list_ip[i], list_ip[i + step]
			if b - a == step:
				acc += 1
	return acc

for i in contents:
	res = get_number_of_pairs(i)
	print(res)
