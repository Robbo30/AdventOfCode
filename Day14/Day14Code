import copy

InputList = []
with open("D:\\AdventOfCode\\Day14\\Day14Input.txt", "r") as data:
    for t in data:
        Line = t.strip()
        InputList.append(Line)

CubeRockSet = set()
RoundRockList = []
for y, i in enumerate(InputList):
    for x, c in enumerate(i):
        if c == "#":
            CubeRockSet.add((x,y))
        elif c == "O":
            RoundRockList.append((x,y))

Height = len(InputList)
Width = len(InputList[0])
RoundRockList.sort()
SolidSet = CubeRockSet.copy()
Part1Answer = 0
for RX, RY in RoundRockList:
    X, Y = RX, RY
    while True:
        NY = Y - 1
        if NY < 0 or (X, NY) in SolidSet:
            SolidSet.add((X,Y))
            Part1Answer += Height - Y
            break
        Y = NY

DirectionDict = {"N": (0,-1), "W":(-1,0), "S":(0,1), "E":(1,0)}
ScoreSets = set()
ExactScoreDict = {}
Count = 0
Jump = True
while Count < 1000000000:
    for d in ["N","W","S","E"]:
        NewRockList = []
        RoundRockList.sort()
        if d == "S" or d == "E":
            RoundRockList.reverse()
        SolidSet = CubeRockSet.copy()
        DX, DY = DirectionDict[d]
        for RX, RY in RoundRockList:
            X, Y = RX, RY
            while True:
                NX, NY = X+DX, Y+DY
                if NX < 0 or NX >= Width or NY < 0 or NY >= Height or (NX,NY) in SolidSet:
                    SolidSet.add((X,Y))
                    NewRockList.append((X,Y))
                    break
                X, Y = NX, NY
        RoundRockList = copy.deepcopy((NewRockList))
    if Count > 1000 and Jump:
        ScoreY = 0
        ScoreX = 0
        for X, Y in RoundRockList:
            ScoreY += Height - Y
            ScoreX += Width - X
        Score = (ScoreX, ScoreY)
        if Score in ScoreSets:
            if Score in ExactScoreDict.keys():
                LastCount, Diff = ExactScoreDict[Score]
                NewDiff = Count - LastCount
                ExactScoreDict[Score] = (Count, NewDiff)
                if Count >= 1500:
                    Jump = False
                    Longdifference = 1000000000 - Count
                    CycleJump = Longdifference // NewDiff
                    Count += CycleJump * NewDiff
            else:
                ExactScoreDict[Score] = (Count, Count)
        ScoreSets.add(Score)
    Count += 1
    if Count % 50 == 25:
        print(Count)

Part2Answer = 0
for X, Y in RoundRockList:
    Part2Answer += Height - Y

print(f"{Part1Answer = }")
print(f"{Part2Answer = }")