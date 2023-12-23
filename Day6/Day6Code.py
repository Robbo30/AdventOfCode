##Part1
import os
import re

def detectWins(time, dist):
    count = 1
    wins = 0
    while int(time) - count != 0:
        if (count * (int(time) - count)) > int(dist):
            wins += 1
        count += 1
    return wins

try:
    with open("D:\\AdventOfCode\\Day6\\Day6Input.txt", "r") as fileData:
        lines = fileData.readlines()
except IOError:
    print("Error: input not found")

time = list(filter(None, lines[0].strip().split(":")[1].split(" ")))
distance = list(filter(None, lines[1].strip().split(":")[1].split(" ")))

loop = len(time) - 1
winProduct = 1

while (loop >= 0):
    winProduct *= detectWins(int(time[loop]), int(distance[loop]))
    loop -= 1

print ("Part1", winProduct)

##Part2

time = int(lines[0].strip().split(":")[1].replace(" ", ""))
distance = int(lines[1].strip().split(":")[1].replace(" ", ""))

winSum = detectWins(time, distance)

print("Part2", winSum)