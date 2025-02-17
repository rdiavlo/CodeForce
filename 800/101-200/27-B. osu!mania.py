"""

Approach:
reorient the input into blocks. for each block
    - for each row, find the position of '#' and append to string. print reversed string

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

    # create blocks
    temp_list = []
    cpy_contents = contents[:]
    while len(cpy_contents) != 0:
        block_size = int(cpy_contents[0])
        block = cpy_contents[1:block_size + 1]
        temp_list.append(block)
        cpy_contents = cpy_contents[block_size + 1:]
    contents = temp_list
    # print(contents)


    def solution_function(block):
        acc = ""
        for row in block:
            acc = acc +  str(row.index("#") + 1) + " "

        print(acc[::-1])




    for v in contents:
        # solution code
        solution_function(v)


"""

    --------------- RUNTIME --------------- 

"""
# test
inp = """3
4
#...
.#..
..#.
...#
2
.#..
.#..
1
...#"""

# test the program; set testProgram flag to True to run pre-defined test cases
testProgram = False
if testProgram:
    main(True, inp)

# if not run in testProgram as True mode. run as program to submit to codeforces
else:
    main()