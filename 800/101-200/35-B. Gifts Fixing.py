"""

Approach:
at the end of the day;
    candies should be a repetition of min(c1, c2, c3,...) --> final_candy_count
    oranges should be a repetition of min(o1, o2, o3,...) --> final_orange_count
so to achieve this loop through length of gifts:
    compute;  max(c1 - final_candy_count, o1 - final_orange_count). this is the number of times you should eat to
    get o1 & c1 to final thresholds

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

    # remove the length parameter from input
    contents = [[int(j) for j in val.split(" ")] for i, val in enumerate(contents) if i % 3 != 0]


    def solution_function(gifts):
        candies, oranges = gifts[0], gifts[1]
        final_candy_count, final_orange_count = min(candies), min(oranges)
        times_to_eat_accumulator = 0
        for i in range(len(candies)):
            times_to_eat = max(candies[i] - final_candy_count, oranges[i] - final_orange_count)
            times_to_eat_accumulator += times_to_eat
        print(times_to_eat_accumulator)


    for v in range(0, len(contents), 2):
        # solution code
        solution_function(contents[v:v + 2])


"""

    --------------- RUNTIME --------------- 

"""
# test
inp = """5
3
3 5 6
3 2 3
5
1 2 3 4 5
5 4 3 2 1
3
1 1 1
2 2 2
6
1 1000000000 1000000000 1000000000 1000000000 1000000000
1 1 1 1 1 1
3
10 12 8
7 5 4"""

# test the program; set testProgram flag to True to run pre-defined test cases
testProgram = False
if testProgram:
    main(True, inp)

# if not run in testProgram as True mode. run as program to submit to codeforces
else:
    main()