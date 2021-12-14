import numpy as np
from matplotlib import pyplot as plt

class line:
    def __init__(self, p1, p2):
        if (p1[0] == p2[0]):
            self.type = "vertical"
            self.length = abs(p2[1] - p1[1]) + 1
            self.origin = (p1[0], min(p1[1], p2[1]))
        elif (p1[1] == p2[1]):
            self.type = "horizontal"
            self.length = abs(p2[0] - p1[0]) + 1
            self.origin = (min(p1[0], p2[0]), p1[1])
        elif (p2[0] - p1[0] - p2[1] + p1[1] == 0):
            self.type = "diagonal"
            self.length = abs(p2[1] - p1[1]) + 1
            self.origin = (min(p1[0], p2[0]), min(p1[1], p2[1]))
        else:
            self.type = "anti-diagonal"
            self.length = abs(p2[1] - p1[1]) + 1
            self.origin = (min(p1[0], p2[0]), max(p1[1], p2[1]))
    

def readLines():
    def arrToInts(array):
        out = []
        for i in array:
            out.append(int(i))
        return out
    
    with open('input.txt') as f:
        output = []
        data = f.readlines()
        for d in data:
            points = d.split(" -> ")
            p1 = arrToInts(points[0].split(","))
            p2 = arrToInts(points[1].split(","))
            output.append(line(p1, p2))

    return output

def getCoverPattern(lines, allowed):
    grid = np.zeros((1000, 1000))
    for line in lines:
        if (line.type in allowed):
            x = line.origin[0]
            y = line.origin[1]
            for i in range(0, line.length):
                grid[x][y] += 1
                if (line.type == "horizontal"):
                    x += 1
                elif (line.type == "vertical"):
                    y += 1
                elif (line.type ==  "diagonal"):
                    x += 1
                    y += 1
                else:
                    x += 1
                    y -= 1
    return grid.T
    
    
def getNumOfOverlaps(grid):
    out = 0
    for val in grid.reshape(1000000):
        if val >= 2:
            out += 1
    return out
    
data = readLines()
grid = getCoverPattern(data, ["vertical", "horizontal"])
plt.imshow(grid)
plt.show()  
print(getNumOfOverlaps(grid))

grid = getCoverPattern(data, ["vertical", "horizontal", "diagonal", "anti-diagonal"])
plt.imshow(grid)
plt.show()  
print(getNumOfOverlaps(grid))

