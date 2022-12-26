def main(lines):
    # このコードは標準入力と標準出力を用いたサンプルコードです。
    # このコードは好きなように編集・削除してもらって構いません。
    # ---
    # This is a sample code to use stdin and stdout.
    # Edit and remove this code as you like.
    highestCount = -1
    numberOfWords = int(lines[0])
    validWords = []

    for validWord in lines[1:numberOfWords+1]:
        if len(validWord) >= 2:
            validWords.append(validWord)

    validWords.sort(reverse=True, key=len)
    numberOfWords = len(validWords)

    highest = -1
    leftInd = 0
    rightInd = 0

    for left in range(0, numberOfWords-1):
        currentHighest = len(validWords[left]) + len(validWords[left + 1])
        if currentHighest < highest:
            break
        for right in range(left + 1, numberOfWords):
            if validWords[left][-2:] == validWords[right][:2] or validWords[right][-2:] == validWords[left][:2]:
                newHigh = len(validWords[left]) + len(validWords[right]) - 2
                if newHigh > highest:
                    highest = newHigh
                    leftInd = left
                    rightInd = right
    
    print(validWords)
    print(highest)
    print(validWords[leftInd])
    print(validWords[rightInd])

if __name__ == '__main__':
    lines = [2, "thirty", "tycoon"]
    main(lines)