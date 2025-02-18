contents = []
while True:
    try:
        line = input()
        if len(line) == 0:
            break
    except EOFError:
        break
    contents.append(line)

contents = [[int(i) for i in j.split(" ")] for index_v, j in enumerate(contents[1:]) if index_v % 2 != 0]

grouping_list_real = []
element_list = []
for i in contents:
    t_list = []
    element_grouping_list = []
    temp_list = []
    prev_element = None
    for ii in i:
        # print(temp_list)
        if len(t_list) == 0:
            if ii >= 0:
                t_list.append(1)
            else:
                t_list.append(-1)
            prev_element = ii
            temp_list.append(ii)
        else:
            # check if sign of previous element and current element is matching
            prev_sign = prev_element / abs(prev_element)
            current_sign = ii / abs(ii)
            if prev_sign == current_sign:
                t_list[-1] = t_list[-1] + current_sign
                temp_list.append(ii)
            # the sign is not matching. then:
            else:
                prev_element = ii
                t_list.append(current_sign)
                element_grouping_list.append(temp_list[:])
                temp_list.clear()
                temp_list.append(ii)
    if len(temp_list) > 0:
        element_grouping_list.append(temp_list)

    element_list.append(element_grouping_list)

    t_list = [int(i) for i in t_list]
    grouping_list_real.append(t_list)

# print(grouping_list_real, f"\n{'=' * 20}\n")

# print(element_list)
for i in element_list:
    acc = 0
    for ii in i:
        # if list is positive, get max val
        if min(ii) >= 0:
            acc += max(ii)
        # if list is negative, get min negative value
        else:
            acc += max(ii)
    print(acc)
