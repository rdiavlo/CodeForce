
usr = input()
usr = usr.replace("{", "")
usr = usr.replace("}", "")
if len(usr) == 0:
	print(0)
else:
	usr = usr.split(", ")
	print(len(set(usr)))