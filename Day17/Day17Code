direction_to_delta = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}
turns = {"^": "^<>", "v": "v<>", "<": "<^v", ">": ">^v"}


def dirFunction_1(steps, direction):
    dirs = turns[direction]
    if steps < 3:
        pass
    else:
        dirs = dirs[1:]
    return dirs


def dirFunction_2(steps, direction):
    dirs = turns[direction]
    if steps < 4:
        dirs = [direction]
    elif steps < 10:
        pass
    else:
        dirs = dirs[1:]
    return dirs


def calcHeatLoss(dir_function, heat_losses, grid):
    to_check = list(heat_losses.keys())
    while to_check:
        new_to_check = []
        for direction, steps, x, y in to_check:
            possible_directions = dir_function(steps, direction)

            for possible_direction in possible_directions:
                delta = direction_to_delta[possible_direction]
                next_x = x + delta[0]
                next_y = y + delta[1]
                if (next_x, next_y) not in grid:
                    continue
                next_steps = steps + 1 if possible_direction == direction else 1
                next_key = (possible_direction, next_steps, next_x, next_y)
                next_heat_loss = heat_losses[(direction, steps, x, y)] + grid[(next_x, next_y)]
                if next_key not in heat_losses or heat_losses[next_key] > next_heat_loss:
                    heat_losses[next_key] = next_heat_loss
                    new_to_check.append((possible_direction, next_steps, next_x, next_y))
        to_check = new_to_check


def parse(lines):
    lines = lines.splitlines()
    grid = {}
    heat_losses = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            grid[(x, y)] = int(c)
    end_pos = (x, y)
    heat_losses[(">", 10, 0, 0)] = 0
    heat_losses[("v", 10, 0, 0)] = 0
    return end_pos, grid, heat_losses


def part1(lines):
    end_pos, grid, heat_losses = parse(lines)
    calcHeatLoss(dirFunction_1, heat_losses, grid)
    return min((value for (_, steps, x, y), value in heat_losses.items() if end_pos == (x, y)))


def part2(lines):
    end_pos, grid, heat_losses = parse(lines)
    calcHeatLoss(dirFunction_2, heat_losses, grid)
    return min((value for (_, steps, x, y), value in heat_losses.items() if end_pos == (x, y) and steps >= 4))


if __name__ == "__main__":
    lines = open("D:\\AdventOfCode\\Day17\\Day17Input.txt", "r").read()
    print("Part 1 Solution:", part1(lines))
    print("Part 2 Solution:", part2(lines))