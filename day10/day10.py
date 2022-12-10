def main():
    partTwo()

def partOne():
    with open("input.txt") as f:
        ticks = 0
        checkTicks = [i for i in range(220, 0, -40)]
        checkTick = checkTicks.pop()
        register = 1
        prevValue = None
        sumAllSignal = 0
        lineNum = 1
        for line in f:
            if checkTick < ticks:
                sumAllSignal += prevValue * checkTick
                print("prev: " + str(lineNum - 1) + " " + str(prevValue * checkTick))
                if len(checkTicks) == 0:
                    break
                checkTick = checkTicks.pop()
            elif checkTick == ticks:
                sumAllSignal += prevValue * ticks
                print("current: " + str(lineNum) + " " + str(prevValue * ticks))
                if len(checkTicks) == 0:
                    break
                checkTick = checkTicks.pop()

            if line == "noop\n":
                ticks += 1
                prevValue = register
            else:
                increment = int(line.strip("\n").split(" ")[1])
                prevValue = register
                register += increment
                ticks += 2
            lineNum += 1
        print(sumAllSignal)

def partTwo():
    with open("input.txt") as f:
        ticks = 0
        runningTick = 0
        row = ""
        register = 1
        prevValue = None
        lineNum = 1
        for line in f:
            if line == "noop\n":
                ticks += 1
                prevValue = register
            else:
                increment = int(line.strip("\n").split(" ")[1])
                prevValue = register
                register += increment
                ticks += 2
            lineNum += 1
            while runningTick <= ticks:
                reference = register if runningTick == ticks else prevValue
                row += "#" if abs(reference - runningTick) <= 1 else "."
                runningTick += 1
                if runningTick > 39:
                    runningTick = runningTick - 40
                    ticks = ticks - 40
                    print(row)
                    row = ""


if __name__ == "__main__":
    main()