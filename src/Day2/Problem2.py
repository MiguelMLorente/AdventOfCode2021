class movement:
    def __init__(self, direction, size):
        self.direction = direction
        self.size = size
        
class position:
    def __init__(self):
        self.horizontal = 0
        self.vertical = 0
    
    def move(self, move):
        if (move.direction == "forward"):
            self.horizontal += move.size
        elif (move.direction == "down"):
            self.vertical += move.size
        else:
            self.vertical -= move.size
            
    def printProduct(self):
        print(self.horizontal * self.vertical)
   
        


def readMoves(strategy):
    with open('input.txt') as f:
        output = []
        lines = f.readlines()
        if (strategy == "old"):
            for i , move in enumerate(lines):
                x = move.split(" ")
                output.append(movement(x[0], int(x[1])))
        else:
            aim = 0
            for i , move in enumerate(lines):
                x = move.split(" ")
                if (x[0] == "up"):
                    aim -= int(x[1])
                elif (x[0] == "down"):
                    aim += int(x[1])
                else:
                    output.append(movement("forward", int(x[1])))
                    output.append(movement("down", int(x[1]) * aim))
        return output
    
def getFinalPosition(moves):
    pos = position()
    for i, move in enumerate(moves):
        pos.move(move)
    pos.printProduct()
    
moves = readMoves("old")
getFinalPosition(moves)

moves = readMoves("new")
getFinalPosition(moves)

    