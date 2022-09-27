#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    list_copy = my_list[:]
    if 0 <= idx < len(list_copy):
        list_copy[idx] = element
        return (list_copy)
    return (my_list)
