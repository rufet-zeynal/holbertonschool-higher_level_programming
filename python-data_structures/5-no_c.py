#!/usr/bin/python3
def no_c(my_string):
    newstring = ""
    for st in my_string:
        if st == 'c' or st == 'C':
            continue
        newstring += st
    return newstring
