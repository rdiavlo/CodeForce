"""

Approach:
loop through rows checking for "?"
    when found; do a set difference with (A, B, C) to get missing element

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


    def solution_function(side_list):
        # print(side_list)
        set_all = {"A", "B", "C"}
        for s in side_list:
            if "?" in s:
                for missing_v in set_all.difference(set(s)):
                    print(missing_v)

    for v in range(0, len(contents), 3):
        # solution code
        solution_function(contents[v:v + 3])


"""

    --------------- RUNTIME --------------- 

"""
# test
inp = """3
ABC
C?B
BCA
BCA
CA?
ABC
?AB
BCA
ABC"""

# test the program; set testProgram flag to True to run pre-defined test cases
testProgram = False
if testProgram:
    main(True, inp)

# if not run in testProgram as True mode. run as program to submit to codeforces
else:
    main()