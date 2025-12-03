#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum_=0
    for i in range(1, len(sys.argv)):
        sum_.append( int(sys.argv[i]))
print(sum_)
