#!/usr/bin/env python3
def no_c(my_string):
    new = ""
    for i in range(len(my_string)):
        if (my_string[i] != 'c' or my_string[i] !='C'):
            new += my_string[i]
    return new
