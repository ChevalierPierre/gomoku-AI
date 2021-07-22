
def set_val( x, y, nb,boa):
######## set the desired value at this position on the grid
    boa[y][x] = str(nb)

def check_val( x, y,boa):
##### return the value at this position on the grid
    return int(boa[y][x])

def check_inside( x, y,siz):
####### check if the position is inside the grid
    return -1 if (x < 0 or y < 0 or x >= siz or y >= siz) else 0


"""    
###### below there's functions meant to check the victory conditions
def check_win( x, y, nb):
    if check_win_diagonal_right( x, y, nb) == 0:
        return 0
    elif check_win_diagonal_left( x, y, nb) == 0:
        return 0
    elif check_win_horizontal( x, y, nb) == 0:
        return 0
    elif check_win_vertical( x, y, nb) == 0:
        return 0
    else:
        return -1
def check_win_diagonal_right( x, y, nb):
    xx = x
    yy = y
    win = 0
    while(True):
        if check_inside(xx, yy) == -1:
            break
        if check_val(xx,yy) == nb:
            xx += 1
            yy += 1
            win += 1
        else:
            break
    xx = x
    yy = y
    while(True):
        if check_inside(xx, yy) != 0:
            break
        if check_val(xx,yy) == nb:
            xx -= 1
            yy -= 1
            win += 1
        else:
            break
    if win >= 5:
        return 0
def check_win_diagonal_left( x, y, nb):
    xx = x
    yy = y
    win = 0
    while(True):
        if check_inside(xx, yy) == -1:
            break
        if check_val(xx,yy) == nb:
            xx += 1
            yy -= 1
            win += 1
        else:
            break
    xx = x
    yy = y
    while(True):
        if check_inside(xx, yy) != 0:
            break
        if check_val(xx,yy) == nb:
            xx -= 1
            yy += 1
            win += 1
        else:
            break
    if win >= 5:
        return 0
def check_win_horizontal( x, y, nb):
    xx = x
    yy = y
    win = 0
    while(True):
        if check_inside(xx, yy) == -1:
            break
        if check_val(xx,yy) == nb:
            yy += 1
            win += 1
        else:
            break
    xx = x
    yy = y
    while(True):
        if check_inside(xx, yy) != 0:
            break
        if check_val(xx,yy) == nb:
            yy -= 1
            win += 1
        else:
            break
    if win >= 5:
        return 0
def check_win_vertical( x, y, nb):
    xx = x
    yy = y
    win = 0
    while(True):
        if check_inside(xx, yy) == -1:
            break
        if check_val(xx,yy) == nb:
            xx += 1
            win += 1
        else:
            break
    xx = x
    yy = y
    while(True):
        if check_inside(xx, yy) != 0:
            break
        if check_val(xx,yy) == nb:
            xx -= 1
            win += 1
        else:
            break
    if win >= 5:
        return 0
"""