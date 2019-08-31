import random

# A=0, B=10, C=20, D=30, E=40, F=50, G=60, H=70, I=80, J=90
# C5 = 20 + 4 = 24

# C4, D1, D9, E6, G7, H2, H4, H9
alphaMapIslandCoords = [23, 30, 38, 45, 66, 71, 73, 78]

# C4, D1, D9, G7, H2, H4
betaMapIslandCoords = [23, 30, 38, 66, 71, 73]

path1 = ['N', 'N', 'N', 'E', 'E', 'E', 'E', 'S', 'S', 'W', 'W', 'W', 'S']

autoRepairPatterns = [
    'NNNE',
    'NNEN',
    'NENN',
    'ENNN',
    'SSSE',
    'SSES',
    'SESS',
    'ESSS',
    'NNEENWWW',
    'NNWWWNEE',
    'NENENWWW',
    'NENWWWNE',
    'NEENNWWW',
    'NEENWNWW',
    'NEENWWNW',
    'NEENWWWN',
    'NWNEENWW',
    'NWNWWNEE',
    'NWWNEENW',
    'NWWNWNEE',
    'NWWWNNEE',
    'NWWWNENE',
    'NWWWNEEN',
    'ENNENWWW',
    'ENNWWWNE',
    'ENENNWWW',
    'ENENWNWW',
    'ENENWWNW',
    'ENENWWWN',
    'ENWNENWW',
    'ENWNWWNE',
    'ENWWNENW',
    'ENWWNWNE',
    'ENWWWNNE',
    'ENWWWNEN',
    'EENNNWWW',
    'EENNWNWW',
    'EENNWWNW',
    'EENNWWWN',
    'EENWNNWW',
    'EENWNWNW',
    'EENWNWWN',
    'EENWWNNW',
    'EENWWNWN',
    'EENWWWNN',
    'WNNEENWW',
    'WNNWWNEE',
    'WNENENWW',
    'WNENWWNE',
    'WNEENNWW',
    'WNEENWNW',
    'WNEENWWN',
    'WNWNEENW',
    'WNWNWNEE',
    'WNWWNNEE',
    'WNWWNENE',
    'WNWWNEEN',
    'WWNNEENW',
    'WWNNWNEE',
    'WWNENENW',
    'WWNENWNE',
    'WWNEENNW',
    'WWNEENWN',
    'WWNWNNEE',
    'WWNWNENE',
    'WWNWNEEN',
    'WWWNNNEE',
    'WWWNNENE',
    'WWWNNEEN',
    'WWWNENNE',
    'WWWNENEN',
    'WWWNEENN',
    'SSEESWWW',
    'SSWWWSEE',
    'SESESWWW',
    'SESWWWSE',
    'SEESSWWW',
    'SEESWSWW',
    'SEESWWSW',
    'SEESWWWS',
    'SWSEESWW',
    'SWSWWSEE',
    'SWWSEESW',
    'SWWSWSEE',
    'SWWWSSEE',
    'SWWWSESE',
    'SWWWSEES',
    'ESSESWWW',
    'ESSWWWSE',
    'ESESSWWW',
    'ESESWSWW',
    'ESESWWSW',
    'ESESWWWS',
    'ESWSESWW',
    'ESWSWWSE',
    'ESWWSESW',
    'ESWWSWSE',
    'ESWWWSSE',
    'ESWWWSES',
    'EESSSWWW',
    'EESSWSWW',
    'EESSWWSW',
    'EESSWWWS',
    'EESWSSWW',
    'EESWSWSW',
    'EESWSWWS',
    'EESWWSSW',
    'EESWWSWS',
    'EESWWWSS',
    'WSSEESWW',
    'WSSWWSEE',
    'WSESESWW',
    'WSESWWSE',
    'WSEESSWW',
    'WSEESWSW',
    'WSEESWWS',
    'WSWSEESW',
    'WSWSWSEE',
    'WSWWSSEE',
    'WSWWSESE',
    'WSWWSEES',
    'WWSSEESW',
    'WWSSWSEE',
    'WWSESESW',
    'WWSESWSE',
    'WWSEESSW',
    'WWSEESWS',
    'WWSWSSEE',
    'WWSWSESE',
    'WWSWSEES',
    'WWWSSSEE',
    'WWWSSESE',
    'WWWSSEES',
    'WWWSESSE',
    'WWWSESES',
    'WWWSEESS'
]

moves = {
    'N': -1,
    'E': +10,
    'S': +1,
    'W': -10
}

# classes

def getHumanCoord(numberCoord):
    return str(chr(65 + (numberCoord // 10))) + str((numberCoord % 10) + 1)

def checkPathAtCoord(currentCoord, remainingPath, islandCoords, currentCount):
    if (currentCoord in islandCoords):
        return False
    if (len(remainingPath) == 0):
        return True
    nextMove = remainingPath.pop(0)
    if (nextMove == 'N' and currentCoord % 10 == 0):
        return False
    if (nextMove == 'E' and currentCoord >= 90):
        return False
    if (nextMove == 'S' and currentCoord % 10 == 9):
        return False
    if (nextMove == 'W' and currentCoord < 10):
        return False
    nextCoord = currentCoord + moves[nextMove]
    return checkPathAtCoord(nextCoord, remainingPath, islandCoords, currentCount + 1)

def getPathPossibleStartCoords(path):
    #print('Get possible start coords for path: ', path)
    possibleStartCoords = []
    for startCoord in range(100):
        if checkPathAtCoord(startCoord, path.copy(), alphaMapIslandCoords, 0):
            possibleStartCoords.append(startCoord)
    return possibleStartCoords

def pathIsALoop(path):
    return path.count('N') == path.count('S') and path.count('E') == path.count('W')

def pathHasInnerLoops(path):
    #print('Check loops in path: ', path)
    # length for loop is 2 min, and has to be even
    for start in range(len(path) - 1):
        for end in range(start + 2, len(path) + 1, 2):
            if pathIsALoop(path[start:end]):
                #print(path[start:end])
                return True
    return False

def pathHasSufficiantAutoRepair(path, maxBreakdowns):
    moveCounts = {
        'N': 0,
        'E': 0,
        'S': 0,
        'W': 0
    }
    for move in path:
        moveCounts[move] += 1
        if (moveCounts[move] > 3):
            if (move in ['N', 'S', 'W'] and moveCounts['E'] > 0):
                # auto-repair
                moveCounts['E'] -= 1
                moveCounts[move] -= 3
            elif (move == 'E' and moveCounts['N'] >= 3):
                # auto-repair NNNE
                moveCounts['E'] -= 1
                moveCounts['N'] -= 3
            elif (move == 'E' and moveCounts['S'] >= 3):
                # auto-repair SSSE
                moveCounts['E'] -= 1
                moveCounts['S'] -= 3
            elif (move == 'E' and moveCounts['W'] >= 3):
                # auto-repair WWWE
                moveCounts['E'] -= 1
                moveCounts['W'] -= 3
            else:
                return False
    # repair remaining breakdowns
    for move in ['N', 'S', 'W']:
        if moveCounts[move] >= 3 and moveCounts['E'] > 0:
            moveCounts[move] -= 3
            moveCounts['E'] -= 1
    return sum(moveCounts.values()) <= maxBreakdowns

def pathIsValid(path, maxBreakdowns):
    return not pathHasInnerLoops(path) and pathHasSufficiantAutoRepair(path, maxBreakdowns)

def generateRandomPath(length):
    moves = ['N', 'E', 'S', 'W'];
    path = []
    while length > 0:
        path.append(moves[random.randrange(4)])
        length -= 1
    return path

def evaluatePath(path, maxBreakdowns, minScore):
    if pathIsValid(path, maxBreakdowns):
        possibleStartCoords = getPathPossibleStartCoords(path)
        if (len(possibleStartCoords) >= minScore):
            print('Score', len(possibleStartCoords), 'for path:', path)
            print(' '.join([getHumanCoord(c) for c in possibleStartCoords]))

def checkRandomPaths(length, maxBreakdowns, minScore, attempts, logStep):
    while attempts > 0:
        if attempts % logStep == 0:
            print('Remaining', attempts, 'attempts')
        path = generateRandomPath(length)
        evaluatePath(path, maxBreakdowns, minScore)
        attempts -= 1

def checkExhaustivePaths(length, maxBreakdowns, minScore, logStep):
    path = ['N'] * length
    lastPath = ['W'] * length
    attempts = 4  ** length
    while path != lastPath:
        if attempts % logStep == 0:
            print('Remaining', attempts, 'attempts')
        attempts -= 1
        evaluatePath(path, maxBreakdowns, minScore)
        for i in range(length - 1, -1, -1):
            if path[i] != 'W':
                if path[i] == 'S':
                    path[i] = 'W'
                if path[i] == 'E':
                    path[i] = 'S'
                if path[i] == 'N':
                    path[i] = 'E'
                break
            else:
                path[i:] = ['N'] * (length - i)
                continue
    evaluatePath(path, maxBreakdowns, minScore)

def checkExhaustivePathsWithAutoRepairPatterns(length, minScore):
    if length % 4 or length < 12:
        print('length should be a multiple of 4 and at least 12. Abort.')
        return
    paths = autoRepairPatterns.copy()
    somePathsAreIncomplete = True
    while somePathsAreIncomplete:
        somePathsAreIncomplete = False
        pathsToAppend = []
        pathsToRemove = []
        for path in paths:
            pathLength = len(path)
            if pathLength < length:
                pathsToRemove.append(path)
                for pattern in autoRepairPatterns:
                    if pathLength + len(pattern) <= length:
                        pathsToAppend.append(path + pattern)
        for pathToAppend in pathsToAppend:
            lengthOfPathToAppend = len(pathToAppend)
            if lengthOfPathToAppend < length:
                paths.append(pathToAppend)
                somePathsAreIncomplete = True
            if lengthOfPathToAppend == length:
                evaluatePath(list(pathToAppend), 0, minScore)
            if lengthOfPathToAppend > length:
                pathsToRemove.append(pathToAppend)
        for pathToRemove in pathsToRemove:
            paths.remove(pathToRemove)

checkExhaustivePathsWithAutoRepairPatterns(20, 4)

# checkExhaustivePaths(12, 0, 10, ...)
# Score 10 for path: ['N', 'N', 'N', 'E', 'S', 'E', 'S', 'S', 'E', 'N', 'N', 'N'] = "N 1"
# A7 A8 B4 B5 C9 C10 D5 D6 F7 F8
# Score 10 for path: ['N', 'N', 'N', 'E', 'S', 'S', 'E', 'S', 'E', 'N', 'N', 'N'] = "N 2"
# A6 A7 A8 B4 C8 C9 D5 D6 F6 F7
# Score 10 for path: ['E', 'N', 'W', 'N', 'N', 'E', 'N', 'W', 'N', 'E', 'N', 'W'] = "snake up 1"
# A7 A8 A9 A10 D8 F9 I7 I8 I9 I10
# Score 10 for path: ['E', 'S', 'W', 'S', 'E', 'S', 'W', 'S', 'S', 'E', 'S', 'W'] = "snake down"
# A1 A2 A3 A4 D2 F3 I1 I2 I3 I4
# Score 10 for path: ['W', 'N', 'E', 'N', 'W', 'N', 'N', 'E', 'N', 'W', 'N', 'E'] = "snake up 2"
# B7 B8 B9 B10 C7 G10 J7 J8 J9 J10
# Score 10 for path: ['W', 'N', 'E', 'N', 'W', 'N', 'E', 'N', 'N', 'W', 'N', 'E'] = "snake up 3"
# B7 B8 B9 B10 D8 F10 J7 J8 J9 J10
# Score 10 for path: ['W', 'S', 'E', 'S', 'S', 'W', 'S', 'E', 'S', 'W', 'S', 'E'] = "snake down 2"
# B1 B2 B3 B4 D2 F4 J1 J2 J3 J4
# Score 10 for path: ['W', 'S', 'E', 'S', 'W', 'S', 'S', 'E', 'S', 'W', 'S', 'E'] = "snake down 3"
# B1 B2 B3 B4 C1 G4 J1 J2 J3 J4

# checkRandomPaths(16, 0, 5, ...)
# Score 5 for path: ['E', 'S', 'S', 'W', 'W', 'W', 'W', 'N', 'W', 'W', 'N', 'N', 'E', 'E', 'E', 'S']
# F8 H6 I3 I4 I6
# Score 6 for path: ['S', 'S', 'E', 'S', 'E', 'N', 'N', 'E', 'N', 'N', 'W', 'W', 'W', 'N', 'N', 'E']
# A4 A6 A7 B4 D5 G4
# Score 7 for path: ['S', 'S', 'W', 'W', 'W', 'N', 'N', 'E', 'N', 'N', 'N', 'E', 'E', 'S', 'E', 'N']
# D5 D6 F5 F6 F8 I4 ?6
# Score 5 for path: ['N', 'N', 'E', 'N', 'N', 'N', 'N', 'E', 'E', 'S', 'S', 'S', 'S', 'S', 'S', 'E']
# A8 C8 C9 C10 F7
# Score 5 for path: ['S', 'W', 'N', 'W', 'W', 'N', 'E', 'N', 'N', 'N', 'E', 'E', 'S', 'S', 'E', 'N']
# D6 D7 F7 F8 I5
# Score 5 for path: ['S', 'W', 'N', 'W', 'W', 'N', 'N', 'E', 'N', 'N', 'E', 'E', 'S', 'S', 'E', 'N']
# D6 D7 F7 F8 I5
# Score 5 for path: ['W', 'W', 'N', 'E', 'N', 'N', 'N', 'N', 'N', 'E', 'S', 'E', 'E', 'S', 'S', 'W']
# C7 C8 E8 G8 G10
# Score 6 for path: ['N', 'E', 'E', 'S', 'S', 'W', 'S', 'W', 'W', 'N', 'N', 'N', 'N', 'E', 'N', 'E']
# B4 B6 D8 E5 G4 G6
# Score 5 for path: ['E', 'S', 'W', 'S', 'S', 'E', 'E', 'N', 'N', 'E', 'N', 'N', 'N', 'W', 'N', 'W']
# A4 A5 C7 D4 E7
# Score 5 for path: ['S', 'S', 'W', 'W', 'N', 'N', 'E', 'N', 'W', 'N', 'N', 'N', 'E', 'S', 'E', 'E']
# C5 C6 C8 D6 H6
# Score 5 for path: ['N', 'N', 'N', 'E', 'S', 'E', 'E', 'S', 'S', 'S', 'W', 'W', 'S', 'W', 'S', 'E']
# A4 A5 A7 B4 F7
# Score 5 for path: ['E', 'E', 'S', 'S', 'S', 'E', 'N', 'E', 'S', 'S', 'S', 'W', 'W', 'W', 'N', 'N']
# A5 B2 B5 E3 F5
# Score 5 for path: ['S', 'W', 'W', 'W', 'N', 'E', 'N', 'N', 'N', 'N', 'E', 'E', 'S', 'S', 'E', 'N']
# D6 D7 F6 F7 I5

# checkExhaustivePathsWithAutoRepairPatterns(12, 8)
# Score 8 for path: ['E', 'S', 'S', 'S', 'S', 'W', 'S', 'E', 'E', 'S', 'W', 'W']
# A1 A2 A3 A4 C2 E3 E4 H1
# Score 8 for path: ['E', 'S', 'S', 'S', 'W', 'W', 'S', 'W', 'S', 'S', 'E', 'E']
# C2 C3 D2 E1 E2 E4 F1 I4
# Score 8 for path: ['W', 'W', 'N', 'N', 'E', 'E', 'N', 'W', 'N', 'N', 'E', 'N']
# C8 D10 E7 E10 F7 I10 J7 J8
# Score 8 for path: ['W', 'W', 'N', 'W', 'N', 'E', 'E', 'N', 'N', 'N', 'E', 'N']
# D10 E7 E8 E10 F7 G9 I10 J7
# Score 8 for path: ['W', 'W', 'N', 'W', 'N', 'E', 'E', 'N', 'E', 'N', 'N', 'N']
# D8 D10 E7 E8 F7 G9 I10 J7
# Score 8 for path: ['W', 'W', 'W', 'N', 'N', 'E', 'N', 'E', 'E', 'N', 'N', 'N']
# D8 D10 E8 F7 F8 F10 I8 J10
# Score 9 for path: ['W', 'W', 'W', 'N', 'N', 'E', 'E', 'N', 'E', 'N', 'N', 'N']
# D8 D10 E7 E8 F7 F10 I8 I10 J10
# Score 8 for path: ['S', 'E', 'E', 'S', 'S', 'W', 'W', 'W', 'S', 'S', 'S', 'E']
# B2 B4 C2 D2 D4 E1 E2 G2
# Score 8 for path: ['S', 'W', 'W', 'W', 'S', 'S', 'E', 'E', 'S', 'S', 'S', 'E']
# D2 D4 E2 F4 G2 G4 I2 J2
# Score 8 for path: ['E', 'E', 'S', 'S', 'S', 'W', 'W', 'W', 'S', 'S', 'S', 'E']
# B2 B3 C2 D2 D4 E1 E2 G3
# Score 8 for path: ['N', 'N', 'N', 'E', 'N', 'N', 'N', 'E', 'S', 'E', 'S', 'S']
# A7 A8 C8 C9 C10 D7 D8 E10
# Score 9 for path: ['N', 'N', 'N', 'E', 'N', 'N', 'N', 'E', 'E', 'S', 'S', 'S']
# A8 A9 C8 C9 C10 D7 D8 F7 F9
# Score 9 for path: ['N', 'N', 'N', 'E', 'S', 'S', 'S', 'E', 'E', 'N', 'N', 'N']
# A5 A6 A7 A8 B10 C8 D5 F5 F6
# Score 10 for path: ['N', 'N', 'N', 'E', 'S', 'S', 'E', 'S', 'E', 'N', 'N', 'N']
# A6 A7 A8 B4 C8 C9 D5 D6 F6 F7
# Score 10 for path: ['N', 'N', 'N', 'E', 'S', 'E', 'S', 'S', 'E', 'N', 'N', 'N']
# A7 A8 B4 B5 C9 C10 D5 D6 F7 F8
# Score 8 for path: ['N', 'N', 'N', 'E', 'E', 'S', 'S', 'S', 'E', 'N', 'N', 'N']
# A8 B5 C10 D5 D6 F8 G4 G6
# Score 8 for path: ['N', 'N', 'E', 'N', 'E', 'S', 'S', 'S', 'E', 'N', 'N', 'N']
# A8 B5 C10 D4 D5 D6 F8 G10
# Score 8 for path: ['S', 'S', 'S', 'E', 'N', 'N', 'N', 'E', 'E', 'S', 'S', 'S']
# A2 A3 A5 B7 C5 D2 F1 F3
# Score 9 for path: ['S', 'S', 'S', 'E', 'E', 'N', 'N', 'N', 'E', 'N', 'N', 'N']
# A5 A6 A7 B4 B5 C7 D4 D5 F5
# Score 8 for path: ['S', 'S', 'E', 'S', 'E', 'N', 'N', 'N', 'E', 'N', 'N', 'N']
# A5 A6 A7 B4 B5 D5 D6 G4
# Score 8 for path: ['S', 'E', 'S', 'S', 'E', 'N', 'N', 'N', 'N', 'E', 'N', 'N']
# A6 A7 B4 B5 D6 D7 G4 G5
# Score 8 for path: ['S', 'E', 'S', 'S', 'E', 'N', 'N', 'N', 'E', 'N', 'N', 'N']
# A5 A6 A7 B4 B5 D6 G4 G5

# checkExhaustivePathsWithAutoRepairPatterns(16, 6)
# Score 6 for path: ['E', 'N', 'E', 'N', 'W', 'W', 'W', 'N', 'W', 'W', 'W', 'S', 'S', 'S', 'E', 'E']
# E5 E10 G8 H5 H7 H8
# Score 6 for path: ['E', 'N', 'W', 'N', 'E', 'N', 'W', 'W', 'W', 'W', 'W', 'S', 'S', 'S', 'E', 'E']
# E5 E10 F5 F6 H8 I4
# Score 6 for path: ['E', 'N', 'W', 'N', 'E', 'N', 'W', 'W', 'W', 'W', 'W', 'S', 'S', 'E', 'S', 'E']
# E5 E10 F6 H8 I4 I6
# Score 6 for path: ['E', 'E', 'N', 'N', 'W', 'W', 'W', 'N', 'W', 'W', 'S', 'E', 'S', 'W', 'S', 'E']
# D4 D5 D10 E10 G5 H5
# Score 6 for path: ['E', 'E', 'N', 'N', 'W', 'W', 'W', 'N', 'W', 'W', 'S', 'W', 'S', 'S', 'E', 'E']
# E5 E10 G8 G10 H5 H7
# Score 7 for path: ['E', 'E', 'N', 'N', 'W', 'W', 'W', 'N', 'W', 'W', 'W', 'S', 'S', 'S', 'E', 'E']
# E5 E10 G8 G10 H5 H7 H8
# Score 6 for path: ['E', 'E', 'N', 'W', 'N', 'W', 'W', 'N', 'W', 'W', 'S', 'E', 'S', 'W', 'S', 'E']
# D4 D5 D10 E9 E10 H5
# Score 6 for path: ['E', 'E', 'N', 'W', 'N', 'W', 'W', 'N', 'W', 'W', 'S', 'W', 'S', 'S', 'E', 'E']
# E5 E9 E10 G8 H5 H7
# Score 8 for path: ['E', 'E', 'N', 'W', 'N', 'W', 'W', 'N', 'W', 'W', 'W', 'S', 'S', 'S', 'E', 'E']
# E5 E9 E10 F6 G8 H5 H7 H8
# Score 7 for path: ['E', 'E', 'N', 'W', 'N', 'W', 'W', 'N', 'W', 'W', 'W', 'S', 'S', 'E', 'S', 'E']
# E5 E9 E10 F6 G8 H5 H8
# Score 6 for path: ['E', 'E', 'N', 'W', 'N', 'W', 'W', 'N', 'W', 'W', 'W', 'S', 'S', 'E', 'E', 'S']
# E9 E10 F6 G8 H5 H8
# Score 6 for path: ['E', 'E', 'N', 'W', 'W', 'N', 'W', 'N', 'W', 'W', 'W', 'S', 'S', 'S', 'E', 'E']
# E5 E9 E10 F6 H7 H8
# Score 6 for path: ['W', 'W', 'N', 'W', 'N', 'E', 'E', 'N', 'E', 'N', 'N', 'W', 'W', 'W', 'N', 'E']
# D8 D10 E7 E8 G9 I10
# Score 6 for path: ['W', 'W', 'W', 'N', 'N', 'N', 'E', 'E', 'E', 'N', 'N', 'W', 'W', 'W', 'N', 'E']
# D8 D10 E8 F8 G8 I8
# Score 6 for path: ['W', 'W', 'W', 'N', 'N', 'E', 'E', 'N', 'E', 'N', 'N', 'W', 'W', 'W', 'N', 'E']
# D8 D10 E7 E8 I8 I10
# Score 6 for path: ['W', 'W', 'W', 'N', 'N', 'E', 'E', 'N', 'E', 'N', 'E', 'N', 'W', 'W', 'W', 'N']
# D8 E7 E8 F10 I8 I10
# Score 6 for path: ['S', 'E', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'W', 'N', 'N', 'W', 'N', 'E', 'E']
# E2 E7 F5 G2 G5 H7
# Score 7 for path: ['S', 'E', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'W', 'N', 'E', 'N', 'W', 'N', 'E']
# D2 D4 D7 E7 F5 G2 H7
# Score 6 for path: ['S', 'W', 'W', 'S', 'W', 'S', 'E', 'E', 'E', 'S', 'W', 'W', 'W', 'S', 'S', 'E']
# D2 D4 E4 F4 G1 I2
# Score 6 for path: ['S', 'W', 'W', 'W', 'S', 'S', 'E', 'E', 'S', 'W', 'W', 'W', 'S', 'S', 'E', 'E']
# E2 E4 F4 G1 G4 J2
# Score 6 for path: ['S', 'W', 'W', 'W', 'S', 'S', 'E', 'E', 'E', 'S', 'W', 'W', 'W', 'S', 'S', 'E']
# D2 D4 E4 F4 G1 I2
# Score 6 for path: ['S', 'W', 'W', 'W', 'S', 'E', 'S', 'E', 'S', 'W', 'W', 'S', 'W', 'S', 'E', 'E']
# E4 F1 F4 G1 I2 J4
# Score 8 for path: ['S', 'W', 'W', 'W', 'S', 'E', 'S', 'E', 'E', 'S', 'W', 'W', 'W', 'S', 'S', 'E']
# D2 D4 E4 F1 F4 G1 I2 J4
# Score 6 for path: ['S', 'W', 'W', 'W', 'S', 'E', 'E', 'S', 'S', 'W', 'W', 'S', 'W', 'S', 'E', 'E']
# E1 E4 F1 G1 I4 J4
# Score 6 for path: ['S', 'W', 'W', 'W', 'S', 'E', 'E', 'S', 'S', 'W', 'W', 'W', 'S', 'S', 'E', 'E']
# E1 E4 F1 G1 I4 J4
# Score 6 for path: ['S', 'W', 'W', 'W', 'S', 'E', 'E', 'S', 'S', 'W', 'W', 'W', 'S', 'E', 'S', 'E']
# E1 E4 F1 G1 I4 J4
# Score 7 for path: ['S', 'W', 'W', 'W', 'S', 'E', 'E', 'S', 'E', 'S', 'W', 'W', 'W', 'S', 'S', 'E']
# D4 E1 E4 F1 G1 I4 J4
# Score 6 for path: ['E', 'S', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'W', 'N', 'E', 'N', 'W', 'N', 'E']
# D2 D4 D7 E7 F5 H7
# Score 6 for path: ['E', 'S', 'W', 'W', 'W', 'S', 'S', 'E', 'E', 'S', 'W', 'W', 'W', 'S', 'S', 'E']
# D2 D4 E4 F1 F4 I2
# Score 6 for path: ['E', 'S', 'W', 'W', 'W', 'S', 'E', 'S', 'E', 'E', 'S', 'W', 'W', 'W', 'S', 'S']
# C2 D4 E1 E4 F1 I4
# Score 6 for path: ['E', 'E', 'S', 'S', 'S', 'W', 'W', 'W', 'W', 'W', 'N', 'E', 'N', 'W', 'N', 'E']
# D2 D4 D5 D7 F5 H7
# Score 6 for path: ['W', 'S', 'E', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'W', 'N', 'N', 'N', 'E', 'E']
# E2 E7 F2 F7 G5 H5
# Score 7 for path: ['W', 'S', 'W', 'W', 'S', 'S', 'E', 'E', 'S', 'W', 'W', 'W', 'S', 'S', 'E', 'E']
# E2 E4 F4 G1 G4 H1 J2
# Score 6 for path: ['W', 'S', 'W', 'W', 'S', 'E', 'S', 'E', 'S', 'W', 'W', 'W', 'S', 'S', 'E', 'E']
# E4 F1 F4 G1 H1 J4
# Score 6 for path: ['W', 'S', 'W', 'W', 'S', 'E', 'S', 'E', 'E', 'S', 'W', 'W', 'W', 'S', 'S', 'E']
# D2 E4 F1 F4 G1 J4
# Score 6 for path: ['N', 'N', 'N', 'E', 'S', 'E', 'S', 'S', 'E', 'E', 'S', 'S', 'S', 'W', 'W', 'W']
# A7 B4 B5 D5 E5 F7
# Score 6 for path: ['S', 'S', 'S', 'E', 'E', 'N', 'N', 'N', 'E', 'N', 'N', 'W', 'W', 'W', 'N', 'E']
# A5 A7 B4 B5 D5 F5
# Score 6 for path: ['S', 'S', 'E', 'S', 'E', 'N', 'N', 'N', 'E', 'N', 'N', 'W', 'W', 'W', 'N', 'E']
# A5 A7 B4 B5 D5 D6
# Score 6 for path: ['S', 'S', 'E', 'S', 'E', 'N', 'N', 'N', 'E', 'N', 'W', 'W', 'W', 'N', 'N', 'E']
# A6 A7 B4 D5 D6 G4
# Score 6 for path: ['N', 'E', 'N', 'W', 'W', 'W', 'N', 'E', 'N', 'N', 'N', 'E', 'E', 'S', 'S', 'S']
# C8 C9 E9 E10 F7 H7
# Score 6 for path: ['W', 'W', 'W', 'N', 'N', 'E', 'E', 'N', 'E', 'N', 'N', 'N', 'E', 'S', 'S', 'S']
# D8 E7 E8 F7 I8 I10
# Score 6 for path: ['N', 'N', 'N', 'E', 'N', 'N', 'N', 'E', 'E', 'S', 'S', 'S', 'S', 'S', 'S', 'E']
# A8 C8 C9 C10 F7 F9
# Score 7 for path: ['N', 'N', 'N', 'E', 'N', 'N', 'N', 'E', 'E', 'S', 'S', 'S', 'S', 'S', 'E', 'S']
# A8 A9 C9 C10 D7 F7 F9
# Score 6 for path: ['N', 'N', 'N', 'E', 'N', 'N', 'N', 'E', 'E', 'S', 'S', 'S', 'S', 'E', 'S', 'S']
# A9 C10 D7 D8 F7 F9
# Score 6 for path: ['N', 'N', 'N', 'E', 'S', 'E', 'S', 'S', 'E', 'N', 'N', 'N', 'N', 'N', 'E', 'N']
# A7 A8 C9 C10 F7 F8
# Score 6 for path: ['N', 'N', 'N', 'E', 'S', 'E', 'S', 'S', 'E', 'N', 'N', 'N', 'N', 'E', 'N', 'N']
# A7 A8 C9 C10 F7 F8
# Score 6 for path: ['N', 'N', 'E', 'N', 'N', 'N', 'N', 'E', 'E', 'S', 'S', 'S', 'S', 'S', 'E', 'S']
# A8 A9 C9 C10 D7 F7
# Score 6 for path: ['S', 'E', 'S', 'S', 'S', 'S', 'S', 'E', 'E', 'N', 'N', 'N', 'E', 'N', 'N', 'N']
# A1 A2 B4 C1 C2 E2

# checkExhaustivePathsWithAutoRepairPatterns(20, 4)
# Score 4 for path: ['S', 'S', 'S', 'E', 'S', 'E', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'N', 'W', 'W', 'N', 'N', 'E', 'E']
# D4 E2 F2 G2
# Score 4 for path: ['S', 'S', 'S', 'E', 'S', 'E', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'W', 'N', 'W', 'N', 'N', 'E', 'E']
# D4 E2 F2 G2
# Score 4 for path: ['S', 'S', 'S', 'E', 'S', 'E', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'W', 'W', 'N', 'N', 'N', 'E', 'E']
# D4 E2 F2 G2
# Score 4 for path: ['S', 'S', 'S', 'E', 'E', 'S', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'N', 'W', 'W', 'N', 'N', 'E', 'E']
# D4 E2 F2 G2
# Score 4 for path: ['S', 'S', 'S', 'E', 'E', 'S', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'W', 'N', 'W', 'N', 'N', 'E', 'E']
# D4 E2 F2 G2
# Score 4 for path: ['S', 'S', 'S', 'E', 'E', 'S', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'W', 'W', 'N', 'N', 'N', 'E', 'E']
# D4 E2 F2 G2
# Score 4 for path: ['S', 'E', 'S', 'S', 'E', 'E', 'S', 'S', 'S', 'W', 'W', 'W', 'W', 'W', 'N', 'E', 'N', 'W', 'N', 'E']
# C1 C2 E2 G4
# Score 4 for path: ['E', 'N', 'W', 'N', 'E', 'N', 'W', 'W', 'W', 'W', 'W', 'S', 'S', 'S', 'E', 'E', 'S', 'S', 'E', 'S']
# E5 F5 F6 I4
# Score 4 for path: ['S', 'E', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'N', 'W', 'N', 'W', 'N', 'E', 'E', 'N', 'N', 'E', 'N']
# E7 F5 G5 H7
# Score 4 for path: ['S', 'E', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'N', 'W', 'N', 'W', 'N', 'E', 'E', 'N', 'E', 'N', 'N']
# E7 F5 G5 H7
# Score 4 for path: ['S', 'E', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'N', 'W', 'W', 'N', 'N', 'E', 'E', 'N', 'N', 'E', 'N']
# E7 F5 G5 H5
# Score 4 for path: ['S', 'E', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'N', 'W', 'W', 'N', 'N', 'E', 'E', 'N', 'E', 'N', 'N']
# E7 F5 G5 H5
# Score 4 for path: ['S', 'E', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'N', 'W', 'W', 'N', 'N', 'E', 'E', 'E', 'N', 'N', 'N']
# E7 F5 G5 H5
# Score 4 for path: ['S', 'E', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'W', 'N', 'N', 'W', 'N', 'E', 'E', 'N', 'N', 'E', 'N']
# E7 F5 G5 H7
# Score 4 for path: ['S', 'E', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'W', 'N', 'N', 'W', 'N', 'E', 'E', 'N', 'E', 'N', 'N']
# E7 F5 G5 H7
# Score 4 for path: ['S', 'E', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'W', 'N', 'E', 'N', 'W', 'N', 'E', 'N', 'N', 'E', 'N']
# D4 E7 F5 H7
# Score 4 for path: ['S', 'E', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'W', 'N', 'E', 'N', 'W', 'N', 'E', 'N', 'E', 'N', 'N']
# D4 E7 F5 H7
# Score 4 for path: ['S', 'E', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'W', 'N', 'W', 'N', 'N', 'E', 'E', 'N', 'N', 'E', 'N']
# E7 F5 G5 H5
# Score 4 for path: ['S', 'E', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'W', 'N', 'W', 'N', 'N', 'E', 'E', 'N', 'E', 'N', 'N']
# E7 F5 G5 H5
# Score 4 for path: ['S', 'E', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'W', 'N', 'W', 'N', 'N', 'E', 'E', 'E', 'N', 'N', 'N']
# E7 F5 G5 H5
# Score 4 for path: ['S', 'E', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'W', 'W', 'N', 'N', 'N', 'E', 'E', 'N', 'N', 'E', 'N']
# E7 F5 G5 H5
# Score 4 for path: ['S', 'E', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'W', 'W', 'N', 'N', 'N', 'E', 'E', 'N', 'E', 'N', 'N']
# E7 F5 G5 H5
# Score 4 for path: ['S', 'E', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'W', 'W', 'N', 'N', 'N', 'E', 'E', 'E', 'N', 'N', 'N']
# E7 F5 G5 H5
# Score 4 for path: ['E', 'S', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'N', 'W', 'N', 'W', 'N', 'E', 'E', 'N', 'N', 'E', 'N']
# E7 F5 G5 H7
# Score 4 for path: ['E', 'S', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'N', 'W', 'N', 'W', 'N', 'E', 'E', 'N', 'E', 'N', 'N']
# E7 F5 G5 H7
# Score 4 for path: ['E', 'S', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'N', 'W', 'W', 'N', 'N', 'E', 'E', 'N', 'N', 'E', 'N']
# E7 F5 G5 H5
# Score 4 for path: ['E', 'S', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'N', 'W', 'W', 'N', 'N', 'E', 'E', 'N', 'E', 'N', 'N']
# E7 F5 G5 H5
# Score 4 for path: ['E', 'S', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'N', 'W', 'W', 'N', 'N', 'E', 'E', 'E', 'N', 'N', 'N']
# E7 F5 G5 H5
# Score 4 for path: ['E', 'S', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'W', 'N', 'N', 'W', 'N', 'E', 'E', 'N', 'N', 'E', 'N']
# E7 F5 G5 H7
# Score 4 for path: ['E', 'S', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'W', 'N', 'N', 'W', 'N', 'E', 'E', 'N', 'E', 'N', 'N']
# E7 F5 G5 H7
# Score 4 for path: ['E', 'S', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'W', 'N', 'E', 'N', 'W', 'N', 'E', 'N', 'N', 'E', 'N']
# D4 E7 F5 H7
# Score 4 for path: ['E', 'S', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'W', 'N', 'E', 'N', 'W', 'N', 'E', 'N', 'E', 'N', 'N']
# D4 E7 F5 H7
# Score 4 for path: ['E', 'S', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'W', 'N', 'W', 'N', 'N', 'E', 'E', 'N', 'N', 'E', 'N']
# E7 F5 G5 H5
# Score 4 for path: ['E', 'S', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'W', 'N', 'W', 'N', 'N', 'E', 'E', 'N', 'E', 'N', 'N']
# E7 F5 G5 H5
# Score 4 for path: ['E', 'S', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'W', 'N', 'W', 'N', 'N', 'E', 'E', 'E', 'N', 'N', 'N']
# E7 F5 G5 H5
# Score 4 for path: ['E', 'S', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'W', 'W', 'N', 'N', 'N', 'E', 'E', 'N', 'N', 'E', 'N']
# E7 F5 G5 H5
# Score 4 for path: ['E', 'S', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'W', 'W', 'N', 'N', 'N', 'E', 'E', 'N', 'E', 'N', 'N']
# E7 F5 G5 H5
# Score 4 for path: ['E', 'S', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'W', 'W', 'N', 'N', 'N', 'E', 'E', 'E', 'N', 'N', 'N']
# E7 F5 G5 H5
# Score 4 for path: ['E', 'E', 'S', 'S', 'S', 'W', 'W', 'W', 'W', 'W', 'N', 'E', 'N', 'W', 'N', 'E', 'N', 'N', 'N', 'E']
# D4 D5 F5 H7
# Score 4 for path: ['E', 'E', 'S', 'S', 'S', 'W', 'W', 'W', 'W', 'W', 'N', 'E', 'N', 'W', 'N', 'E', 'N', 'N', 'E', 'N']
# D4 D5 F5 H7
# Score 4 for path: ['W', 'S', 'E', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'N', 'W', 'N', 'N', 'E', 'E', 'N', 'N', 'E', 'N']
# E7 F7 G5 H5
# Score 4 for path: ['W', 'S', 'E', 'E', 'S', 'S', 'W', 'W', 'W', 'W', 'W', 'N', 'N', 'N', 'E', 'E', 'N', 'N', 'E', 'N']
# E7 F7 G5 H5
# Score 4 for path: ['N', 'N', 'N', 'E', 'N', 'N', 'N', 'E', 'S', 'S', 'E', 'S', 'S', 'E', 'E', 'S', 'S', 'W', 'W', 'W']
# A7 C8 D8 E10
# Score 4 for path: ['N', 'N', 'N', 'E', 'N', 'N', 'N', 'E', 'S', 'S', 'E', 'S', 'E', 'S', 'E', 'S', 'S', 'W', 'W', 'W']
# A7 C8 D8 E10
# Score 4 for path: ['N', 'N', 'N', 'E', 'N', 'N', 'N', 'E', 'S', 'S', 'E', 'S', 'E', 'E', 'S', 'S', 'S', 'W', 'W', 'W']
# A7 C8 D8 E10
# Score 4 for path: ['N', 'N', 'N', 'E', 'N', 'N', 'N', 'E', 'S', 'E', 'S', 'S', 'S', 'E', 'E', 'S', 'S', 'W', 'W', 'W']
# A7 C8 D8 E10
# Score 4 for path: ['N', 'N', 'N', 'E', 'N', 'N', 'N', 'E', 'S', 'E', 'S', 'S', 'E', 'S', 'E', 'S', 'S', 'W', 'W', 'W']
# A7 C8 D8 E10
# Score 5 for path: ['N', 'N', 'N', 'E', 'N', 'N', 'N', 'E', 'S', 'E', 'S', 'S', 'E', 'E', 'S', 'S', 'S', 'W', 'W', 'W']
# A7 A8 C8 D8 E10
# Score 4 for path: ['N', 'N', 'N', 'E', 'N', 'N', 'N', 'E', 'S', 'E', 'S', 'S', 'E', 'E', 'S', 'S', 'W', 'S', 'W', 'W']
# A8 C9 D8 E10
# Score 4 for path: ['N', 'N', 'N', 'E', 'N', 'N', 'N', 'E', 'E', 'S', 'S', 'S', 'S', 'W', 'S', 'E', 'E', 'S', 'W', 'W']
# A8 C9 C10 F7
# Score 4 for path: ['N', 'N', 'N', 'E', 'S', 'S', 'E', 'S', 'E', 'N', 'N', 'N', 'N', 'E', 'N', 'W', 'W', 'W', 'N', 'E']
# A7 A8 C8 C9
# Score 4 for path: ['N', 'N', 'N', 'E', 'S', 'S', 'E', 'S', 'E', 'N', 'N', 'N', 'E', 'N', 'N', 'W', 'W', 'W', 'N', 'E']
# A7 A8 C8 C9
# Score 4 for path: ['N', 'N', 'N', 'E', 'S', 'S', 'E', 'S', 'E', 'N', 'N', 'N', 'E', 'N', 'W', 'N', 'E', 'N', 'W', 'W']
# A8 C8 C9 F7
# Score 4 for path: ['N', 'N', 'N', 'E', 'S', 'S', 'E', 'S', 'E', 'N', 'N', 'N', 'E', 'N', 'W', 'N', 'W', 'W', 'N', 'E']
# A7 A8 C8 C9
# Score 4 for path: ['N', 'N', 'N', 'E', 'S', 'S', 'E', 'S', 'E', 'N', 'N', 'N', 'E', 'N', 'W', 'W', 'W', 'N', 'N', 'E']
# A7 C8 C9 F7
# Score 4 for path: ['N', 'N', 'N', 'E', 'S', 'E', 'S', 'S', 'E', 'N', 'N', 'N', 'N', 'E', 'N', 'W', 'W', 'W', 'N', 'E']
# A7 A8 C9 C10
# Score 4 for path: ['N', 'N', 'E', 'N', 'N', 'N', 'N', 'E', 'S', 'E', 'S', 'S', 'E', 'E', 'S', 'S', 'S', 'W', 'W', 'W']
# A7 A8 C8 E10
# Score 4 for path: ['N', 'N', 'E', 'N', 'N', 'N', 'N', 'E', 'E', 'S', 'S', 'S', 'S', 'W', 'S', 'E', 'E', 'S', 'W', 'W']
# A8 C9 C10 F7
# Score 4 for path: ['N', 'E', 'N', 'N', 'N', 'N', 'N', 'E', 'S', 'E', 'S', 'S', 'E', 'E', 'S', 'S', 'S', 'W', 'W', 'W']
# A7 A8 C8 E10
# Score 4 for path: ['E', 'N', 'N', 'N', 'N', 'N', 'N', 'E', 'S', 'E', 'S', 'S', 'E', 'E', 'S', 'S', 'S', 'W', 'W', 'W']
# A7 A8 C8 E10
# Score 4 for path: ['S', 'S', 'S', 'E', 'S', 'S', 'S', 'E', 'E', 'N', 'N', 'N', 'E', 'N', 'E', 'N', 'W', 'W', 'W', 'N']
# A1 A2 B4 E2
# Score 4 for path: ['S', 'S', 'E', 'S', 'S', 'S', 'S', 'E', 'E', 'N', 'N', 'N', 'E', 'N', 'E', 'N', 'W', 'W', 'W', 'N']
# A1 A2 B4 E2
# Score 4 for path: ['S', 'E', 'S', 'S', 'S', 'S', 'S', 'E', 'E', 'N', 'N', 'N', 'E', 'N', 'E', 'N', 'W', 'W', 'W', 'N']
# A1 A2 B4 E2
# Score 4 for path: ['E', 'S', 'S', 'S', 'S', 'S', 'E', 'S', 'E', 'N', 'N', 'N', 'E', 'N', 'W', 'N', 'E', 'N', 'W', 'W']
# A2 C2 C3 F1
# Score 4 for path: ['E', 'N', 'W', 'W', 'N', 'W', 'N', 'E', 'N', 'N', 'N', 'E', 'S', 'E', 'S', 'S', 'E', 'N', 'N', 'N']
# C7 C8 E8 E9
# Score 4 for path: ['E', 'N', 'W', 'W', 'N', 'W', 'N', 'E', 'N', 'N', 'N', 'E', 'E', 'S', 'S', 'S', 'E', 'N', 'N', 'N']
# C8 E8 E9 H7
# Score 4 for path: ['E', 'N', 'W', 'W', 'W', 'N', 'N', 'E', 'N', 'N', 'N', 'E', 'S', 'E', 'S', 'S', 'E', 'N', 'N', 'N']
# C7 C8 E8 E9
# Score 4 for path: ['E', 'N', 'W', 'W', 'W', 'N', 'N', 'E', 'N', 'N', 'N', 'E', 'E', 'S', 'S', 'S', 'E', 'N', 'N', 'N']
# C8 E8 E9 H7
# Score 4 for path: ['E', 'N', 'W', 'W', 'W', 'N', 'E', 'N', 'N', 'N', 'N', 'E', 'S', 'E', 'S', 'S', 'E', 'N', 'N', 'N']
# C7 C8 E8 E9
# Score 4 for path: ['E', 'N', 'W', 'W', 'W', 'N', 'E', 'N', 'N', 'N', 'N', 'E', 'E', 'S', 'S', 'S', 'E', 'N', 'N', 'N']
# C8 E8 E9 H7
# Score 4 for path: ['W', 'W', 'N', 'N', 'E', 'E', 'N', 'W', 'N', 'N', 'N', 'E', 'E', 'S', 'S', 'S', 'S', 'S', 'E', 'S']
# C8 C9 E10 F7
# Score 4 for path: ['W', 'W', 'N', 'E', 'N', 'W', 'N', 'E', 'N', 'N', 'N', 'E', 'S', 'E', 'S', 'S', 'E', 'N', 'N', 'N']
# C7 C8 E8 G10
# Score 4 for path: ['E', 'S', 'W', 'W', 'S', 'E', 'S', 'W', 'S', 'S', 'S', 'E', 'E', 'N', 'N', 'N', 'E', 'N', 'N', 'N']
# B2 D4 E1 E2
# Score 4 for path: ['W', 'S', 'E', 'E', 'S', 'W', 'W', 'S', 'S', 'S', 'E', 'S', 'E', 'N', 'N', 'N', 'E', 'N', 'N', 'N']
# B4 C1 E2 E3
# Score 4 for path: ['N', 'N', 'N', 'E', 'S', 'S', 'S', 'E', 'N', 'N', 'N', 'E', 'N', 'N', 'N', 'E', 'S', 'E', 'S', 'S']
# A8 A9 A10 B8
# Score 4 for path: ['N', 'N', 'N', 'E', 'S', 'S', 'S', 'E', 'N', 'N', 'N', 'E', 'N', 'N', 'N', 'E', 'E', 'S', 'S', 'S']
# A8 A9 A10 B8
# Score 4 for path: ['N', 'N', 'N', 'E', 'S', 'S', 'S', 'E', 'N', 'N', 'N', 'E', 'N', 'N', 'E', 'N', 'E', 'S', 'S', 'S']
# A8 A9 A10 B8
# Score 5 for path: ['N', 'N', 'N', 'E', 'S', 'S', 'S', 'E', 'N', 'N', 'E', 'N', 'N', 'N', 'E', 'N', 'E', 'S', 'S', 'S']
# A7 A8 A9 A10 E10
# Score 4 for path: ['N', 'N', 'N', 'E', 'S', 'S', 'S', 'E', 'N', 'N', 'E', 'N', 'N', 'E', 'N', 'N', 'E', 'S', 'S', 'S']
# A7 A8 A9 E10
# Score 4 for path: ['N', 'N', 'N', 'E', 'S', 'E', 'S', 'S', 'S', 'S', 'S', 'E', 'E', 'N', 'N', 'N', 'E', 'N', 'N', 'N']
# A7 B4 B5 D5
# Score 4 for path: ['S', 'S', 'S', 'E', 'S', 'S', 'S', 'E', 'N', 'N', 'N', 'E', 'N', 'N', 'N', 'E', 'S', 'E', 'S', 'S']
# A2 A3 A4 B2
# Score 4 for path: ['S', 'S', 'S', 'E', 'S', 'S', 'S', 'E', 'N', 'N', 'N', 'E', 'N', 'N', 'N', 'E', 'E', 'S', 'S', 'S']
# A2 A3 A4 B2
# Score 4 for path: ['S', 'S', 'S', 'E', 'S', 'S', 'S', 'E', 'N', 'N', 'N', 'E', 'N', 'N', 'E', 'N', 'E', 'S', 'S', 'S']
# A2 A3 A4 B2
# Score 4 for path: ['S', 'S', 'S', 'E', 'S', 'S', 'S', 'E', 'N', 'N', 'E', 'N', 'N', 'N', 'E', 'N', 'E', 'S', 'S', 'S']
# A1 A2 A3 A4
# Score 4 for path: ['S', 'S', 'E', 'S', 'S', 'S', 'S', 'E', 'N', 'N', 'E', 'N', 'N', 'N', 'E', 'N', 'E', 'S', 'S', 'S']
# A1 A2 A3 A4
# Score 4 for path: ['S', 'S', 'E', 'S', 'S', 'S', 'S', 'E', 'N', 'E', 'N', 'N', 'N', 'E', 'N', 'N', 'E', 'S', 'S', 'S']
# A1 A2 A3 E3
# Score 5 for path: ['S', 'E', 'S', 'S', 'S', 'S', 'S', 'E', 'N', 'N', 'E', 'N', 'N', 'N', 'E', 'N', 'E', 'S', 'S', 'S']
# A1 A2 A3 A4 E4
# Score 4 for path: ['S', 'E', 'S', 'S', 'S', 'S', 'S', 'E', 'N', 'N', 'E', 'N', 'N', 'E', 'N', 'N', 'E', 'S', 'S', 'S']
# A1 A2 A3 E4
# Score 4 for path: ['S', 'E', 'S', 'S', 'S', 'S', 'S', 'E', 'N', 'E', 'N', 'N', 'N', 'E', 'N', 'N', 'E', 'S', 'S', 'S']
# A1 A2 A3 E3
# Score 5 for path: ['E', 'S', 'S', 'S', 'S', 'S', 'S', 'E', 'N', 'N', 'E', 'N', 'N', 'N', 'E', 'N', 'E', 'S', 'S', 'S']
# A1 A2 A3 A4 E4
# Score 4 for path: ['E', 'S', 'S', 'S', 'S', 'S', 'S', 'E', 'N', 'N', 'E', 'N', 'N', 'E', 'N', 'N', 'E', 'S', 'S', 'S']
# A1 A2 A3 E4
# Score 4 for path: ['E', 'S', 'S', 'S', 'S', 'S', 'S', 'E', 'N', 'E', 'N', 'N', 'N', 'E', 'N', 'N', 'E', 'S', 'S', 'S']
# A1 A2 A3 E3
