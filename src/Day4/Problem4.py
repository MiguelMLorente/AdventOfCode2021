import numpy as np
import re

class bingoBoard:
    def __init__(self, board):
        self.board = board
        self.checked = np.zeros_like(board)
        self.complete = False
    
    def checkComplete(self):
        if (self.complete == True):
            return True
        for idx1 in range(0, 5):
            completeRow = True
            completeCol = True
            for idx2 in range(0, 5):
                completeRow = completeRow & (self.checked[idx1, idx2] == 1)
                completeCol = completeCol & (self.checked[idx2, idx1] == 1)
            if (completeRow or completeCol):
                self.complete = True
                return self.complete
        return self.complete
    
    def markNumber(self, num):
        idx = np.where(self.board == num)
        for i in range(0, len(idx[0])):
            self.checked[idx[0][i], idx [1][i]] = True
            
    def getScore(self, last):
        out = 0
        idx = np.where(self.checked == 0)
        for i in range(0, len(idx[0])):
            out += self.board[idx[0][i], idx [1][i]]
        return out * last
            
def charsToInts(array):
    out = []
    for i in array:
        out.append(int(i))
    return out

def readData():
    def readLine(lines):
        chars = re.findall(r"[\w']+", lines.pop(0))
        if (len(chars) == 0):
            return readLine(lines)
        return charsToInts(chars)
    
    with open('input.txt') as f:
        output = []
        lines = f.readlines()
        numbers = readLine(lines)
        boards = []
        while(len(lines) > 0):
            board = []
            for i in range(0,5):
                board.append(readLine(lines))
            boards.append(bingoBoard(np.array(board)))    
    
    return numbers, boards

def getWinningBoard(numbers, boards):
    for n, num in enumerate(numbers):
        for idx in range(0, len(boards)):
            boards[idx].markNumber(num) 
            if boards[idx].checkComplete():
                return boards[idx], num

def getLosingBoard(numbers, boards):
    for n, num in enumerate(numbers):
        for idx in reversed(range(0, len(boards))):
            boards[idx].markNumber(num)
            if boards[idx].checkComplete():
                if (len(boards) == 1):
                    return boards[0], num
                boards.pop(idx)

numbers, boards = readData()
winningBoard, lastNum = getWinningBoard(numbers, boards)
print(winningBoard.getScore(lastNum))

losingBoard, lastNum = getLosingBoard(numbers, boards)
print(losingBoard.getScore(lastNum))