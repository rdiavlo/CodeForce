"""

Approach:
Sorting is only concerned with the max and min for each team and not overall strength & itrs distribution.
to solve this;
    1. check for duplicates; if yes return 0
    2. aort and get the difference between consecutive elements. find the min of this
    3. return this min
"""

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

    # remove length of params
    contents = [i for index_v, i in enumerate(contents) if index_v % 2 != 0]

    # split parameters in inputs;
    contents = [[int(j) for j in i.split(" ")] for i in contents]
    # print(contents)


    def get_team_strength_difference(input_list):
        cpy_input_list = input_list.copy()

        # check for duplicates
        unique_inputs = set(cpy_input_list)

        if len(cpy_input_list) != len(unique_inputs):
            return 0

        #  sort inputs
        cpy_input_list.sort()

        # get elemental difference
        difference_list = [cpy_input_list[i + 1] - cpy_input_list[i] for i in range(0, len(cpy_input_list) - 1)]
        min_difference = min(difference_list)

        return min_difference

    for v in contents:
        print(get_team_strength_difference(v))



#  RUNTIME
# test
inp = """5
5
3 1 2 6 4
6
2 1 3 2 4 3
4
7 9 3 1
2
1 1000
3
100 150 200"""

# test the program
testProgram = False
if testProgram:
    main(True, inp)

# run actual program for codeforces
else:
    main()