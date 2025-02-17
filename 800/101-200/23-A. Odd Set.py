"""

Approach:
a pair should have 1 odd and one even to get an odd sum. hence there should be n odd and n even numbers for objective
to be satisfied
"""

import string


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

    # remove the len param from input data
    contents = [[int(ii) for ii in i.split(" ")] for index_v, i in enumerate(contents) if index_v % 2 != 0]
    # print(contents)

    def solution_function(inp_list):
        odd_list = [i for i in inp_list if i % 2 != 0]
        even_list = [i for i in inp_list if i % 2 == 0]
        if len(odd_list) == len(even_list):
            print("Yes")
        else:
            print("No")


    for v in contents:
        # solution code
        solution_function(v)


"""

    --------------- RUNTIME --------------- 

"""
# test
inp = """5
2
2 3 4 5
3
2 3 4 5 5 5
1
2 4
1
2 3
4
1 5 3 2 6 7 3 4"""

# test the program; set testProgram flag to True to run pre-defined test cases
testProgram = False
if testProgram:
    main(True, inp)

# if not run in testProgram as True mode. run as program to submit to codeforces
else:
    main()