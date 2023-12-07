

def read_board(board):
    return [
        [
            int(number) for number in row.strip().split()
        ] for row in board.split('\n')
    ]


def check_finished(board):
    horizontal, vertical = False, False
    for row in board:
        horizontal = all(element is False for element in row)
        if horizontal:
            break
    for i in range(len(board[0])):
        vertical_row = [row[i] for row in board]
        vertical = all(element is False for element in vertical_row)
        if vertical:
            break
    return horizontal or vertical


def apply_number(board, number):
    for row in board:
        if number in row:
            row[row.index(number)] = False
            return check_finished(board)
    return False


def board_score(board):
    return sum(sum(row) for row in board)


def option1(file_name):
    with open(file_name, 'r') as file:
        file_data = file.read().strip().split('\n\n')
    numbers = [int(number) for number in file_data[0].strip().split(',')]
    boards = [read_board(board) for board in file_data[1:]]
    finished = False
    for number in numbers:
        for board in boards:
            finished = apply_number(board, number)
            if finished:
                break
        if finished:
            break
    return board_score(board) * number


def option2(file_name):
    with open(file_name, 'r') as file:
        file_data = file.read().strip().split('\n\n')
    numbers = [int(number) for number in file_data[0].strip().split(',')]
    boards = [read_board(board) for board in file_data[1:]]
    last_board = []
    for number in numbers:
        boards = [board for board in boards
                  if not apply_number(board, number)]
        if len(boards) == 1:
            last_board = boards[0]
            print(last_board)
        if len(boards) == 0:
            break
    print(last_board)
    print(number)
    return board_score(last_board) * number


# print(option1('day4_test.txt'))
# print(option1('day4.txt'))
# print(option2('day4_test.txt'))
# print(option2('day4.txt'))


myInput = open("day4.txt", "r")

numsStr = myInput.readline()
numsList = numsStr.split(',')
n = 0
while n in range(len(numsList)):
    try:
        numsList[n]=int(numsList[n])
        n += 1
    except:
        numsList.pop(n)

print(myInput)
print(numsList)

boards = myInput.read().split('\n\n')
print("FIRST BOARDS\n")
print(boards)

i = 0
while i in range(len(boards)):
    if boards[i]=='':
        boards.pop[i]
    else:
        i += 1

for i in range(len(boards)):
    boards[i]=boards[i].split('\n')

print("BOARDS SPLIT BY ROW\n")
print(boards)

for i in range(len(boards)):
    j = 0
    while j in range(len(boards[i])):
        if boards[i][j]=='':
            boards[i].pop(j)
        else:
            j += 1

for i in range(len(boards)):
    for j in range(len(boards[i])):
        boards[i][j]=boards[i][j].split(' ')

print("BOARDS SPLIT BY ROW SPLIT INTO CHARS\n")
print(boards)

for i in range(len(boards)):
    for j in range(len(boards[i])):
        k = 0
        while k in range(len(boards[i][j])):
            if boards[i][j][k]=='':
                boards[i][j].pop(k)
            else:
                k += 1

for i in range(len(boards)):
    for j in range(len(boards[i])):
        k = 0
        while k in range(len(boards[i][j])):
            try:
                boards[i][j][k]=int(boards[i][j][k])
                k += 1
            except:
                boards[i][j].pop(k)

print("COMPLETE BOARDS\n")
print(boards)

boardsWon = set()
winningBoard = 0
numJustCalled = 0

n = 0

while len(boardsWon)<len(boards):

        for i in range(len(boards)):
            for j in range(len(boards[i])):
                for k in range(len(boards[i][j])):
                    if boards[i][j][k]==numsList[n]:
                        boards[i][j][k] = -1

        for i in range(len(boards)):
            for j in range(5):
                if (boards[i][j][0]==-1 and\
                    boards[i][j][1]==-1 and\
                    boards[i][j][2]==-1 and\
                    boards[i][j][3]==-1 and\
                    boards[i][j][4]==-1) and\
                    (i not in boardsWon):

                    boardsWon.add(i)
                    if len(boardsWon)==len(boards):
                        winningBoard = i
                        numJustCalled = numsList[n]

        for i in range(len(boards)):
            for j in range(5):
                if (boards[i][0][j]==-1 and\
                    boards[i][1][j]==-1 and\
                    boards[i][2][j]==-1 and\
                    boards[i][3][j]==-1 and\
                    boards[i][4][j]==-1) and\
                    (i not in boardsWon):

                    boardsWon.add(i)
                    if len(boardsWon)==len(boards):
                        winningBoard = i
                        numJustCalled = numsList[n]

        n += 1

print(boardsWon)

def getScore(board):

    score = 0

    for j in range(5):
        for k in range(5):
            if boards[board][j][k]>0:
                score += boards[board][j][k]

    score *= numJustCalled

    return score

winningScore = getScore(winningBoard)

print("The winning board is at ", winningBoard)

print("The winning score is ", winningScore)