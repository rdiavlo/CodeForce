"""

Approach:
the patters division of leaders are all factors of n. so the solution is to find the number of factors < n

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

    contents = [int(i) for i in contents]

    def solution_function(number):
        factor_accumulator = 0
        for i in range(1, number):
            if number % i == 0:
                factor_accumulator += 1
        print(factor_accumulator)


    for v in contents:
        # solution code
        solution_function(v)


"""

    --------------- RUNTIME --------------- 

"""
# test
inp = """10"""

# test the program; set testProgram flag to True to run pre-defined test cases
testProgram = False
if testProgram:
    main(True, inp)

# if not run in testProgram as True mode. run as program to submit to codeforces
else:
    main()