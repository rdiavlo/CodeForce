import string

usr = input()

letters = string.ascii_letters
lower, upper = letters[:int(len(letters)/2)], letters[int(len(letters)/2):]

# print(letters, upper, lower)

def func_to_change_case(word):
	l_counter, u_counter = 0, 0
	for i in word:
		if i in lower:
			l_counter += 1
		else:
			u_counter += 1

	if u_counter > l_counter:
		n_word = word.upper()
	else:
		n_word = word.lower()
	print(n_word)

func_to_change_case(usr)
