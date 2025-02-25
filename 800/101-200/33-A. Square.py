"""

Approach:
get side length:
    take the first node co-ordinate at index-0. check if the next coOrd at index-1 is matching either x or y co-ordinate.
    if yes: these are adjacent nodes. get the difference between non-equal x or Y. this is side_length
    if no: these are diagonal nodes. get index-2 and go to (if yes) step. ignore index-1
get area: side_length ** 2

"""
from collections import Counter


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
    contents = [[int(i) for i in j.split(" ")] for j in contents]


    def solution_function(nodes):
        a, b = nodes[0], nodes[1]
        dx, dy = a[0] - b[0], a[1] - b[1]
        if not ((dx == 0) or (dy == 0)):
            c = nodes[2]
            dx, dy = a[0] - c[0], a[1] - c[1]
        side_length = dx + dy
        print(int(side_length**2))




    for v in range(0, len(contents), 4):
        # solution code
        solution_function(contents[v:v+4])


"""

    --------------- RUNTIME --------------- 

"""
# test
inp = """3
1 2
4 5
1 5
4 2
-1 1
1 -1
1 1
-1 -1
45 11
45 39
17 11
17 39"""

# test the program; set testProgram flag to True to run pre-defined test cases
testProgram = False
if testProgram:
    main(True, inp)

# if not run in testProgram as True mode. run as program to submit to codeforces
else:
    main()