"""

Approach:
first filter values in both pockets ie any element should not be >= k
then sort both pockets. after that loop through one pocket with a nested loop through the other pocket
if sum < k. add to counter. otherwise break from nested loop
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
    contents = [[int(j) for j in val.split(" ")] for val in contents]
    # print(contents)


    def solution_function(inp_list):
        k = inp_list[0][2]
        left_pocket, right_pocket = inp_list[1], inp_list[2]
        left_pocket_limited, right_pocket_limited = [i for i in left_pocket if i < k], [i for i in right_pocket if i < k]
        left_pocket_limited.sort()
        right_pocket_limited.sort()
        # print(f"To find k: {k}")
        # print(f"\t{left_pocket_limited}\n\t{right_pocket_limited}")

        pair_counter = 0
        for r in right_pocket_limited:
            for l in left_pocket_limited:
                if r + l > k:
                    break
                else:
                    pair_counter += 1
        print(pair_counter)


    for v in range(0, len(contents), 3):
        # solution code
        solution_function(contents[v:v+3])


"""

    --------------- RUNTIME --------------- 

"""
# test
test_inp = """100
2 5 1
1 1
1 1 1 1 1
5 2 6
4 4 2 4 1
1 3"""

# test the program; set testProgram flag to True to run pre-defined test cases
testProgram = False
if testProgram:
    main(True, test_inp)

# if not run in testProgram as True mode. run as program to submit to codeforces
else:
    main()