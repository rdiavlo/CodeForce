"""

Approach:
this is an operation about the center. combine elements equidistant from the center to get max number of sticks
1. identify center; get half_length ie center index - 1
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

    def solution_function(n):
        n = int(n)
        if n <= 2:
            print(1)
            return

        half_length = (n//2) + (n%2)
        print(half_length)


    for v in contents:
        # solution code
        solution_function(v)


"""

    --------------- RUNTIME --------------- 

"""
# test
inp = """4
1
2
3
4"""

# test the program; set testProgram flag to True to run pre-defined test cases
testProgram = False
if testProgram:
    main(True, inp)

# if not run in testProgram as True mode. run as program to submit to codeforces
else:
    main()