#!/usr/bin/python3
for alph in range(97, 123):
    if chr(alph) == 'q':
        continue
    elif chr(alph) == 'e':
        continue
    else:
        print("{}".format(chr(alph)), end="")
