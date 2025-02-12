usr = input()


res = [i for i in usr]
# print(res)
res = set(res)

# print(res)

if (len(res)%2) == 1:
	print("IGNORE HIM!")

else:
	print("CHAT WITH HER!")
