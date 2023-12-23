InputList = []
with open("D:\\AdventOfCode\\Day13\\Day13Input.txt", "r") as data:
    for t in data:
        Line = t.strip()
        InputList.append(Line)

PatternList = []
NewPattern = []
for i in InputList:
    if i == "":
        NewPattern = tuple(NewPattern)
        PatternList.append(NewPattern)
        NewPattern = []
    else:
        NewPattern.append(i)
PatternList.append(tuple(NewPattern))

def FindLine(Pattern, Skip):
    for v in range(len(Pattern)-1):
        Line = True
        Height = min(v+1, len(Pattern)-1-v)
        for y in range(Height):
            if Pattern[v-y] != Pattern[v+1+y]:
                Line = False
                break
        if Line:
            PotentialAnswer = (v+1)*100
            if PotentialAnswer != Skip:
                return PotentialAnswer

    for v in range(len(Pattern[0])-1):
        Line = True
        Width = min(v+1, len(Pattern[0])-1-v)
        for x in range(Width):
            for y in range(len(Pattern)):
                if Pattern[y][v-x] != Pattern[y][v+1+x]:
                    Line = False
                    break
            if not(Line):
                break
        if Line:
            PotentialAnswer = v+1
            if PotentialAnswer != Skip:
                return PotentialAnswer
    return 0

Part1Solution = 0
AnswerList = []
for Pattern in PatternList:
    Rea = FindLine(Pattern, 0)
    AnswerList.append(Rea)
    Part1Solution += Rea

Part2Solution = 0
for n, Pattern in enumerate(PatternList):
    Skip = AnswerList[n]
    Width = len(Pattern[0])
    Height = len(Pattern)
    for y in range(Height):
        MoveOn = False
        for x in range(Width):
            NewPattern = list(Pattern)
            NewPattern[y] = list(NewPattern[y])
            if NewPattern[y][x] == ".":
                NewPattern[y][x] = "#"
            else:
                NewPattern[y][x] = "."
            NewPattern[y] = "".join(NewPattern[y])
            NewPattern = tuple(NewPattern)
            Rea = FindLine(NewPattern, Skip)
            if Rea != 0 and Rea != AnswerList[n]:
                Part2Solution += Rea
                MoveOn = True
                break
        if MoveOn:
            break

print(f"{Part1Solution = }")
print(f"{Part2Solution = }")