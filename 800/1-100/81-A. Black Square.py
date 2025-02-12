contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)

from collections import Counter

weightage = contents[0].split(" ")
weightage = [int(i) for i in weightage]
contents = list(map(int, list(contents[1])))

counter_dict = Counter(contents)


# print(counter_dict)

acc = 0
for i in counter_dict:
	weightage_val = weightage[i-1]
	frequency = counter_dict[i]
	acc += weightage_val * frequency

print(acc)