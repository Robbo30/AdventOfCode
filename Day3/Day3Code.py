##Part1

f = open("D:\\AdventOfCode\\Day3\\Day3Input.txt", "r")
lines = f.readlines()

def find_full_number(lines, y, x):
    start_index, end_index = x, x
    while start_index > 0:
        if start_index-1 < 0 or not lines[y][start_index-1].isdigit():
            break
        start_index -= 1
    while end_index < len(lines[y]):
        if end_index+1 >= len(lines[y]) or not lines[y][end_index+1].isdigit():
            break
        end_index += 1
    return int(lines[y][start_index:end_index+1])
 
def get_top_or_bottom(lines, y, x, check_top):
    if check_top: y -= 1
    else: y += 1
    if y < 0 or y > len(lines): return 0
    mid_empty = True if lines[y][x] == '.' else False
    left_num, right_num = 0, 0
    if mid_empty:
        if x-1 >= 0 and lines[y][x-1].isdigit():
            left_num = find_full_number(lines, y, x-1)
        if x+1 < len(lines[y]) and lines[y][x+1].isdigit():
            right_num = find_full_number(lines, y, x+1)
    else:
        left_num = find_full_number(lines, y, x)
    return left_num + right_num
        
def get_sum_of_neighbors(lines, y, x):
    top = get_top_or_bottom(lines, y, x, True)
    left = find_full_number(lines, y, x-1) if x-1 > 0 and lines[y][x-1].isdigit() else 0
    right = find_full_number(lines, y, x+1) if x+1 < len(lines[y]) and lines[y][x+1].isdigit() else 0
    bottom = get_top_or_bottom(lines, y, x, False)
    return top + left + right + bottom
 
lines = [line.strip('\n') for line in lines]
counter = 0
for line in range(len(lines)):
    for char in range(len(lines[line])):
        if not lines[line][char].isdigit() and lines[line][char] != '.':
            counter += get_sum_of_neighbors(lines, line, char)
print(f"Solution Part 1: {counter}")

##Part2

f = open("D:\\AdventOfCode\\Day3\\Day3Input.txt", "r")
lines = f.readlines()

def find_full_number(lines, y, x):
    start_index, end_index = x, x
    while start_index > 0:
        if start_index-1 < 0 or not lines[y][start_index-1].isdigit():
            break
        start_index -= 1
    while end_index < len(lines[y]):
        if end_index+1 >= len(lines[y]) or not lines[y][end_index+1].isdigit():
            break
        end_index += 1
    return int(lines[y][start_index:end_index+1])
 
def get_top_or_bottom(lines, y, x, check_top):
  
    if check_top: y -= 1
    else: y += 1
    if y < 0 or y > len(lines): return 0
    mid_empty = True if lines[y][x] == '.' else False
    left_num, right_num = 0, 0
    if mid_empty:
        if x-1 >= 0 and lines[y][x-1].isdigit():
            left_num = find_full_number(lines, y, x-1)
        if x+1 < len(lines[y]) and lines[y][x+1].isdigit():
            right_num = find_full_number(lines, y, x+1)
    else:
        left_num = find_full_number(lines, y, x)
    return (left_num + right_num, left_num, right_num)
        
def get_gear_ratio(lines, y, x):
    top = get_top_or_bottom(lines, y, x, True)
    left = find_full_number(lines, y, x-1) if x-1 > 0 and lines[y][x-1].isdigit() else 0
    right = find_full_number(lines, y, x+1) if x+1 < len(lines[y]) and lines[y][x+1].isdigit() else 0
    bottom = get_top_or_bottom(lines, y, x, False)
    nums = [top[1], top[2], left, right, bottom[1], bottom[2]]
    product = 1
    if nums.count(0) == len(nums) - 2:
        for i in nums:
            if i: product *= i
        return product
    return 0
 
lines = [line.strip('\n') for line in lines]
counter = 0
for line in range(len(lines)):
    for char in range(len(lines[line])):
        if not lines[line][char].isdigit() and lines[line][char] != '.':
            counter += get_gear_ratio(lines, line, char)
print(f"Solution Part 2: {counter}")
