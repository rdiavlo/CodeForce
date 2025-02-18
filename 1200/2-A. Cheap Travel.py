"""

Approach:
check if the special ticket is actually cheaper compared to normal cost for the same number of 'a' ruble rides
    if yes:
        reduce the number by dividing by m (these are the special rides); (n // m) * b
        then add the price of normal rides; (n % m) * a
    if no: all rides normal; n * a
"""
import math


def main(test_mode=False, contents=None):
    if not test_mode:
        contents = []
        line = input()
        contents.append(line)
    else:
        contents = contents.split("\n")


    contents = [[int(j) for j in val.split(" ")] for i, val in enumerate(contents)]
    # print(contents)


    def solution_function(inp_list):
        # solution code
        n, m, a, b = tuple(inp_list)

        # check is special ride is cheaper
        equivalent_m_normal_rides_price = m * a
        if equivalent_m_normal_rides_price <= b:
            print(n * a)
        else:
            # reduce n by m
            number_of_special_rides = n // m
            cost_special_rides = number_of_special_rides * b

            # at this point check if getting the remainder of rides as special ticket is cheaper
            remaining_rides = n % m

            number_of_special_tickets_needed = math.ceil(remaining_rides/m)
            cost_of_special_tickets = number_of_special_tickets_needed * b
            cost_remaining_rides_at_normal_price = remaining_rides * a

            if (cost_of_special_tickets <= cost_remaining_rides_at_normal_price):
                print(cost_special_rides + cost_of_special_tickets)
            else:
                print(cost_special_rides + cost_remaining_rides_at_normal_price)


    # run solution function
    solution_function(contents[0])


"""

    --------------- RUNTIME --------------- 

"""
# test
inp = """5 2 2 3"""

# test the program; set testProgram flag to True to run pre-defined test cases
testProgram = False
if testProgram:
    main(True, inp)

# if not run in testProgram as True mode. run as program to submit to codeforces
else:
    main()