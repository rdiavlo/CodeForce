"""

Approach:
0. check if len is 0
    return 0
1. check if len is odd/even
    if odd: indexV --> (n - 1) / 2
    else: indexV --> n / 2
2. loop upto indexV from both directions
    if: forwardElement + backwardElement = 1; add to accumulator
    else: break
    return n - (2 * accumulator)

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
    #  remove lengths in input
    contents = [i for index_v, i in enumerate(contents) if index_v%2 != 0]
    # print(contents)

    def get_min_start_string_length (inp_string):
        string_len = len(inp_string)
        if string_len == 0:
            return 0

        # get index to loop to
        index_v = string_len // 2

        acc = 0
        for i in range(index_v):
            forward, backward = inp_string[i], inp_string[string_len - (i + 1)]
            if int(forward) + int(backward) == 1:
                acc += 1
            else:
                break


        return string_len - (2 * acc)


    for s in contents:
        print(get_min_start_string_length(s))




#  RUNTIME
# test
inp = """9
3
100
4
0111
5
10101
6
101010
7
1010110
1
1
2
10
2
11
10
1011011010"""

# test the program
testProgram = False
if testProgram:
    main(True, inp)

# run actual program for codeforces
else:
    main()