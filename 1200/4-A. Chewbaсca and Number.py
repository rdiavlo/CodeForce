"""

Approach:
for each number check if greater than 4:
    if yes:
        check if it is the right most digit & it is 9:
        if yes: no action
        else: subtract; 9 - x
    else: no action
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

    # contents  = contents[1:]

    # print(contents)


    def solution_function(inp_list):
        # solution code
        minimum_number = []
        character_list = list(inp_list[0])
        # print(character_list)
        for i, val in enumerate(character_list):
            val = int(val)
            if i == 0:
                if val == 9:
                    minimum_number.append(val)
                    continue
            if val > 4:
                val = 9 - val
            minimum_number.append(val)

        minimum_number = [str(i) for i in minimum_number]
        print(''.join(minimum_number))




    # run solution function
    solution_function(contents)


"""

    --------------- RUNTIME --------------- 

"""
# test
inp = """4545"""

# test the program; set testProgram flag to True to run pre-defined test cases
testProgram = False
if testProgram:
    main(True, inp)

# if not run in testProgram as True mode. run as program to submit to codeforces
else:
    main()