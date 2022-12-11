from collections import deque

def main():
    partTwo()
    # partOne()

ops = {
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
}

monkeys = {}

def parseSimpleEqn(eqn):
    _, rhs = eqn.split(" = ")
    lOp, op, rOp = rhs.split(" ")

    if lOp == "old" and rOp != "old":
        otherOp = int(rOp)
        return lambda x : ops[op](x, otherOp)
    elif lOp != "old" and rOp == "old":
        otherOp = int(lOp)
        return lambda x : ops[op](otherOp, x)
    else:
        return lambda x : ops[op](x, x)

def parseThrowTo(test, ifMonkey, elseMonkey):
    global monkeys
    return lambda t : monkeys[ifMonkey].receiveItem(t) if test(t) else monkeys[elseMonkey].receiveItem(t)

def parseTest(divideBy):
    return lambda x : x % divideBy == 0

def parseTestImproved(divideBy, idx):
    return lambda x : (x % divideBy).monkeyValues[idx] == 0

def seeInspectedCount():
    global monkeys
    for idx in monkeys:
        print("Monkey %d has inspected items %d times." %(idx, monkeys[idx].seenNumberOfItems))

def findMonkeyBusiness():
    global monkeys
    highest = 0
    secondHighest = 0
    changed = False
    for idx in monkeys:
        monkeyInspected = monkeys[idx].seenNumberOfItems
        if monkeyInspected > secondHighest:
            secondHighest = monkeyInspected
            changed = True
        if changed and secondHighest > highest:
            temp = secondHighest
            secondHighest = highest
            highest = temp
            changed = False
    print(highest * secondHighest)
        

def playOneMonkeyEpisode():
    global monkeys
    for idx in monkeys:
        monkeys[idx].inspect()
        for idxs in monkeys:
            print(monkeys[idxs])

def playOneMonkeyEpisodeWorriedly():
    global monkeys
    for idx in monkeys:
        monkeys[idx].inspectWorriedly()
        # for idxs in monkeys:
        #     print(monkeys[idxs])

def partOne():
    global monkeys
    with open("input.txt") as f:
        while True: 
            collectMonkeyDetail = [f.readline().strip() for _ in range(0, 7)]
            if not any(collectMonkeyDetail):
                break
            idx = int(collectMonkeyDetail[0].split(" ")[1][:-1])
            items = deque([int(i) for i in collectMonkeyDetail[1].split(": ")[1].split(", ")])
            operation = parseSimpleEqn(collectMonkeyDetail[2].split(": ")[1])
            test = parseTest(int(collectMonkeyDetail[3].split(" ")[-1]))
            throwRule = parseThrowTo(test, int(collectMonkeyDetail[4].split(" ")[-1]),
                                           int(collectMonkeyDetail[5].split(" ")[-1]))
            newMonkey = Monkey(idx, items, operation, throwRule)
            monkeys[idx] = newMonkey
        
        for _ in range(0, 5):
            playOneMonkeyEpisode()
            print("")
        
        for idx in monkeys:
            print(monkeys[idx])
        
        seeInspectedCount()
        findMonkeyBusiness()


def partTwo():
    global monkeys
    with open("input.txt") as f:
        # the challenge is that the values are extremely huge, arithmetic takes a long time
        while True: 
            collectMonkeyDetail = [f.readline().strip() for _ in range(0, 7)]
            if not any(collectMonkeyDetail):
                break
            idx = int(collectMonkeyDetail[0].split(" ")[1][:-1])
            items = deque([int(i) for i in collectMonkeyDetail[1].split(": ")[1].split(", ")])
            operation = parseSimpleEqn(collectMonkeyDetail[2].split(": ")[1])
            checkRemainder = int(collectMonkeyDetail[3].split(" ")[-1])
            test = parseTestImproved(checkRemainder, idx)
            throwRule = parseThrowTo(test, int(collectMonkeyDetail[4].split(" ")[-1]),
                                           int(collectMonkeyDetail[5].split(" ")[-1]))
            newMonkey = Monkey(idx, items, operation, throwRule, checkRemainderValue=checkRemainder)
            monkeys[idx] = newMonkey
        
        for idx in monkeys:
            newItems = deque()
            while monkeys[idx].items:
                newItems.append(Item(monkeys[idx].items.popleft()))
            monkeys[idx].items = newItems

        for episode in range(0, 10000):
            print("episode %d" %(episode))
            playOneMonkeyEpisodeWorriedly()
            # print("")
        
        for idx in monkeys:
            print(monkeys[idx])
        
        seeInspectedCount()
        findMonkeyBusiness()

class Monkey:
    def __init__(self, identifier, items, operation, throwRule, checkRemainderValue=1):
        self.identifier = identifier
        self.items = items
        self.seenNumberOfItems = 0
        self.operation = operation
        self.throwRule = throwRule
        self.checkRemainderValue = checkRemainderValue

    def inspect(self):
        while self.items:
            item = self.items.popleft()
            notWorried = self.operation(item)
            self.seenNumberOfItems += 1
            self.throwRule(notWorried)
    
    def inspectWorriedly(self):
        while self.items:
            item = self.items.popleft()
            worried = self.operation(item)
            self.seenNumberOfItems += 1
            self.throwRule(worried)

    def receiveItem(self, item):
        self.items.append(item)

    def __str__(self):
        tempQueue = deque()
        queue = ""
        while self.items:
            item = self.items.popleft()
            tempQueue.append(item)
            queue += str(item) + " "
        self.items = tempQueue
        return "Monkey" + str(self.identifier) + ": " + queue

class Item:
    def __init__(self, initialValue, items=None):
        global monkeys
        self.monkeyValues = {}
        self.original = initialValue
        if items is None:
            for idx in monkeys:
                self.monkeyValues[idx] = initialValue % monkeys[idx].checkRemainderValue
        else:
            self.monkeyValues = items
    
    def __add__(self, other):
        # self.original = self.original + other
        for idx in monkeys:
            self.monkeyValues[idx] = (self.monkeyValues[idx] + other) % monkeys[idx].checkRemainderValue
        return self

    def __radd__(self, other):
        return self.__add__(other)
    
    def __mul__(self, other):
        if isinstance(other, Item):
            # self.original = self.original * other.original
            for idx in monkeys:
                self.monkeyValues[idx] = (self.monkeyValues[idx] * other.monkeyValues[idx]) % monkeys[idx].checkRemainderValue 
            return self
        # self.original = self.original * other   
        for idx in monkeys:
            self.monkeyValues[idx] = (self.monkeyValues[idx] * other) % monkeys[idx].checkRemainderValue
        return self

    def __rmul__(self, other):
        return self.__mul__(other)

    def __mod__(self, other):
        newItems = {}
        for idx in monkeys:
            newItems[idx] = (self.monkeyValues[idx]) % other
        return Item(self.original, newItems)

    def __str__(self):
        return str(self.original)

if __name__ == "__main__":
    main()