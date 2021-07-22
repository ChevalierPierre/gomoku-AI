from boardd import *


evaluationCount = 0
def ai_turn(bgn, board,size,depth):
####### check if it responds to a BEGIN or TURN command then display position of the desired move
        if bgn is True:
                msg = ["3", "3"]
        else:
                msg = calculateNextMove(depth,board,size)
        set_val(int(msg[0]), int(msg[1]), 1,board)
        print("{0},{1}".format(msg[0], msg[1]))


def calculateNextMove(depth,board,size):
        move = []
        i = 0
        while(i < 2):
                i+=1
                move.append(None)
#	long startTime = System.currentTimeMillis()
        bestMove = None
        bestMove = searchWinningMove(board,size)
        if(bestMove != None ):
                move[0] = (bestMove[1])
                move[1] = (bestMove[2])

        else:
                bestMove = minimaxSearchAB(depth,board,size,True,-1,100000000)
                if(bestMove[1] == None):
                        move = None
                else:
                        move[0] = (bestMove[1])
                        move[1] = (bestMove[2])
        global evaluationCount
        evaluationCount=0

        return move


def searchWinningMove(board,size):
        allPossibleMoves = get_moves(size,board)
        winningMove = []
        i = 0
        while(i < 3):
                i+=1
                winningMove.append(None)
        global evaluationCount
        for move in allPossibleMoves:
                evaluationCount+=1
                board2=copy_board(board)
                set_val(move[0],move[1],1,board2) #creating many unwanted pawns

                if(getScore(board2,size,"1",False) >= 100000000):
                        winningMove[1] = move[0]
                        winningMove[2] = move[1]
                        return winningMove
        return None



def gomokuShapeScore(consecutive, openEnds, currentTurn):
        if (openEnds == 0 and consecutive < 5):
                return 0
        elif consecutive == 4:
                if openEnds == 1:
                        if (currentTurn):
                                return 100000000
                        return 50
                if openEnds == 2:
                        if (currentTurn):
                                return 100000000
                        return 100000000/4
        elif consecutive == 3:
                if openEnds == 1:
                        if (currentTurn):
                                return 7
                        return 5
                if openEnds == 2:
                        if (currentTurn):
                                return 50000
                        return 200
        elif consecutive == 2:
                if openEnds == 1:
                        return 2
                if openEnds == 2:
                        if (currentTurn):
                                return 7
                        return 5
        elif consecutive == 1:
                return 1
        else:
                return 200000000

def analyzeVertical(current_turn, pwn, board,size):


        score = 0
        countConsecutive = 0
        openEnds = 0

        for a in range(size):
                for i in range(size):
                        if (board[i][a] == pwn):
                                countConsecutive += 1
                        elif (board[i][a] == '0' and countConsecutive > 0):
                                openEnds += 1
                                score += gomokuShapeScore(countConsecutive, openEnds, current_turn is True)
                                countConsecutive = 0
                                openEnds = 1
                        elif (board[i][a] == '0'):
                                openEnds = 1
                        elif (countConsecutive > 0):
                                score += gomokuShapeScore(countConsecutive, openEnds, current_turn is True)
                                countConsecutive = 0
                                openEnds = 0
                        else:
                                 openEnds = 0
                if (countConsecutive > 0):
                        score += gomokuShapeScore(countConsecutive, openEnds, current_turn is True)
                countConsecutive = 0
                openEnds = 0
        return score

def analyzeHorizontal(current_turn, pwn, board, size):

        score = 0
        countConsecutive = 0
        openEnds = 0

        for i in range(size):
                for a in range(size):
                        if (board[i][a] == pwn):
                                countConsecutive += 1
                        elif (board[i][a] == '0' and countConsecutive > 0):
                                openEnds += 1
                                score += gomokuShapeScore(countConsecutive, openEnds, current_turn is True)
                                countConsecutive = 0
                                openEnds = 1
                        elif (board[i][a] == '0'):
                                openEnds = 1
                        elif (countConsecutive > 0):
                                score += gomokuShapeScore(countConsecutive, openEnds, current_turn is True)
                                countConsecutive = 0
                                openEnds = 0
                        else:
                                 openEnds = 0
                if (countConsecutive > 0):
                        score += gomokuShapeScore(countConsecutive, openEnds, current_turn is True)
                countConsecutive = 0
                openEnds = 0
        return score

"""
def analyzeDiagonal(current_turn, pwn, board, size):

        score = 0
        countConsecutive = 0
        openEnds = 0
        k = 0
        while (k < size):
                j = 0
                while (j <= k):
                        i = k-j
                        if (board[i][j] == pwn):
                                countConsecutive += 1
                        elif (board[i][j] == '0' and countConsecutive > 0):
                                openEnds += 1
                                score += gomokuShapeScore(countConsecutive, openEnds, current_turn is True)
                                countConsecutive = 0
                                openEnds = 1
                        elif (board[i][j] == '0'):
                                openEnds = 1
                        elif (countConsecutive > 0):
                                score += gomokuShapeScore(countConsecutive, openEnds, current_turn is True)
                                countConsecutive = 0
                                openEnds = 0
                        else:
                                 openEnds = 0
                        j += 1
                if (countConsecutive > 0):
                        score += gomokuShapeScore(countConsecutive, openEnds, current_turn is True)
                countConsecutive = 0
                openEnds = 0
                k += 1
                countConsecutive = 0


        openEnds = 0
        k = size - 2
        while (k >= 0):
                j = 0
                while (j <= k):
                        i = k-j
                        if (board[i][j] == pwn):
                                countConsecutive += 1
                        elif (board[i][j] == '0' and countConsecutive > 0):
                                openEnds += 1
                                score += gomokuShapeScore(countConsecutive, openEnds, current_turn is True)
                                countConsecutive = 0
                                openEnds = 1
                        elif (board[i][j] == '0'):
                                openEnds = 1
                        elif (countConsecutive > 0):
                                score += gomokuShapeScore(countConsecutive, openEnds, current_turn is True)
                                countConsecutive = 0
                                openEnds = 0
                        else:
                                 openEnds = 0
                        j += 1
                if (countConsecutive > 0):
                        score += gomokuShapeScore(countConsecutive, openEnds, current_turn is True)
                countConsecutive = 0
                openEnds = 0
                k -= 1

        return score

def analyzeDiagonal2(current_turn, pwn, board, size):

        score = 0
        countConsecutive = 0
        openEnds = 0
        k = 0
        while (k < size):
                j = 0
                while (j <= k):
                        i = k-j
                        if (board[i][j] == pwn):
                                countConsecutive += 1
                        elif (board[j][i] == '0' and countConsecutive > 0):
                                openEnds += 1
                                score += gomokuShapeScore(countConsecutive, openEnds, current_turn is True)
                                countConsecutive = 0
                                openEnds = 1
                        elif (board[j][i] == '0'):
                                openEnds = 1
                        elif (countConsecutive > 0):
                                score += gomokuShapeScore(countConsecutive, openEnds, current_turn is True)
                                countConsecutive = 0
                                openEnds = 0
                        else:
                                 openEnds = 0
                        j += 1
                if (countConsecutive > 0):
                        score += gomokuShapeScore(countConsecutive, openEnds, current_turn is True)
                countConsecutive = 0
                openEnds = 0
                k += 1
                countConsecutive = 0


        openEnds = 0
        k = size - 2
        while (k >= 0):
                j = 0
                while (j <= k):
                        i = k-j
                        if (board[j][i] == pwn):
                                countConsecutive += 1
                        elif (board[j][i] == '0' and countConsecutive > 0):
                                openEnds += 1
                                score += gomokuShapeScore(countConsecutive, openEnds, current_turn is True)
                                countConsecutive = 0
                                openEnds = 1
                        elif (board[j][i] == '0'):
                                openEnds = 1
                        elif (countConsecutive > 0):
                                score += gomokuShapeScore(countConsecutive, openEnds, current_turn is True)
                                countConsecutive = 0
                                openEnds = 0
                        else:
                                 openEnds = 0
                        j += 1
                if (countConsecutive > 0):
                        score += gomokuShapeScore(countConsecutive, openEnds, current_turn is True)
                countConsecutive = 0
                openEnds = 0
                k -= 1

        return score
"""
def getScore(board,size, pwn, blacksTurn):
        return (analyzeHorizontal(blacksTurn,pwn, board, size) +analyzeVertical(blacksTurn, pwn, board,size) +analyzeDiagonal(blacksTurn, pwn, board, size))


def evaluateBoardForWhite(board, blacksTurn,size):
        global evaluationCount
        evaluationCount+= 1


        blackScore = getScore(board,size, "2", blacksTurn)
        whiteScore = getScore(board,size, "1", blacksTurn)

        if(blackScore == 0): blackScore = 1

        return whiteScore / blackScore


def minimaxSearchAB(depth, board,size, max,  alpha, beta):
        if(depth == 0):
                x = None
                x = [evaluateBoardForWhite(board, not max,size),None,None]
                return x
        allPossibleMoves = get_moves(size, board)
        if(len(allPossibleMoves) == 0):
                x = None
                x = [evaluateBoardForWhite(board, not max,size), None,None]
                return x

        bestMove = []
        i = 0
        while(i<3):
                i+=1
                bestMove.append(None)

        if(max):
                bestMove[0] = -1
                for move in allPossibleMoves:
                        board2 = copy_board(board)
                        set_val(move[0], move[1], 1, board2) #creating many unwanted pawns

                        tempMove = None
                        tempMove=(minimaxSearchAB(depth-1, board2,size, not max, alpha, beta))
                        if ((tempMove[0])) > (alpha):
                                alpha = tempMove[0]
                        if (tempMove[0] >= beta):
                                return tempMove
                        if(tempMove[0] > (bestMove[0])):
                                bestMove = tempMove
                                bestMove[1] = move[0]
                                bestMove[2] = move[1]

        else:
                bestMove[0] = 100000000
                bestMove[1] = allPossibleMoves[0][0]
                bestMove[2] = allPossibleMoves[0][1]
                for move in allPossibleMoves:
                        board2 = copy_board(board)
                        set_val(move[0], move[1], 2, board2) #creating many unwanted pawns
                        tempMove = None
                        tempMove=( minimaxSearchAB(depth-1,board2,size, not max, alpha, beta))
                        if(tempMove[0] < beta):
                                beta = (tempMove[0])

                        if((tempMove[0]) <= alpha):
                                return tempMove

                        if(tempMove[0] < bestMove[0]):
                                bestMove = tempMove
                                bestMove[1] = move[0]
                                bestMove[2] = move[1]
        return bestMove


"""
def bestGomokuMove(bturn, depth, board, size):
############## Evaluate recursively the best move to make by comparing score of available moves
#	aiMoveCheck = 25
        color = '1' if bturn else '2'
        xBest = -1
        yBest = -1
        bestScore = -1000000000 if bturn else 1000000000
        analysis = 0
        response = 0
        if (depth % 2 == 0):
                analTurn = bturn
        else:
                analTurn = not bturn
        moves = get_moves(size,board)

        i = len(moves)-1
        while(i >= 0):
                set_val(int(moves[i][0]),int(moves[i][1]), color,board)
                if (depth == 1):
                        if bturn:
                                analysis_horizontal = analyzeHorizontal(analTurn, 1, board,size) - analyzeHorizontal(not analTurn, 2,board,size)
                                analysis_vertical = analyzeVertical(analTurn, 1,board,size) - analyzeVertical(not analTurn, 2,board,size)
                                analysis_diagonal = analyzeDiagonal(analTurn, 1,board,size) - analyzeDiagonal(not analTurn, 2,board,size)
                                if analysis_horizontal >= analysis_vertical and analysis_horizontal >= analysis_diagonal:
                                        analysis = analysis_horizontal
                                elif analysis_vertical >= analysis_horizontal and analysis_vertical >= analysis_diagonal:
                                        analysis = analysis_vertical
                                else:
                                        analysis = analysis_diagonal
                        else:
                                analysis_horizontal = -analyzeHorizontal( analTurn, 1,board,size) + analyzeHorizontal(not analTurn, 2,board,size)
                                analysis_vertical = -analyzeVertical( analTurn, 1,board,size) + analyzeVertical(not analTurn, 2,board,size)
                                analysis_diagonal = -analyzeDiagonal( analTurn, 1,board,size) + analyzeDiagonal(not analTurn, 2,board,size)
                                if analysis_horizontal <= analysis_vertical and analysis_horizontal <= analysis_diagonal:
                                        analysis = analysis_horizontal
                                elif analysis_vertical <= analysis_horizontal and analysis_vertical <= analysis_diagonal:
                                        analysis = analysis_vertical
                                else:
                                        analysis = analysis_diagonal
                        if analysis_horizontal >= analysis_vertical and analysis_horizontal >= analysis_diagonal:
                                analysis = analysis_horizontal
                        elif analysis_vertical >= analysis_horizontal and analysis_vertical >= analysis_diagonal:
                                analysis = analysis_vertical
                        else:
                                analysis = analysis_diagonal
                else:
                        response = bestGomokuMove(not bturn, depth - 1,board,size)
                        analysis = response[2]
                set_val(int(moves[i][0]),int(moves[i][1]), 0,board)
                if ((analysis > bestScore and bturn) or (analysis < bestScore and not bturn)):
                        bestScore = analysis
                        xBest = moves[i][0]
                        yBest = moves[i][1]
                i -= 1
        return [xBest, yBest, bestScore]
"""
def get_moves(size,board):
############### returns the array of available moves not too far from already existing pawns
        tab = []
        k = 0
        distance = []
        l = 0
        for i in range(size):
                for j in range(size):
                        if check_val(j,i,board) != 0:
                                distance.append([])
                                distance[l].append(j)
                                distance[l].append(i)
                                l+=1
                        elif check_val(j,i,board) == 0 and distance == []:
                                tab.append([])
                                tab[k].append(j)
                                tab[k].append(i)
                                k += 1

                        elif check_val(j,i,board) == 0 and close_enough(distance, i, j,l) == 0:
                                tab.append([])
                                tab[k].append(j)
                                tab[k].append(i)
                                k += 1
        return tab

def close_enough(distance, i,j,l):
############# check the distance between pawns and available moves
        for m in range(l):
                if (abs(int(i)-int(distance[m][1])) <= 1 and abs(int(j)-int(distance[m][0])) <= 1):
                        return 0
        return -1

def copy_board(board):
        #made to debug the copy of a global variable that modifies the original
        new_board = []
        for i in range(len(board)):
                new_board.append([])
                new_board[i] = board[i].copy()
#	print(board)
#	print(new_board)
        return new_board
"""
for j in range(len(board[0])):
                        new_board[i].append(board[j][i])
"""

def analyzeDiagonal( playersTurn,forBlack,board, size ):
    consecutive = 0
    blocks = 2
    score = 0
    # From bottom-left to top-right diagonally
    k = 0
    while k <= 2*(len(board) - 1):
        iStart = max(0, k - len(board) + 1)
        iEnd = min(len(board) - 1, k)
        i = iStart
        while ( i <= iEnd):
            j = k - i
            if board[i][j] == str(2 if forBlack else 1):
                consecutive+=1
            elif (board[i][j] == "0"):
                if (consecutive > 0):
                    blocks-=1
                    score += gomokuShapeScore(consecutive, abs(blocks-2), playersTurn is True)
                    consecutive = 0
                    blocks = 1
                else:
                    blocks = 1
            elif consecutive > 0:
                score += gomokuShapeScore(consecutive, abs(blocks-2), playersTurn is True)
                consecutive = 0
                blocks = 2
            else:
                blocks = 2
            i += 1
        if (consecutive > 0):
            score += gomokuShapeScore(consecutive, abs(blocks-2), playersTurn is True)
        consecutive = 0
        blocks = 2
        k+=1


      # From top-left to bottom-right diagonally
    k = 1-len(board)
    while (k < len(board)):
        iStart = max(0, k)
        iEnd = min(len(board) + k - 1, len(board)-1)
        i = iStart
        while (i <= iEnd):
            j = i - k
            if board[i][j] == str(1 if forBlack else 1):
                consecutive += 1
            elif (board[i][j] == "0"):
                if(consecutive > 0):
                    blocks -= 1
                    score += gomokuShapeScore(consecutive, abs(blocks-2), playersTurn is True)
                    consecutive = 0
                    blocks = 1
                else:
                    blocks = 1
            elif (consecutive > 0):
                score += gomokuShapeScore(consecutive, abs(blocks-2), playersTurn is True)
                consecutive = 0
                blocks = 2
            else:
                blocks = 2
            i += 1
        if (consecutive > 0):
            score += gomokuShapeScore(consecutive, abs(blocks-2), playersTurn is True)
        consecutive = 0
        blocks = 2
        k+=1
    return score
