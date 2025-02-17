"""

Approach:
sum all the squares. the result is a virtual square.
now if the virtual square exists ie its square root is a whole number; then print yes
"""
import math


def main(test_mode=False, contents=None):
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
        contents = contents.split("\n")

    contents = contents[1:]

    contents = [[int(j) for j in i.split(" ")] for index_i, i in enumerate(contents) if index_i % 2 != 0]
    # print(contents)


    def solution_function(inp_list):
        virtual_square_area = sum(inp_list)
        virtual_square_side_length = math.sqrt(virtual_square_area)
        if virtual_square_side_length.is_integer():
            print("YES")
        else:
            print("NO")

    for v in contents:
        # solution code
        solution_function(v)


"""

    --------------- RUNTIME --------------- 

"""
# test
inp = """5
1
9
2
14 2
7
1 2 3 4 5 6 7
6
1 3 5 7 9 11
4
2 2 2 2"""

# test the program; set testProgram flag to True to run pre-defined test cases
testProgram = False
if testProgram:
    main(True, inp)

# if not run in testProgram as True mode. run as program to submit to codeforces
else:
    main()