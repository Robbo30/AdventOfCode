##Part 1

with open("D:\\AdventOfCode\\Day16\\Day16Input.txt", "r") as file:
    grid = [list(line) for line in file.read().splitlines()]

lasers = [((0, -1), "R")]
seen = set()
energized = set()

while any(lasers):
    current_tile, direction = lasers.pop(0)
    if direction == "R":
        current_tile = (current_tile[0], current_tile[1] + 1)
    if direction == "L":
        current_tile = (current_tile[0], current_tile[1] - 1)
    if direction == "U":
        current_tile = (current_tile[0] - 1, current_tile[1])
    if direction == "D":
        current_tile = (current_tile[0] + 1, current_tile[1])

    row = current_tile[0]
    col = current_tile[1]

    if 0 <= current_tile[0] < len(grid[0]) and 0 <= current_tile[1] < len(grid) and (current_tile, direction) not in seen:
        energized.add(current_tile)
        seen.add((current_tile, direction))
        if grid[row][col] == "/":
            if direction == "R":
                lasers.append((current_tile, "U"))
            elif direction == "L":
                lasers.append((current_tile, "D"))
            elif direction == "U":
                lasers.append((current_tile, "R"))
            elif direction == "D":
                lasers.append((current_tile, "L"))
            continue
        elif grid[row][col] == "\\":
            if direction == "R":
                lasers.append((current_tile, "D"))
            elif direction == "L":
                lasers.append((current_tile, "U"))
            elif direction == "U":
                lasers.append((current_tile, "L"))
            elif direction == "D":
                lasers.append((current_tile, "R"))
            continue
        elif grid[row][col] == "|":
            if direction in "RL":
                lasers.append((current_tile, "U"))
                lasers.append((current_tile, "D"))
                continue
        elif grid[row][col] == "-":
            if direction in "UD":
                lasers.append((current_tile, "L"))
                lasers.append((current_tile, "R"))
                continue

        lasers.append((current_tile, direction))

total_energized = len(energized)
print("Part 1 Solution:", total_energized)

##Part 2 

starting_lasers = [((row, -1), "R") for row in range(len(grid[0]))] + [((row, len(grid[0])), "L") for row in range(
    len(grid[0]))] + [((-1, col), "D") for col in range(len(grid))] + [((len(grid), col), "U") for col in range(len(grid))]

total_energized = []

for laser in starting_lasers:
    lasers = [laser]
    seen = set()
    energized = set()

    while any(lasers):
        current_tile, direction = lasers.pop(0)
        if direction == "R":
            current_tile = (current_tile[0], current_tile[1] + 1)
        if direction == "L":
            current_tile = (current_tile[0], current_tile[1] - 1)
        if direction == "U":
            current_tile = (current_tile[0] - 1, current_tile[1])
        if direction == "D":
            current_tile = (current_tile[0] + 1, current_tile[1])

        row = current_tile[0]
        col = current_tile[1]

        if 0 <= current_tile[0] < len(grid[0]) and 0 <= current_tile[1] < len(grid) and (current_tile, direction) not in seen:
            energized.add(current_tile)
            seen.add((current_tile, direction))
            if grid[row][col] == "/":
                if direction == "R":
                    lasers.append((current_tile, "U"))
                elif direction == "L":
                    lasers.append((current_tile, "D"))
                elif direction == "U":
                    lasers.append((current_tile, "R"))
                elif direction == "D":
                    lasers.append((current_tile, "L"))
                continue
            elif grid[row][col] == "\\":
                if direction == "R":
                    lasers.append((current_tile, "D"))
                elif direction == "L":
                    lasers.append((current_tile, "U"))
                elif direction == "U":
                    lasers.append((current_tile, "L"))
                elif direction == "D":
                    lasers.append((current_tile, "R"))
                continue
            elif grid[row][col] == "|":
                if direction in "RL":
                    lasers.append((current_tile, "U"))
                    lasers.append((current_tile, "D"))
                    continue
            elif grid[row][col] == "-":
                if direction in "UD":
                    lasers.append((current_tile, "L"))
                    lasers.append((current_tile, "R"))
                    continue

            lasers.append((current_tile, direction))

    total_energized.append(len(energized))

max_energized = max(total_energized)
print("Part 2 Solution", max_energized)