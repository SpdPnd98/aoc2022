def main():
    partOne()

def partOne():
    allSnarfu = parseSNAFU()
    print("Parsed values: %s" % allSnarfu)
    runningDec = 0
    for snarfu in allSnarfu:
        print("Converting %s to decimal..." % snarfu)
        currentItem = 1
        currentDecimal = 0
        while snarfu:
            newItem = snarfu.pop()
            # print(newItem)
            dec = snarfuToDec(newItem) * currentItem
            runningDec += dec
            currentDecimal += dec
            currentItem *= 5
        print("Decimal is %d" %currentDecimal)
    print("Total decimal is %d" %runningDec)
    result = ""
    snarfuResult = decToSnarfu(runningDec)[::-1]
    for item in snarfuResult:
        result += item
    print("Converting result to Snarfu: %s" %result)
    currentItem = 1
    newRunningDec = 0
    while snarfuResult:
        newItem = snarfuResult.pop()
        # print(newItem)
        dec = snarfuToDec(newItem) * currentItem
        newRunningDec += dec
        currentItem *= 5
    print(newRunningDec)

def partTwo():
    with open("input.txt") as f:
        pass

def parseSNAFU():
    allSnarfu = []
    with open("input.txt") as f:
        for line in f:
            snarfuStack = []
            for char in line.strip():
                # print(char)
                snarfuStack.append(char)
            # print(snarfuStack)
            allSnarfu.append(snarfuStack)
    return allSnarfu

def snarfuToDec(char):
    if char == "2":
        return 2
    elif char == "1":
        return 1
    elif char == "0":
        return 0
    elif char == "-":
        return -1
    elif char == "=":
        return -2
    else:
        print("nani mo")

def base5ToSnarfu(num):
    if num == 4:
        return ["1","-"]
    elif num == 3:
        return ["1","="]
    elif num == 2:
        return ["2"]
    elif num == 1:
        return ["1"]
    elif num == 0:
        return ["0"]
    elif num == -1:
        return ["-"]
    elif num == -2:
        return ["="]
    else:
        return "<not recognized %s >".format(num)

snarfuMap = {
    "2": 2,
    "1": 1,
    "0": 0,
    "-": -1,
    "=": -2
}



def snarfuArithmetic(char1, char2):
    return base5ToSnarfu(snarfuMap[char1] + snarfuMap[char2])[::-1]

def decToSnarfu(dec):
    base_num = []
    while dec>0:
        dig = int(dec%5)
        base_num.append(int(dig))
        dec //= 5
    base_num = base_num[::-1]
    print("  Number in base 5 is %s" %base_num)

    snarfuNum = []
    carryOver = []
    while base_num: # handle carry over
        getDigit = base_num.pop()
        newSnarfuNum = base5ToSnarfu(getDigit)[::-1]
        print("  Converting %s to snarfu %s, carry over %s" %(getDigit, newSnarfuNum, carryOver))
        if carryOver:
            handleCarryOver = snarfuArithmetic(newSnarfuNum[0], carryOver[0])
            print("    Generated new carry over %s" %handleCarryOver)
            snarfuNum.append(handleCarryOver[0])
            if len(handleCarryOver) > 1 and len(newSnarfuNum) > 1:
                carryOver = snarfuArithmetic(handleCarryOver[1], newSnarfuNum[1])
                continue
            elif len(handleCarryOver) > 1:
                carryOver = handleCarryOver[1:2]
                continue
                
        else:
            snarfuNum.append(newSnarfuNum[0])
            print(" current snarfu %s" %snarfuNum)
        carryOver = newSnarfuNum[1:2] # get carry over if exist
        # print(snarfuNum)

    if carryOver:
        snarfuNum.append(carryOver[0])

    # print(snarfuNum)

    return snarfuNum


if __name__ == "__main__":
    main() 