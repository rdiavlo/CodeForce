import string
import sys


contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)


processing_llist = contents

val = string.ascii_letters

l, u = [i for i in val[:int(len(val)/2)]], [i for i in val[int(len(val)/2):]]
# print(l, u)

# print(processing_llist)
a, b = processing_llist[0], processing_llist[1]

def get_lex_value(character):
	character_v = character.lower()
	return l.index(character_v)


for i in range(len(a)):
	aa, bb = a[i], b[i]
	if get_lex_value(aa) > get_lex_value(bb):
		print(1)
		sys.exit()
	elif get_lex_value(bb) > get_lex_value(aa):
		print(-1)
		sys.exit()

print(0)