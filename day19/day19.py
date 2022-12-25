from collections import deque

def main():
    # naiveSolve()
    # anotherAttempt()
    dfsRunner()

import math

def dfsRunner():
    blueprints = parseInputDFS("input.txt")
    total = 0
    for bi, blueprint in enumerate(blueprints):
        maxSpend = [0, 0, 0, 0]
        for recipe in blueprint:
            for i in range(len(recipe)):
                maxSpend[i] = max(maxSpend[i], recipe[i])
        currentBots = (1,0,0,0)
        currentResources = (0,0,0,0)
        minute = 32
        cache = {}
        # print(maxSpend)
        maxGeo = dfs(blueprint, maxSpend, cache, minute, currentBots, currentResources)
        print(maxGeo, bi)
        # total += maxGeo * (bi + 1)
        total *= maxGeo
    print(total)


def dfs(blueprint, maxSpend, cache, minute, currentBots, currentResources):
    if minute == 0:
        return currentResources[3]

    key = (minute, currentBots, currentResources)
    if key in cache:
        return cache[key]

    maxVal = currentResources[3] + currentBots[3] * minute

    for i, recipe in enumerate(blueprint):
        if i != 3 and currentBots[i] >= maxSpend[i]:
            continue

        # skip to next time 
        skipTime = 0
        canMake = True
        for ind, item in enumerate(recipe):
            if item == 0:
                continue
            if currentBots[ind] == 0:
                # print("Cannot make type", ind, "at", i)
                canMake = False
                break
            skipTime = max(skipTime, math.ceil((item - currentResources[ind]) / currentBots[ind]))

        if canMake:
            # print("Can make type", ind)
            if skipTime >= minute + 1:
                # print("escaped")
                continue
            newCurrentBots = [*currentBots]
            newCurrentBots[i] = newCurrentBots[i] + 1
            newCurrentResources = [res + bots * (skipTime + 1) for res, bots in zip(currentResources, currentBots)]
            for ind, item in enumerate(recipe):
                newCurrentResources[ind] -= item
            for i in range(3): # increase possibility to hit cache by "trimming" newResources. i.e. 25 ores at 0th minute == 0 ores at 0th minute, etc.
                newCurrentResources[i] = min(newCurrentResources[i], maxSpend[i] * (minute - skipTime - 1))
            newCurrentBots = tuple(newCurrentBots)
            newCurrentResources = tuple(newCurrentResources)
            maxVal = max(maxVal, dfs(blueprint, maxSpend, cache, minute - skipTime - 1, newCurrentBots, newCurrentResources))

    cache[key] = maxVal
    return maxVal

def parseInputDFS(filename):
    blueprints = []
    with open(filename) as f:
        for line in f:
            tokenized = line[:-1].split(" ")
            oreR = (int(tokenized[6]), 0, 0, 0)
            clayR = (int(tokenized[12]), 0, 0, 0)
            obsR = (int(tokenized[18]), int(tokenized[21]), 0, 0)
            geoR = (int(tokenized[27]), 0, int(tokenized[30]), 0)
            blueprints.append((oreR, clayR, obsR, geoR))
    print(blueprints)
    return blueprints

if __name__ == "__main__":
    main()