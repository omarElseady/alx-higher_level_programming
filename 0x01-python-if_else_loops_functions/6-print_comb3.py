#!/usr/bin/python3
for dig1 in range(0, 10):
    for dig2 range(dig1 + 1, 9):
        if dig1 == 8 and dig2 == 9:
            print("{}{}".format(dig1, dig2))
        else:
            print("{}{}".format(dig1, dig2), end=", ")
