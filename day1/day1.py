def main():
    # partOne()
    partTwo()    

def partOne():
    with open("input.txt") as f:
        highest = -1
        currentSum = 0
        for line in f:
            if line == "\n":
                highest = max(highest, currentSum)
                currentSum = 0
            else:
                currentSum += int(line)
        print(highest)
    
def partTwo():
    with open("input.txt") as f:
        highest_three = [-1, -1, -1]
        currentSum = 0
        for line in f:
            if line == "\n":
                if currentSum >= highest_three[1]:
                    if currentSum >= highest_three[0]:
                        highest_three = [currentSum] + highest_three
                        highest_three = highest_three[:3]
                    else:
                        highest_three[2] = highest_three[1]
                        highest_three[1] = currentSum
                elif currentSum > highest_three[2]:
                    highest_three[2] = currentSum
                # print(currentSum)
                # print (highest_three)
                currentSum = 0
            else:
                currentSum += int(line)
        print(highest_three)
        print(sum(highest_three))

if __name__ == "__main__":
    main()