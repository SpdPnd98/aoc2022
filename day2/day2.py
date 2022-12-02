def main():
    partTwo()

def partOne():
    with open("input.txt") as f:
        pointMap = {
            "X": 1,
            "Y": 2,
            "Z": 3,
            "A": 1,
            "B": 2,
            "C": 3,
            2: 3,
            1: 6,
            0: 0
        }
        total = 0
        for line in f:
            opponent, played = line.strip("\n").split(" ", 2)
            opponent, played = pointMap[opponent], pointMap[played]
            total += pointMap[(opponent - played + 2) % 3] + played

        print(total)

def partTwo():
    with open("input.txt") as f:
        pointMap = {
            "X": 0,
            "Y": 3,
            "Z": 6,
        }
        actionMap = {
            "A": {
                "Z": 2,
                "X": 3,
                "Y": 1
            },
            "B": {
                "Z": 3,
                "X": 1,
                "Y": 2
            },
            "C": {
                "Z": 1,
                "X": 2,
                "Y": 3
            },
            
        }
        total = 0
        for line in f:
            opponent, result = line.strip("\n").split(" ", 2)
            total += actionMap[opponent][result] + pointMap[result]

        print(total)

if __name__ == "__main__":
    main()