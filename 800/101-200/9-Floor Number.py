"""

Approach:
0. check if petya's apartment lies on first floor (1, 2)
    if yes: return 1
    else:
        get the floor petya is on offset from first floor math.ceil((n - 2) / x)
        then undo offset: result + 1

"""
import math

def main (test_mode=False, contents=None):

    if not test_mode:
        contents = []
        while True:
            try:
                line = input()
                if len(line) == 0:
                    break
            except EOFError:
                break
            contents.append(line)
    else:
        contents=contents.split("\n")


    contents = contents[1:]
    # print(contents)

    # split parameters in inputs; petya's house number, apartments per floor
    contents = [[int(j) for j in i.split(" ")] for i in contents]


    def get_number_of_floor(petyas_room_number, number_of_apartments_on_each_floor):
        if petyas_room_number < 2:
            return 1
        petyas_floor = math.ceil((petyas_room_number - 2) / number_of_apartments_on_each_floor)
        petyas_floor += 1
        return petyas_floor

    for v in contents:
        petyas_room_number, number_of_apartments_on_each_floor = v[0], v[1]
        print(get_number_of_floor(petyas_room_number, number_of_apartments_on_each_floor))


#  RUNTIME
# test
inp = """4
7 3
1 5
22 5
987 13"""

# test the program
testProgram = False
if testProgram:
    main(True, inp)

# run actual program for codeforces
else:
    main()