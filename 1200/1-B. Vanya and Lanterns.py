"""

Approach:
get the distance between each consecutive light tower.
then result revolves around the max of this. but remember, the first and last
    if 1 lantern: get max of forward & reverse
    if 2 or more: there are two considerations
        case-1; the distance in-between first/last lantern and endpoint
            get dist;
        case-2; the distance in-between the two lanterns
            get dist; if odd divide by two and round up; if even divide by two
        result is the max of case-1 and case-2 dist
"""
import math
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


    contents = [[int(j) for j in val.split(" ")] for i, val in enumerate(contents)]
    # print(contents)


    def solution_function(inp_list):
        # solution code
        metadata, data = inp_list[0], inp_list[1]
        length_of_street = metadata[1]
        data_cpy = data[:]
        data_cpy.sort()

        # if 1 lantern
        if len(inp_list) == 1:
            print(max(data_cpy[0], length_of_street - data_cpy[0]))
            return

        # get the endpoint distance's
        start_d, end_d = data_cpy[0], length_of_street - data_cpy[-1]

        # get the in-between distance's
        dist_list = [data_cpy[i+1] - data_cpy[i] for i in range(len(data_cpy) - 1)]
        dist_list = [i/2 for i in dist_list]

        # find the max distance
        max_distance = max(dist_list + [start_d, end_d])
        print(max_distance)

    solution_function(contents)



"""

    --------------- RUNTIME --------------- 

"""
# test
inp = """2 5
2 5"""

# test the program; set testProgram flag to True to run pre-defined test cases
testProgram = False
if testProgram:
    main(True, inp)

# if not run in testProgram as True mode. run as program to submit to codeforces
else:
    main()