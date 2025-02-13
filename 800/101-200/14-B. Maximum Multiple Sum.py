"""

Approach:
If number <= 3 return number. else return sum of all 2 multiples up to that number
Note: get_max_multiple_sum, validate_sum_of_2s are experimenting functions. they do not contribute to the solution,
but rather are for learning purpose
"""
import math


def main (test_mode=False, contents=None):

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
        contents=contents.split("\n")

    contents = contents[1:]

    # split parameters in inputs; cast to int; then collocate parameter with data
    contents = [int(i) for i in contents]
    # print(contents)


    def get_max_multiple_sum(val):
        if val <= 3:
            return val

        # check if number of 2's
        number_of_2s = val // 2
        check_for_even_number_of_2s = (number_of_2s % 2) == 0

        # all 2 are distributed about center. center is the average. soo sum is the product of center into count of 2's
        # for even center does not exist. so decrement counter by 1. get center. then add the truncated multiple of 2
        virtual_number_of_2s = number_of_2s
        if check_for_even_number_of_2s:
            virtual_number_of_2s -= 1

        # for odd center exists
        center_of_2s = math.ceil(virtual_number_of_2s/2) * 2

        result = virtual_number_of_2s * center_of_2s

        # add truncated multiple if even number of 2's
        if check_for_even_number_of_2s:
            result += 2 * number_of_2s
        return result

    def validate_sum_of_2s(a):
        acc = 0
        for i in range(a+1):
            if i% 2 == 0:
                acc += i
        return acc

    def solution_function(val):
        if val <= 3:
            return val
        return 2

    for v in contents:

        # experimental test code; not relevant to solution
        # try:
        #     assert validate_sum_of_2s(v) == get_max_multiple_sum(v)
        # except AssertionError:
        #     print(v)
        # print("Expected --> ", validate_sum_of_2s(v))
        # print("Returned --> ", get_max_multiple_sum(v))

        # solution code
        print(solution_function(v))



#  RUNTIME
# test
inp = """2
3
15
7
8
127
231"""

# test the program; set testProgram flag to True to run pre-defined test cases
testProgram = False
if testProgram:
    main(True, inp)

# if not run in testProgram as True mode. run as program to submit to codeforces
else:
    main()