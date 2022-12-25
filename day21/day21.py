def main():
    partTwo()

def partOne():
    parseMonkes()
    print(allMonke["root"].traverseNode())

def partTwo():
    parseMonkes()
    allMonke["humn"] = "x"
    value = 0
    toMatch = 0
    if allMonke[allMonke["root"].childOne].atChild("humn") != 0:
        value = 1
        toMatch = allMonke[allMonke["root"].childTwo].traverseNode()
    elif allMonke[allMonke["root"].childTwo].atChild("humn") != 0:
        value = -1
        toMatch = allMonke[allMonke["root"].childOne].traverseNode()
        return 
    # print(allMonke[allMonke["root"].childOne])
    lowerBound = 3342154812537
    upperBound = 3342154812538
    step = 1
    if value > 0:
        # print("%d = %s" %(toMatch, str(allMonke[allMonke["root"].childOne])))
        # checks = (x * step for x in range(int(lowerBound * 10000), int(upperBound * 10000)))
        print(toMatch)
        for x in range(lowerBound, upperBound, step):
        # for x in checks:
            result = eval(str(allMonke[allMonke["root"].childOne]) +" - " + str(toMatch))
            if result == toMatch:
                print ("humn shouts", x)
                break
            if result < 0:
                print("Exceed at closest integer", x)
                break
    else:
        # print("%d = %s" %(toMatch, str(allMonke[allMonke["root"].childTwo])))
        for x in range(lowerBound, upperBound, step):
            result = eval(str(allMonke[allMonke["root"].childTwo]) +" - " + str(toMatch))
            if result == toMatch:
                print ("humn shouts", x)
                break
            if result < 0:
                print("Exceed at closest integer", x)
                break
        
    

allMonke = {}

operations = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: x / y,
    "==": lambda x, y: x == y,
}

class Node:
    def __init__(self, current, childOne=None, childTwo=None):
        self.current = current   # store operation
        self.childOne = childOne # identifying name
        self.childTwo = childTwo # identifying name
    
    def traverseNode(self):
        getOperation = operations[self.current]
        if isinstance(allMonke[self.childOne], Node):
            value1 = allMonke[self.childOne].traverseNode()
        else:
            value1 = allMonke[self.childOne]
        if isinstance(allMonke[self.childTwo], Node):
            value2 = allMonke[self.childTwo].traverseNode()
        else:
            value2 = allMonke[self.childTwo]
        
        return int(getOperation(value1, value2))
    
    def atChild(self, target):
        if target == self.childOne:
            return -1 
        elif target == self.childTwo:
            return 1
        else:
            leftChild = allMonke[self.childOne]
            if isinstance(leftChild, Node):    
                atLeft = leftChild.atChild(target)
                if atLeft != 0:
                    return -1
            rightChild = allMonke[self.childTwo]
            if isinstance(rightChild, Node):
                atRight = rightChild.atChild(target)
                if atRight != 0:
                    return 1
            return 0
    
    def __str__(self):
        left = str(allMonke[self.childOne])
        right = str(allMonke[self.childTwo])

        return "(" + left + " " + self.current + " " + right + ")"

def checkOperation(char):
    return char == "+" or char == "-" or char == "*" or char == "/"

def parseMonkes():
    with open("input.txt") as f:
        for line in f:
            currentMonke, operation = line.strip().split(": ")
            splitOps = operation.split(" ")
            if len(splitOps) == 1:
                allMonke[currentMonke] = int(splitOps[0])
            else:
                allMonke[currentMonke] = Node(current=splitOps[1], childOne=splitOps[0], childTwo=splitOps[2])

if __name__ == "__main__":
    main()