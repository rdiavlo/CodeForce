contents = []
while True:
	try:
		line = input()
		if len(line) == 0:
			break
	except EOFError:
		break
	contents.append(line)


processing_llist = contents
words_list = processing_llist[1:]
# print(words_list)



def process_statement(statement):
	if statement == "X++" or statement == "++X":
		return 1
	elif (statement == "X--") or (statement == "--X"):
		return -1
statement_execution_result = list(map(process_statement, words_list))
variable_value = sum(statement_execution_result)
print(variable_value)