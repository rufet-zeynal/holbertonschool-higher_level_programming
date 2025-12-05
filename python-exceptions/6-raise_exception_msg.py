#!/usr/bin/python3
def raise_exception_msg(message=""):
    try:
        raise NameError('HiThere')
    except NameError:
        print('An exception flew by!')
         raise
