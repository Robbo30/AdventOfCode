#Part 1
txt = open("D:\\AdventOfCode\\Day18\\Day18Input.txt", "r")

dirs = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}

digplan = []
for line in txt.readlines():
    line = line.strip().split(" ")
    dir = dirs[line[0]]
    meters = int(line[1])
    digplan.append((dir, meters))

def tupleAdd(t1, t2, multiply):
    return (t1[0] + t2[0] * multiply, t1[1] + t2[1] * multiply)

coordinates = [(0, 0)]
prevPos = (0, 0)
borderLength = 1
for (dir, meters) in digplan:
    nextPos = tupleAdd(prevPos, dir, meters)
    borderLength += meters
    coordinates.append(nextPos)
    prevPos = nextPos

area = 0
for i in range(1, len(coordinates)):
    x1, y1 = coordinates[i - 1]
    x2, y2 = coordinates[i]
    area += (y1 + y2) * (x1 - x2)

area = (abs(area) + borderLength + 1) / 2
print("Part 1 Solution: ",area)

#Part 2

txt = open("D:\\AdventOfCode\\Day18\\Day18Input.txt", "r")

dirs = {'0': (0, 1), '1': (1, 0), '2': (0, -1), '3': (-1, 0)}

digplan = []
for line in txt.readlines():
    hex = line.strip().split(" ")[2][2:-1]
    meters = int(hex[:5], 16)
    dir = dirs[hex[5]]
    digplan.append((dir, meters))

def tupleAdd(t1, t2, multiply):
    return (t1[0] + t2[0] * multiply, t1[1] + t2[1] * multiply)

coordinates = [(0, 0)]
prevPos = (0, 0)
borderLength = 1
for (dir, meters) in digplan:
    nextPos = tupleAdd(prevPos, dir, meters)
    borderLength += meters
    coordinates.append(nextPos)
    prevPos = nextPos

area = 0
for i in range(1, len(coordinates)):
    x1, y1 = coordinates[i - 1]
    x2, y2 = coordinates[i]
    area += (y1 + y2) * (x1 - x2)

area = (abs(area) + borderLength + 1) / 2
print("Part 2 Solution: ",area)