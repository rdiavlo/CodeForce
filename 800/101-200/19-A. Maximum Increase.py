"""

Approach:
1. get the difference between consecutive elements as difference_list; at this point positive means next number is greater
than previous
2. now loop through list and for each island of positive numbers ie contiguous sequence; get width of island
3. print max(width of island)
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
    contents = [int(i) for i in contents[0].split(" ")]

    def solution_function(inp_list):
        cpy_inp_list = inp_list.copy()

        #  check if more than 1 element in list
        if len(cpy_inp_list) <= 1:
            print(1)
            return

        #  check if at least 2 elements are unique
        if len(set(cpy_inp_list)) == 1:
            print(1)
            return

        diff_list = [cpy_inp_list[i+1] - cpy_inp_list[i] for i in range(len(cpy_inp_list)-1)]

        # difference list should have a positive value
        if not (max(diff_list) > 0):
            print(1)
            return

        # at this point; difference list has at least 1 positive element
        current_island_width_max = 0
        final_island_width_max = 1
        for i in diff_list:
            if i > 0:
                current_island_width_max += 1
            else:
                if current_island_width_max > final_island_width_max:
                    final_island_width_max = current_island_width_max

                # reset island length if negative found
                current_island_width_max = 0

        # last diff element may not be negative; check for last island too (corner case)
        if current_island_width_max > final_island_width_max:
            final_island_width_max = current_island_width_max

        print(final_island_width_max + 1)



    solution_function(contents)


"""

    --------------- RUNTIME --------------- 

"""
# test
inp = """5
1 7 2 11 15"""

# test the program; set testProgram flag to True to run pre-defined test cases
testProgram = False
if testProgram:
    main(True, inp)

# if not run in testProgram as True mode. run as program to submit to codeforces
else:
    main()