import numpy as np

def readData():
    with open('input.txt') as f:
        output = []
        lines = f.readlines()
        for line in lines:
            nums = []
            for char in line:
                try:
                    nums.append(int(char))
                except:
                    pass
            output.append(nums)
    return output

def sumData(data):
    out = np.zeros_like(data[0])
    for arr in data:
        out += np.array(arr)
    return out
        
def getLessAndMostCommonDigits(data):
    addition = sumData(data)
    most = []
    less = []
    total = len(data)
    threshold = total/2
    for val in addition:
        if val == total:
            most.append(1)
            less.append(1)
        elif val == 0:
            most.append(0)
            less.append(0)
        elif val >= threshold:
            most.append(1)
            less.append(0)
        else:
            most.append(0)
            less.append(1)
    return less, most

def binToInt(arr):
    out = 0
    exp = 0
    for digit in reversed(arr):
        out += digit * (2**exp)
        exp += 1
    return out

def getPowerConsumption(less, most):
    return binToInt(less) * binToInt(most)

def filterData(data, mode, idx=0):
    try:
        out = []
        less, most = getLessAndMostCommonDigits(data)
        if mode == "most":
            digits = most
        elif mode == "least":
            digits = less
            
        for arr in data:
            if (arr[idx] == digits[idx]):
                out.append(arr)
        if (len(out) == 0):
            out = data
        if (len(out) == 1):
            return out[0]
        return filterData(out, mode, idx+1)     
    except:
        pass
    
def getLifeSupportRating(data, less, most):
    o2 = filterData(data, "most")
    co2 = filterData(data, "least")
    return binToInt(o2) * binToInt(co2)
    
data = readData()
lessCommon, mostCommon = getLessAndMostCommonDigits(data)
print(getPowerConsumption(lessCommon, mostCommon))
print(getLifeSupportRating(data, lessCommon, mostCommon))

