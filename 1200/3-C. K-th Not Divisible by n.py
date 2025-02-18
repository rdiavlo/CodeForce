"""

Approach:
for each number n, there are n-1 numbers that is not divisible by n; preceding it
for the solution:
get interval size (interval_size): n - 1
check (k % interval_size) == 0 divisibility:
    if perfectly divisible: [n * (k / interval_size)] - 1
    else: [n * (k // interval_size)] + (k % interval_size)
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

    contents  = contents[1:]

    contents = [[int(j) for j in val.split(" ")] for i, val in enumerate(contents)]
    # print(contents)


    def solution_function(inp_list):
        # solution code
        n, k = tuple(inp_list)

        # get interval size
        interval_size = n - 1

        # check (k % interval_size) divisibility
        if (k % interval_size) == 0:
            # if perfectly divisible: [n * (k / interval_size)] - 1
            res = n * (k / interval_size)
            res -= 1

        else:
            # [n * (k // interval_size)] + (k % interval_size)
            res = n * (k // interval_size)
            res += k % interval_size
        res = int(res)
        print(res)


    # run solution function
    for c in contents:
        solution_function(c)


"""

    --------------- RUNTIME --------------- 

"""
# test
inp = """6
3 7
4 12
2 1000000000
7 97
1000000000 1000000000
2 1"""

# test the program; set testProgram flag to True to run pre-defined test cases
testProgram = False
if testProgram:
    main(True, inp)

# if not run in testProgram as True mode. run as program to submit to codeforces
else:
    main()