"""

Approach:
loop through responses, check if length <= 10;
    if so: compare with highest_found variable. if greater update highest_found to new value
"""
from collections import Counter


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
    contents = [[int(i) for i in j.split(" ")] for j in contents]

    # reorient into response groups
    reoriented_contents = []
    current_index = 0

    # print(contents)
    while True:
        response_group_len = contents[current_index][0]
        response_group = contents[current_index + 1:current_index + response_group_len + 1]
        reoriented_contents.append(response_group)
        current_index = current_index + response_group_len + 1
        if current_index == len(contents):
            break


    def solution_function(response_group_p):
        max_quality_no = -1
        max_quality_found = 0
        for index, response in enumerate(response_group_p):
            number_of_words, quality = response[0], response[1]
            if number_of_words <= 10:
                if quality > max_quality_found:
                    max_quality_found = quality
                    max_quality_no = index + 1
            pass
        print(max_quality_no)


    for v in reoriented_contents:
        # solution code
        solution_function(v)


"""

    --------------- RUNTIME --------------- 

"""
# test
inp = """3
5
7 2
12 5
9 3
9 4
10 1
3
1 2
3 4
5 6
1
1 43"""

# test the program; set testProgram flag to True to run pre-defined test cases
testProgram = False
if testProgram:
    main(True, inp)

# if not run in testProgram as True mode. run as program to submit to codeforces
else:
    main()