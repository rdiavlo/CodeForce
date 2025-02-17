"""

Approach:
the same 9 numbers repeat but the interval keeps increasing. first 9 out of an interval of 10. then 9 out of an interval
of 100. then 9 out of 10000 & so on..
so it depends on the magnitude of the number. hence check for length of number.

Check example below for steps:

consider 1456:

    length = 4
    completed_intervals = 4 - 1 = 3
    count_completed_intervals = 3 * 9 = 27

    check MSB: it is 1. so the number can either be before 1111 or after 1111
    create virtual max ordinary number: 1111
    if number >= virtual max ordinary no; current_interval_count = MSB
    else; current_interval_count = MSB - 1

    final result = count_completed_intervals + current_interval_count

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

    contents = [int(val) for i, val in enumerate(contents)]


    def solution_function(n):
        stringified_n = str(n)
        len_of_number = len(stringified_n)

        completed_interval_count = (len_of_number - 1) * 9

        # check MSB
        msb = stringified_n[0]
        simulated_highest_ordinary_number = int(msb * len_of_number)
        # print(simulated_highest_ordinary_number)
        if n >= simulated_highest_ordinary_number:
            current_interval_count = int(msb)
        else:
            current_interval_count = int(msb) - 1

        print(completed_interval_count + current_interval_count)







    for v in contents:
        # solution code
        solution_function(v)
        # print("-"*80)


"""

    --------------- RUNTIME --------------- 

"""
# test
inp = """6
11
1
2
3
4
5
100"""

# test the program; set testProgram flag to True to run pre-defined test cases
testProgram = False
if testProgram:
    main(True, inp)

# if not run in testProgram as True mode. run as program to submit to codeforces
else:
    main()