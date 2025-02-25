"""

Approach:
create a copy of labels and sort it. now loop through the piles as follows;
    piles: [2 7 3 4 9]
    sorted_pile_label
        convert to set to remove duplicated
        then reconvert to list and get a copy
        result: [1 11 25]
    pile_counter (pc) = 0
    result_pile_label_to_pile_number_mapper_dict = {}
    accumulator = 0
    for p in piles:
        pc++
        {
        current pile label range: (accumulator, (accumulator + p)] --> (a, b] where a is exclusive
            get first element in sorted_pile_label;
            loop while True;
                if first element (f_e) falls in pile label range:
                    pop f_e from sorted_pile_label
                    map result; result_pile_label_to_pile_number_mapper_dict[f_e] = pc
                else:
                    break from loop
        }
        accumulator++

    now loop through original pile labels, fetching its corresponding pile number from
    result_pile_label_to_pile_number_mapper_dict. then print it
"""
import math


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

    # remove length params
    contents = [[int(j) for j in val.split(" ")] for i, val in enumerate(contents) if i % 2 != 0]

    # print(contents)


    def solution_function(inp_list):
        # solution code
        piles_list, pile_labels_list = inp_list[0], inp_list[1]

        # copy piles labels, remove duplicates  & sort it
        piles_labels_copy = pile_labels_list[:]
        piles_labels_copy = list(set(piles_labels_copy))
        piles_labels_copy.sort()

        # loop through piles
        pile_counter = 0
        range_accumulator = 0
        result_pile_label_to_pile_number_mapper_dict = {}
        exit_condition = False
        for p in piles_list:
            # increment pile counter
            pile_counter += 1

            # get range values
            a, b = range_accumulator, range_accumulator + p

            # loop through labels
            current_label = piles_labels_copy[0]
            while True:
                if a < current_label <= b:
                    result_pile_label_to_pile_number_mapper_dict[current_label] = pile_counter
                    piles_labels_copy.remove(current_label)
                    if len(piles_labels_copy) > 0:
                        current_label = piles_labels_copy[0]
                    else:
                        exit_condition = True
                        break
                else:
                    break

            if exit_condition:
                break

            # increment range accumulator
            range_accumulator += p

        # loop through pile labels
        # print(result_pile_label_to_pile_number_mapper_dict)
        for l in pile_labels_list:
            print(result_pile_label_to_pile_number_mapper_dict[l])




    # run solution function
    solution_function(contents)


"""

    --------------- RUNTIME --------------- 

"""
# test
inp = """5
2 7 3 4 9
3
1 25 11"""

# test the program; set testProgram flag to True to run pre-defined test cases
testProgram = False
if testProgram:
    main(True, inp)

# if not run in testProgram as True mode. run as program to submit to codeforces
else:
    main()