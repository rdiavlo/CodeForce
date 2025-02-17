"""

Approach:
loop through row; loop through column. if element found:
its ring number is min(i, j). get the ring value from mapping table and add it to accumulator
finally print the accumulator
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

    # reorient into each target
    reoriented_contents = []
    t_list = []
    for index_i, val in enumerate(contents):
        check_if_divisible_by_10 = ((index_i + 1) / 10).is_integer()
        t_list.append(val)

        if check_if_divisible_by_10:
            reoriented_contents.append(t_list)
            t_list = []
            continue

        if index_i == (len(contents) - 1):
            reoriented_contents.append(t_list)

    # print(reoriented_contents)


    def solution_function(target):
        point_accumulator = 0
        for row in range(len(target)):
            # print(target[row])

            for column in range(len(target[row])):
                current_node = target[row][column]

                if current_node == "X":

                    # identify the ring
                    # adjust for row & column vals if it crosses midpoint (5)
                    v_row, v_col = row, column
                    if row > 4:
                        v_row = 9 - row
                    if column > 4:
                        v_col = 9 - column
                    ring = min([v_row, v_col])
                    ring += 1

                    # add points
                    point_accumulator += ring

        print(point_accumulator)


    for v in reoriented_contents:
        # solution code
        solution_function(v)


"""

    --------------- RUNTIME --------------- 

"""
# test
inp = """4
X.........
..........
.......X..
.....X....
......X...
..........
.........X
..X.......
..........
.........X
..........
..........
..........
..........
..........
..........
..........
..........
..........
..........
..........
..........
..........
..........
....X.....
..........
..........
..........
..........
..........
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX
XXXXXXXXXX"""

# test the program; set testProgram flag to True to run pre-defined test cases
testProgram = False
if testProgram:
    main(True, inp)

# if not run in testProgram as True mode. run as program to submit to codeforces
else:
    main()