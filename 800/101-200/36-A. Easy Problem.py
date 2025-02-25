"""

Approach:
this stipulates that; a + b = n
assume n = 6:
    a = 1, b = 5
    a = 2, b = 4
    a = 3, b = 3
    a = 4, b = 2
    a = 5, b = 1
    where b is a mirror of a along the vertical axis
    hence the answer to this is the number of pairs that can be formed = (n - 1)

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

    # clean the input
    contents = [int(i) for i in contents]


    def solution_function(number):
        print(number - 1)


    for v in contents:
        # solution code
        solution_function(v)


"""

    --------------- RUNTIME --------------- 

"""
# test
inp = """3
2
4
6"""

# test the program; set testProgram flag to True to run pre-defined test cases
testProgram = False
if testProgram:
    main(True, inp)

# if not run in testProgram as True mode. run as program to submit to codeforces
else:
    main()