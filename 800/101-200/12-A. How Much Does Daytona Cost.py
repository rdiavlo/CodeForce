"""

Approach:
Subsegment can be just 1 element. In that case the answer is as simple as finding if the element exists within the user
input
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
    contents = [[contents[i][1], contents[i+1]] for i in range(0, len(contents)-1, 2)]
    # print(contents)


    def check_if_most_common_then_print(input_list):
        element_to_check, list_to_check = input_list[0], input_list[1]
        if element_to_check in list_to_check:
            print("YES")
            return 1
        print("NO")
        return 0

    for v in contents:
        check_if_most_common_then_print(v)



#  RUNTIME
# test
inp = """7
5 4
1 4 3 4 1
4 1
2 3 4 4
5 6
43 5 60 4 2
2 5
1 5
4 1
5 3 3 1
1 3
3
5 3
3 4 1 5 5"""

# test the program
testProgram = False
if testProgram:
    main(True, inp)

# run actual program for codeforces
else:
    main()