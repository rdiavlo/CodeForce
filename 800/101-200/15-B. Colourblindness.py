"""

Approach:
rather simple substitution check.
1. replace all occurrence of green with blue in both strings.
2. check if string 2 equals string 1; if yes same color
is it optimal??
    * including validators and checks will prevent unnecessary replacing
    * looping one by one is better for large strings. will break when mismatch is found (color difference is present)
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

    # remove the len param
    contents = [i for index_v, i in enumerate(contents) if index_v%3 != 0]

    # collocate same rows within matrix; more intuitive
    contents = [[contents[i], contents[i+1]] for i in range(0, len(contents)-1, 2)]
    # print(contents)


    def solution_function(inp_list):
        s1, s2 = inp_list[0], inp_list[1]
        #  replace all green with blue in both strings
        s1_modified = s1.replace("G", "B")
        s2_modified = s2.replace("G", "B")

        if s1_modified == s2_modified:
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
inp = """6
2
RG
RB
4
GRBG
GBGB
5
GGGGG
BBBBB
7
BBBBBBB
RRRRRRR
8
RGBRRGBR
RGGRRBGR
1
G
G"""

# test the program; set testProgram flag to True to run pre-defined test cases
testProgram = False
if testProgram:
    main(True, inp)

# if not run in testProgram as True mode. run as program to submit to codeforces
else:
    main()