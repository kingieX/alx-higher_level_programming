#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return

    max_num = my_list[0]
    for i in range(1, len(my_list)):
        if max_num < my_list[i]:
            max_num = my_list[i]
        else:
            continue
        return max_num
