#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    sumo = len(sys.argv) - 1
    if sumo == 0:
        print("0 arguments.")
    elif sumo == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(sumo))
    for j in range(sumo):
        print("{}: {}".format(j + 1, sys.argv[j + 1]))
