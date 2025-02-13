"""

Approach:
the objective is to pass 0 to opponent;
if the number is even; mahmoud has full hegemony and subtract to get 0 which he passes on & wins
if the number is odd; mahmoud can only subtract even; odd is passed to ehab who reduces it to 0 and passes it on to win
in short if even mahmoud wins. else ehab (zero-sum game)

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

    contents = int(contents[0])
    # print(contents)

    def solution_func(n):
        if n % 2 == 0:
            print("Mahmoud")
            return
        print("Ehab")


    solution_func(contents)




#  RUNTIME
# test
inp = """12"""

# test the program
testProgram = False
if testProgram:
    main(True, inp)

# run actual program for codeforces
else:
    main()