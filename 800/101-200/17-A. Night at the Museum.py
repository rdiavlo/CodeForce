"""

Approach:
this is a bidirectional distance calculation. then selection of minimum distance among both directions
set current index as 0 and element is a
function to get distance;
    input element to find. func checks both directions and returns the smallest distance to move along with new index
update index and add distance to accumulator
"""
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

    # print(contents)

    def solution_function(inp_string):
        alphabet_list = list(string.ascii_lowercase)
        number_of_alphabets = len(alphabet_list)
        # print(alphabet_list)

        def find_new_index_and_min_dist(current_index_p, value_to_find):
            element_index = alphabet_list.index(value_to_find)
            forward_distance = abs(element_index - current_index_p)
            reverse_distance = abs(number_of_alphabets - forward_distance)
            return min(forward_distance, reverse_distance), element_index

        current_index = 0
        accumulator = 0
        for character in inp_string:
            res = find_new_index_and_min_dist(current_index, character)
            accumulator += res[0]
            current_index = res[1]

        print(accumulator)


    for v in contents:
        # solution code
        solution_function(v)


"""

    --------------- RUNTIME --------------- 

"""
# test
inp = """zeus"""

# test the program; set testProgram flag to True to run pre-defined test cases
testProgram = False
if testProgram:
    main(True, inp)

# if not run in testProgram as True mode. run as program to submit to codeforces
else:
    main()