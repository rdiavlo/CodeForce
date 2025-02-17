"""

Approach:
reorient the data. once its in vertical grouping, it is as simple as removing non-alphabet"""

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

    contents = contents[1:]

    # group by 8 members
    temp_list = []
    contents = [temp_list[-1].append(i) if index_i % 8 != 0 else temp_list.append([i]) for index_i, i in enumerate(contents)]
    contents = temp_list

    # reorient contents
    # print(contents)
    reorient_contents = []
    for i in range(len(contents)):
        current_matrix = contents[i]
        temp_v =  [[i[index_j] for i in current_matrix] for index_j, j in enumerate(current_matrix)]
        temp_v = [''.join(i) for i in temp_v]
        reorient_contents += [temp_v]

    # print(reorient_contents)

    def solution_function(reoriented_content):
        to_search_characters = set(string.ascii_lowercase)
        for column in reoriented_content:
            column_as_set = set(column)
            if len(column_as_set.intersection(to_search_characters)) > 0:
                print(column.replace(".", ""))
                return
        return

    for v in reorient_contents:
        # solution code
        solution_function(v)


"""

    --------------- RUNTIME --------------- 

"""
# test
inp = """5
........
........
........
........
...i....
........
........
........
........
.l......
.o......
.s......
.t......
........
........
........
........
........
........
........
......t.
......h.
......e.
........
........
........
........
........
.......g
.......a
.......m
.......e
a.......
a.......
a.......
a.......
a.......
a.......
a.......
a......."""

# test the program; set testProgram flag to True to run pre-defined test cases
testProgram = False
if testProgram:
    main(True, inp)

# if not run in testProgram as True mode. run as program to submit to codeforces
else:
    main()