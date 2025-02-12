
contents = []
while True:
    try:
        line = input()
        if len(line) == 0:
            break
    except EOFError:
        break
    contents.append(line)

# print(contents)
# user_input = int(user_input)
# sample_inp = """4
# word
# localization
# internationalization
# pneumonoultramicroscopicsilicovolcanoconiosis"""

# processing_llist = user_input.split("\n")
processing_llist = contents
words_list = processing_llist[1:]

def func_to_abbreviate_words(word):
    return_word = word
    if len(word) > 10:
        return_word = word[0] + str(len(word) - 2) + word[-1]
    return return_word


abbr_list = list(map(func_to_abbreviate_words, words_list))
abbr_str = "\n".join(abbr_list)
print(abbr_str)