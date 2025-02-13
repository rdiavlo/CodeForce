"""

Approach:
Use min and max. that wraps it up.
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

    # split parameters in inputs; cast to int; then collocate parameter with data
    contents = [[int(j) for j in i.split(" ")] for i in contents]
    # print(contents)


    def sort_sequence(input_list):
        return str(min(input_list)) + " " + str(max(input_list))

    for v in contents:
        print(sort_sequence(v))



#  RUNTIME
# test
inp = """10
1 9
8 4
1 4
3 4
2 0
2 4
6 9
3 3
0 0
9 9"""

# test the program; set testProgram flag to True to run pre-defined test cases
testProgram = False
if testProgram:
    main(True, inp)

# if not run in testProgram as True mode. run as program to submit to codeforces
else:
    main()