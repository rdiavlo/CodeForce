"""

Approach:
divide by 2 and get the quotient. this is how many he buys at discounted price. then add the remainder

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

    contents = [[int(j) for j in val.split(" ")] for i, val in enumerate(contents)]
    # print(contents)


    def solution_function(inp_list):
        n, a, b = tuple(inp_list)

        # check if the discount is "actually" a discount; if not buy all for 'a' price
        if  2 * a <= b:
            print(n * a)
            return

        get_discounted_price = (n // 2) * b
        get_remainder_price = (n % 2) * a
        total_price = get_discounted_price + get_remainder_price
        print(total_price)

    for v in contents:
        # solution code
        solution_function(v)


"""

    --------------- RUNTIME --------------- 

"""
# test
inp = """4
2 5 9
3 5 9
3 5 11
4 5 11"""

# test the program; set testProgram flag to True to run pre-defined test cases
testProgram = False
if testProgram:
    main(True, inp)

# if not run in testProgram as True mode. run as program to submit to codeforces
else:
    main()