"""

Approach:
to turn the order in his favor he will;
    position all even bags at the beginning. after which all odd bags are positioned
    he will be in lead with certainty until he gathers all even bags.
    after that each odd bag gathered by bianca reduces his lead
so the solution is simple:
    if; sum(even)  > sum(odd) --> mihai wins
    else --> bianca wins
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
    contents = [[int(j) for j in val.split(" ")] for i, val in enumerate(contents) if i % 2 != 0]
    # print(contents)


    def solution_function(inp_list):
        sum_even_list = sum([i for i in inp_list if i % 2 == 0])
        sum_odd_list = sum(inp_list) - sum_even_list
        if sum_even_list > sum_odd_list:
            print("YES")
        else:
            print("NO")


    for v in contents:
        # solution code
        solution_function(v)


"""

    --------------- RUNTIME --------------- 

"""
# test
inp = """3
4
1 2 3 4
4
1 1 1 2
3
1 4 3"""

# test the program; set testProgram flag to True to run pre-defined test cases
testProgram = False
if testProgram:
    main(True, inp)

# if not run in testProgram as True mode. run as program to submit to codeforces
else:
    main()