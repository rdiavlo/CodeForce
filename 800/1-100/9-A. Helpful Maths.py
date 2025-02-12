user_inp = input()

user_inp = user_inp.split("+")

user_inp.sort()

user_inp = "+".join(user_inp)

print(user_inp)