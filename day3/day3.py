def main():
    partTwo()

def partOne():
    with open("input.txt") as f:
        totalPriority = 0
        for line in f:
            cleanLine = line.strip("\n")
            for i in range(0, len(cleanLine) // 2):
                if (cleanLine[len(cleanLine)//2:].find(cleanLine[i]) > -1):
                    print(cleanLine[i])
                    totalPriority += (ord(cleanLine[i]) - 96 if ord(cleanLine[i]) > 90 else ord(cleanLine[i]) - 65 + 27)
        
        print(totalPriority)

def partTwo():
    with open("input.txt") as f:
        totalPriority = 0
        while(True):
            bag_one = f.readline()
            # print(bag_one)
            if bag_one == "":
                print(totalPriority)
                break
            bag_two = f.readline()
            bag_three = f.readline()
            common_item = set(bag_one[: len(bag_one) - 1]).intersection(set(bag_two[: len(bag_two) - 1])).intersection(set(bag_three[: len(bag_three) - 1])).pop()
            print(common_item)
            totalPriority += (ord(common_item) - 96 if ord(common_item) > 90 else ord(common_item) - 65 + 27)

if __name__ == "__main__":
    main()