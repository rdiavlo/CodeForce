"""

Approach:
1. get the highest of the three. then subtract the other two from this and sum them up. this is the amount of coins
necessary to equalize all 3. so the val should be >= this sum
2. once equalized the remaining coins should be divisible by 3
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


    # clean up input
    contents = [[int(j) for j in i.split(" ")] for i in contents]
    # print(contents)

    def solution_function(inp_list):
        count_of_coins_to_distribute = inp_list[-1]
        sister_coins_list = inp_list[:3]
        max_val = max(sister_coins_list)
        coins_needed_to_equalize = sum([max_val - i for i in sister_coins_list])

        if count_of_coins_to_distribute < coins_needed_to_equalize:
            print("NO")
            return

        remaining_coins = count_of_coins_to_distribute - coins_needed_to_equalize
        if (remaining_coins % 3) != 0:
            print("NO")
        else:
            print("YES")



    for v in contents:
        # solution code
        solution_function(v)


"""

    --------------- RUNTIME --------------- 

"""
# test
inp = """5
5 3 2 8
100 101 102 105
3 2 1 100000000
10 20 15 14
101 101 101 3"""

# test the program; set testProgram flag to True to run pre-defined test cases
testProgram = False
if testProgram:
    main(True, inp)

# if not run in testProgram as True mode. run as program to submit to codeforces
else:
    main()