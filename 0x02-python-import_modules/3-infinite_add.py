#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    cou = 0
    for i in range(len(sys.argv) - 1):
        cou += int(sys.argv[i + 1])
    print("{}".format(total))
