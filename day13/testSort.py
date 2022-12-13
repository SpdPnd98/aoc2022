from math import ceil, floor

def compareWrapper(a, b):
    return a < b

def merge(toSort, leftInd, rightInd, endInd, compareFunc=compareWrapper):
    leftRunning = leftInd
    rightRunning = rightInd
    checkLeft = True
    while rightRunning < endInd:
        if checkLeft:
            if not compareFunc(toSort[leftRunning], toSort[rightInd]):
                temp = toSort[leftRunning]
                toSort[leftRunning] = toSort[rightRunning]
                toSort[rightRunning] = temp
                checkLeft = False
            leftRunning += 1
        else:
            if rightRunning + 1 < endInd and not compareFunc(toSort[rightRunning], toSort[rightRunning + 1]):
                temp = toSort[rightRunning]
                toSort[rightRunning] = toSort[rightRunning + 1]
                toSort[rightRunning + 1] = temp
                rightRunning += 1
            else:
                rightRunning = rightInd
                checkLeft = True
        if leftRunning == rightInd and checkLeft:
            break
            

def sort(toSort, start, end, compareFunc=compareWrapper):
    middle = ceil((start + end) / 2)
    if middle != end:
        sort(toSort, start, middle, compareFunc)
        sort(toSort, middle, end, compareFunc)
        merge(toSort, start, middle, end, compareFunc)

if __name__ == "__main__":
    test = [9, 13, 3, 4, 5, 8, 19, 18, 14, 15, 17, 16,0,12, 2, 1, 7, 6]
    test2 = [4,5,6,2,3,0,-2, -1, -3]
    sort(test,0, len(test))
    print(test)