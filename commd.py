import sys
from boardd import *
from ai import ai_turn

Bboard = None
Ssize = 0

def Cstart(nb):
    global Bboard
    global Ssize
    try:
        nb = int(nb)
    except:
        nb = 0
    if nb >= 5 and nb <= 100:
        msg = "OK - everything is good"
        Ssize = nb
        Bboard = []
        for i in range(Ssize):
            Bboard.append([])
            for j in range(Ssize):
                Bboard[i].append('0')
    else:
        msg = "ERROR"
    print("{}".format(msg))
    sys.stdout.flush()
    

def Cturn(nb):
    global Bboard
    global Ssize
    pos_xy = nb.strip().split(",")
    try:
        int(pos_xy[0])
        int(pos_xy[1])
    except:
        print("ERROR")
        sys.stdout.flush()
        return
    if check_inside(int(pos_xy[0]),int(pos_xy[1]),Ssize) == 0:
        if check_val(int(pos_xy[0]), int(pos_xy[1]),Bboard) == 0:
            set_val(int(pos_xy[0]), int(pos_xy[1]), 2,Bboard)
        else:
            print("ERROR")
            sys.stdout.flush()
            return
    else:
        print("ERROR")
        sys.stdout.flush()
        return
    depth = 5
    if Ssize > 5:
        depth = 3
    if Ssize > 15:
        depth = 2
    if Ssize > 20:
        depth = 1
    ai_turn(False, Bboard,Ssize,depth)
    sys.stdout.flush()


def Cboard():
    global Bboard
    global Ssize
    buff = sys.stdin.readline()
    Cbuff = buff.strip().split(" ")
    while(Cbuff[0] != "DONE"):
        pos_xy = buff.strip().split(",")
        try:
            int(pos_xy[0])
            int(pos_xy[1])
            int(pos_xy[2])
        except:
            print("ERROR")
            sys.stdout.flush()
            return
        if check_inside((int(pos_xy[0])),(int(pos_xy[1])),Ssize) == 0:
            set_val(int(pos_xy[0]), int(pos_xy[1]), pos_xy[2],Bboard)
        else:
            print("ERROR in BOARD")
            sys.stdout.flush()
            return
        buff = sys.stdin.readline()
        Cbuff = buff.strip().split(" ")
    depth = 5
    if Ssize > 5:
        depth = 3
    if Ssize > 15:
        depth = 2
    if Ssize > 20:
        depth = 1
    ai_turn(False, Bboard, Ssize,depth)
    sys.stdout.flush()


def Cinfo():
    pass


def Cend():
    sys.exit(0)


def Cabout():
    msg = "name=\"Brainiac\", version=\"1.0\", author=\"pierre.chevalier@epitech.eu florent.piccinini@epitech.eu\", country=\"FRANCE\""
    print(msg)
    sys.stdout.flush()


def Cbegin():
    global Bboard
    global Ssize
    if Bboard != None and Ssize != 0:
        depth = 5
        if Ssize > 5:
         depth = 3
        if Ssize > 15:
            depth = 2
        if Ssize > 20:
            depth = 1
        ai_turn(True, Bboard, Ssize, depth)
    else:
        print("ERROR")
    sys.stdout.flush()
