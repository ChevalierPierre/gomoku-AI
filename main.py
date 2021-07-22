#!/usr/bin/python3
import sys
from commd import *


def main():
    while True:
        buff = sys.stdin.readline()
        Cbuff = buff.strip().split(" ")
        if Cbuff[0] == "START":
            Cstart(Cbuff[1])
        elif Cbuff[0] == "TURN":
            Cturn(Cbuff[1])
        elif Cbuff[0] == "BOARD":
            Cboard()
        elif Cbuff[0] == "INFO":
            Cinfo()
        elif Cbuff[0] == "END":
            Cend()
        elif Cbuff[0] == "ABOUT":
            Cabout()
        elif Cbuff[0] == "BEGIN":
            Cbegin()
        else:
            print("ERROR with command: {}".format(Cbuff[0]))
            sys.stdout.flush()


if __name__ == "__main__":
    main()
