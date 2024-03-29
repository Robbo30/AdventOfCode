##Part1
import re

file_path = "D:\\AdventOfCode\\Day4\\Day4Input.txt"
with open(file_path, "r") as file:
    puzzle_input = file.readlines()


def calculate_points(puzzle_input):
    total_points = 0

    for line in puzzle_input:
        
        parts = line.split(": ")[1].split("|")
        winning_numbers = set(map(int, parts[0].strip().split()))
        your_numbers = set(map(int, parts[1].strip().split()))

        matches = winning_numbers.intersection(your_numbers)

        points = 0
        if matches:
            points = 2 ** (len(matches) - 1)

        total_points += points

    return total_points

total_points = calculate_points(puzzle_input)

print(f"Solution Part 1: {total_points}")

##Part2

def calculate_total_scratchcards(puzzle_input):
    cards = []
    for line in puzzle_input:
        parts = line.split(": ")[1].split("|")
        winning_numbers = set(map(int, parts[0].strip().split()))
        your_numbers = set(map(int, parts[1].strip().split()))
        cards.append((winning_numbers, your_numbers))

    card_copies = [1] * len(cards)  

    for i in range(len(cards)):
        winning_numbers, your_numbers = cards[i]
        matches = winning_numbers.intersection(your_numbers)

        for j in range(1, len(matches) + 1):
            if i + j < len(cards):
                card_copies[i + j] += card_copies[i]

    return sum(card_copies)

total_scratchcards = calculate_total_scratchcards(puzzle_input)

print(f"Solution Part 2: {total_scratchcards}")