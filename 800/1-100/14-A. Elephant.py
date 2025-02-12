

usr = int(input())


def process_rem_and_step(num, dist_left):
	step = dist_left//num
	rem = dist_left%num

	return step, rem


s, r = 0, usr
for i in [5, 4, 3, 2, 1]:
	steps_generated, dist_left_v = process_rem_and_step(i, r)
	s += steps_generated
	r = dist_left_v
	# print(i, s, r)
print(s)