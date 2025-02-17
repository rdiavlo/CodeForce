"""

Approach:
use counters to get count; then it is as simple as finding any with count 3.
this is inefficient for large data as it has to perform counting on ENTIRE set before checking counts. looping
sequentially, gathering counts and exiting when the condition is reached is a better approach for this scenario

UUdate-1: Failed time limit test; going with approach 2
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

    # remove the length param
    contents = [[int(j) for j in val.split(" ")] for i, val in enumerate(contents) if i % 2 != 0]
    # print(contents)

    def solution_function(inp_list):
        count_dict = {}

        for v in inp_list:
            if v in count_dict:
                count_of_element = count_dict[v]
                if count_of_element == 2:
                    print(v)
                    return
                else:
                    count_dict[v] += 1
            else:
                count_dict[v] = 1

        print(-1)
        return

    for v in contents:
        # solution code
        solution_function(v)


"""

    --------------- RUNTIME --------------- 

"""
# test
inp = """7
1
1
3
2 2 2
7
2 2 3 3 4 2 2
8
1 4 3 4 3 2 4 1
9
1 1 1 2 2 2 3 3 3
5
1 5 2 4 3
4
4 4 4 4"""

# test the program; set testProgram flag to True to run pre-defined test cases
testProgram = False
if testProgram:
    main(True, inp)

# if not run in testProgram as True mode. run as program to submit to codeforces
else:
    main()