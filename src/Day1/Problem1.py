def readInts():
    with open('input.txt') as f:
        output = []
        lines = f.readlines()
        for i , num in enumerate(lines):
            output.append(int(num))
        return output
    
def getSlidingDepths(depths):
    output = []
    for i in range(0, len(depths) - 2):
        res = depths[i] + depths[i+1] + depths[i+2]
        output.append(res)
    return output
    
def getHowManyIncreases(arr):
    increasing = 0
    for idx in range(0, len(arr)-1):
        if (arr[idx + 1] > arr[idx]):
            increasing += 1
    return increasing
    
depths = readInts()
print(getHowManyIncreases(depths))

slidingDepths = getSlidingDepths(depths)
print(getHowManyIncreases(slidingDepths))