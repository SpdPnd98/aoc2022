from collections import deque

def main():
    partTwo()

def partOne():
    with open("input.txt") as f:
        allStacks = []
        doneBuilding = False
        for line in f:
            if not doneBuilding:
                if len(allStacks) == 0:
                    numStacks = len(line) // 4
                    for i in range(0, numStacks + 1):
                        allStacks.append(deque())
                if line[0] == "\n":
                    doneBuilding = True
                    for i in range(1, len(allStacks)):
                        allStacks[i].popleft()
                    continue
                currentIndex = 1
                currentStack = 1
                while currentIndex <= len(line):
                    item = line[currentIndex]
                    if item != " ":
                        allStacks[currentStack].appendleft(item)
                    currentIndex += 4
                    currentStack += 1
            else:
                # print("Running commnads")
                command = line.split(" ")
                move, fr, to = int(command[1]), int(command[3]), int(command[5])
                for i in range(0, move):
                    allStacks[to].extend(allStacks[fr].pop())
                    # print(allStacks)
        print(allStacks)
        for i in range(1, len(allStacks)):
            print(allStacks[i].pop())

def partTwo():
    with open("input.txt") as f:
        allStacks = []
        doneBuilding = False
        for line in f:
            if not doneBuilding:
                if len(allStacks) == 0:
                    numStacks = len(line) // 4
                    for i in range(0, numStacks + 1):
                        allStacks.append(deque())
                if line[0] == "\n":
                    doneBuilding = True
                    for i in range(1, len(allStacks)):
                        allStacks[i].popleft()
                    continue
                currentIndex = 1
                currentStack = 1
                while currentIndex <= len(line):
                    item = line[currentIndex]
                    if item != " ":
                        allStacks[currentStack].appendleft(item)
                    currentIndex += 4
                    currentStack += 1
            else:
                # print("Running commnads")
                command = line.split(" ")
                move, fr, to = int(command[1]), int(command[3]), int(command[5])
                tempDeque = deque()
                for i in range(0, move):
                    tempDeque.extend(allStacks[fr].pop())
                    # print(allStacks)
                for i in range(0, move):
                    allStacks[to].extend(tempDeque.pop())
        print(allStacks)
        for i in range(1, len(allStacks)):
            print(allStacks[i].pop())

if __name__ == "__main__":
    main()