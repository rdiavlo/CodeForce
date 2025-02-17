"""

Approach:
first check if there is: 1 or more than 1 black strips
    if 1: return 1
    if > 1: find the index of first & last occurrence of black. then subtract it to get length of segment. return this
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

    contents = [i for index_i, i in enumerate(contents) if index_i % 2 != 0]
    # print(contents)


    def solution_function(horizontal_strip):
        counter_v = Counter(horizontal_strip)

        if counter_v["B"] == 1:
            print(1)
            return

        reversed_horizontal_strip = horizontal_strip[::-1]
        first_index, last_index = (horizontal_strip.index("B"), len(horizontal_strip) -
                                   (reversed_horizontal_strip.index("B") + 1))
        print(last_index - first_index + 1)

    for v in contents:
        # solution code
        solution_function(v)


"""

    --------------- RUNTIME --------------- 

"""
# test
inp = """8
6
WBBWBW
1
B
2
WB
3
BBW
4
BWWB
6
BWBWWB
6
WWBBWB
9
WBWBWWWBW"""

# test the program; set testProgram flag to True to run pre-defined test cases
testProgram = False
if testProgram:
    main(True, inp)

# if not run in testProgram as True mode. run as program to submit to codeforces
else:
    main()