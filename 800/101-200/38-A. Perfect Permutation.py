"""

Approach:
the question is unclear with p(p(i))??
    * after looking at test cases the pattern has emerged. the solution is derived from swapping 2 elements (for
    convenience swap adjacent elements).
    * the rule is that the "swap pairs" are tightly coupled. so once you swap 2 elements they cannot be reused for
    swaps - 'swap only once' constraint.

    if odd number of elements, then it breaks the 'swap only once' constraint. hence if odd return -1
    else return after all adjacent elements are swapped

    ex: [1 2 3 4 5 6]
    result --> [2 1 4 3 6 5]
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
        if number ==  1 or number % 2 != 0:
            print(-1)
            return
        if number == 2:
            print("2 1")
            return

        list_n = list(range(1, number + 1))
        swapped_list_n = []
        for i in range(0, len(list_n), 2):
            a, b = str(list_n[i]), str(list_n[i+1])
            swapped_list_n += [b, a]
        print(" ".join(swapped_list_n))



    for v in contents:
        # solution code
        solution_function(v)


"""

    --------------- RUNTIME --------------- 

"""
# test
inp = """7"""

# test the program; set testProgram flag to True to run pre-defined test cases
testProgram = False
if testProgram:
    main(True, inp)

# if not run in testProgram as True mode. run as program to submit to codeforces
else:
    main()