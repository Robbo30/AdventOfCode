##Part1
import sys

FILE = 'D:\\AdventOfCode\\Day5\\Day5Input.txt'

with open(FILE) as f:
    seeds = list(map(int, f.readline().split()[1:]))
    f.readline() 
    f.readline() 
    maps = []
    map_ranges = []

    for line in f:
        if line == '\n':
            maps.append(map_ranges)
            map_ranges = []
            next(f) 
        else:
            map_ranges.append(tuple(map(int, line.split())))
    if map_ranges:  
        maps.append(map_ranges)

    lowest_location = sys.maxsize
    for s in seeds:
        for map_ranges in maps:
            for destination_start, source_start, length in map_ranges:
                if source_start <= s <= source_start + length - 1:
                    s = destination_start + s - source_start
                    break

        lowest_location = min(s, lowest_location)
        
    print(f"Solution Part 2: {lowest_location}")
  

##Part2

from operator import itemgetter

def map_seed(s, m):
    destination_start, source_start, _ = m
    return destination_start + s - source_start

def map_seed_range(seed_range, map_ranges):
    seed_ranges = []
    seed_start, seed_end = seed_range[0], seed_range[1]

    for m in map_ranges:
        source_start, source_end = m[1], m[1] + m[2] - 1

        overlap_start = max(seed_start, source_start)
        overlap_end = min(seed_end, source_end)
        
        if overlap_start <= overlap_end:
            if seed_start <= overlap_start - 1:
                seed_ranges.append((seed_start, overlap_start - 1))
            
            seed_ranges.append((map_seed(overlap_start, m), map_seed(overlap_end, m)))
            
            if overlap_end + 1 <= seed_end:
                seed_start = overlap_end + 1
            else:
                seed_start = sys.maxsize 
                break
    
    if seed_start <= seed_end:
        seed_ranges.append((seed_start, seed_end))

    return seed_ranges

with open(FILE) as f:
    seeds = list(map(int, f.readline().split()[1:]))
    f.readline() 
    f.readline() 
    maps = []
    map_ranges = []

    for line in f:
        if line == '\n':
            map_ranges.sort(key=itemgetter(1)) 
            maps.append(map_ranges)
            map_ranges = []
            next(f) 
        else:
            map_ranges.append(tuple(map(int, line.split())))
    if map_ranges:  
        map_ranges.sort(key=itemgetter(1)) 
        maps.append(map_ranges)

    seed_ranges = [(seeds[i], seeds[i] + seeds[i + 1] - 1) for i in range(0, len(seeds), 2)]

   
    for map_ranges in maps:
        new_seed_ranges = [] 
        for seed_range in seed_ranges:
            new_seed_ranges += map_seed_range(seed_range, map_ranges)
        seed_ranges = new_seed_ranges

    lowest_location = min(seed_range[0] for seed_range in seed_ranges)
    print(f"Solution Part 2: {lowest_location}")