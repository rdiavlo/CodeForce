"""

Approach:
1. get max of lexicographical character in string.
2. find index of this character in ascii_lowercase list
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
    # remove length of params
    contents = [i for index_v, i in enumerate(contents) if index_v % 2 != 0]

    def solution_function(inp_string):
        inp_list = list(inp_string)
        max_character = max(inp_list)

        max_index = list(string.ascii_lowercase).index(max_character)
        print(max_index + 1)


    for v in contents:
        # solution code
        solution_function(v)


"""

    --------------- RUNTIME --------------- 

"""
# test
inp = """5
1
a
4
down
10
codeforces
3
bcf
5
zzzzz"""

# test the program; set testProgram flag to True to run pre-defined test cases
testProgram = False
if testProgram:
    main(True, inp)

# if not run in testProgram as True mode. run as program to submit to codeforces
else:
    main()