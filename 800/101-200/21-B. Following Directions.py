"""

Approach:
based on the move change coordinate. at any point if target is reached return true
"""

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
    # print(contents)

    def solution_function(inp_string):
        inp_list = list(inp_string)
        start_position = [0, 0]
        for i in inp_list:
            if i == "U":
                start_position[1] += 1
            elif i == "D":
                start_position[1] -= 1
            elif i == "R":
                start_position[0] += 1
            else:
                start_position[0] -= 1

            # check if designation point reached
            if start_position == [1, 1]:
                print("YES")
                return
        print("NO")




    for v in contents:
        # solution code
        solution_function(v)


"""

    --------------- RUNTIME --------------- 

"""
# test
inp = """7
7
UUURDDL
2
UR
8
RRRUUDDD
3
LLL
4
DUUR
5
RUDLL
11
LLLLDDRUDRD"""

# test the program; set testProgram flag to True to run pre-defined test cases
testProgram = False
if testProgram:
    main(True, inp)

# if not run in testProgram as True mode. run as program to submit to codeforces
else:
    main()