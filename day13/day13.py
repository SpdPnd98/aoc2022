from math import ceil

def main():
    partTwo()

def constructOne(newString, ind=0):
    # assume nothing is malformed
    currentIntStr = ""
    newList = []
    index = ind
    while index < len(newString):
        if newString[index] == "[":
            items, newIndex = constructOne(newString, index+1)
            if index == 0:
                newList.extend(items)
            else:
                newList.append(items)
            index = newIndex
            if index == len(newString) - 1:
                return newList, index
        elif newString[index] == ",":
            if currentIntStr:
                currentInt = int(currentIntStr)
                newList.append(currentInt)
                currentIntStr = ""
        elif newString[index] == "]":
            if currentIntStr:
                currentInt = int(currentIntStr)
                newList.append(currentInt)
                index += 1 # skip over comma
            return newList, index
        else:
            currentIntStr += newString[index]
        index += 1
    
    return newList, 0 # should only be reached when nothing in list

def compare(left, right):
    index = 0
    while index < len(left) and index < len(right):
        # if pass this point, we are still somewhere in the middle of the list
        if isinstance(left[index], list) or isinstance(right[index], list):
            # print("Converting to lists and comparing... %s %s" %(left[index], right[index]))
            newLeft = left[index] if isinstance(left[index], list) else [left[index]]
            newRight = right[index] if isinstance(right[index], list) else [right[index]]

            valid = compare(newLeft, newRight)
            if valid == -1:
                return -1
            elif valid == 1:
                return 1
            # print("Draw, comparing next")
        else:
            # not lists, can compare the items directly
            # print("Left: %d, Right: %d" %(left[index], right[index]))
            if left[index] > right[index]:
                return -1 # wrong order
            elif left[index] < right[index]:
                return 1
            elif left[index] == right[index] and index == len(left) - 1 and len(left) == len(right):
                return 0
        index += 1
    
    if index > len(left) - 1 and len(left) == len(right):
        return 0 # draw
    elif index > len(left) - 1 and len(left) < len(right):
        return 1 # left has less items than right
    else: # if there are any other cases, it must be invalid.
        return -1

def compareWrapper(left, right):
    return compare(left, right) > 0

def partOne():
    with open("input.txt") as f:
        index = 1
        corrects = []
        while True:
            leftRaw = f.readline()[:-1]
            rightRaw = f.readline()[:-1]
            if not leftRaw:
                print("   done.")
                break
            f.readline() # skip a new line
            print("Index %d:" %index)
            left, _ = constructOne(leftRaw)
            right, _ = constructOne(rightRaw)
            print(left)
            print(right)

            if compare(left, right) > 0:
                corrects.append(index)
            index += 1
        
        print("\n")
        print(corrects)
        print(sum(corrects))

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


def partTwo():
    allSignals = [[[2]], [[6]]]
    with open("input.txt") as f:
        while True:
            leftRaw = f.readline()[:-1]
            rightRaw = f.readline()[:-1]
            if not leftRaw:
                print("all signals parsed")
                break
            f.readline() # skip a new line
            left, _ = constructOne(leftRaw)
            right, _ = constructOne(rightRaw)
            allSignals.extend([left, right])
    sort(allSignals, 0, len(allSignals))
    
    print("\n")
    result = 1
    for i, signal in enumerate(allSignals):
        if signal == [[2]]:
            result *= i + 1
        elif signal == [[6]]:
            result *= i + 1
            break
        # print(signal)
    print(result)


if __name__ == "__main__":
    main()