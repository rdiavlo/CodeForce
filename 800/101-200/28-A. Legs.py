"""

Approach:
cows are the best option followed by chickens
reduce number; removing all cows by dividing by 4.
divide what value remains by 2
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

    contents = [int(i) for i in contents]
    # print(contents)


    def solution_function(n):
        number_of_cows = n // 4
        remaining_legs = n % 4
        number_of_chicken = remaining_legs // 2
        print(number_of_chicken + number_of_cows)


    for v in contents:
        # solution code
        solution_function(v)


"""

    --------------- RUNTIME --------------- 

"""
# test
inp = """3
2
6
8"""

# test the program; set testProgram flag to True to run pre-defined test cases
testProgram = False
if testProgram:
    main(True, inp)

# if not run in testProgram as True mode. run as program to submit to codeforces
else:
    main()