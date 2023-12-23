from itertools import combinations

with open("D:\\AdventOfCode\\Day11\\Day11Input.txt") as f:
    read_data = f.read().strip().split('\n')

def map_universe(grid):
    empty_row = set()
    empty_col = set()
    stars = set()
    for i, j in enumerate(grid):
        if len(set(j)) == 1:
            empty_row.add(i)
        for k, l in enumerate(grid[i]):
            if l == '#':
                stars.add((i, k))
    for k in range(len(grid[0])):
        if len(set([j[k] for j in grid])) == 1:
            empty_col.add(k)
    return empty_row, empty_col, stars

e_row, e_col, stars = map_universe(read_data)
star_combs = set(combinations(stars, 2))

def cal_shortest_path(comb, expand_level):
    i, j = comb[0]
    k, l = comb[1]
    x, y = abs(i - k), abs(j - l)
    # Add expansions
    for r in e_row:
        if r in range(*sorted((i, k))):
            x += expand_level
    for c in e_col:
        if c in range(*sorted((j, l))):
            y += expand_level
    return x + y

print('Part 1:', sum(cal_shortest_path(s, 1) for s in star_combs))
print('Part 2:', sum(cal_shortest_path(s, 1000000 - 1) for s in star_combs))