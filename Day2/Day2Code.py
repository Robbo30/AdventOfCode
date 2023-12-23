##Part 1

input = open("D:\\AdventOfCode\\Day2\\Day2Input.txt", "r")
input = input.read()

max_cubes = {"red": 12, "green": 13, "blue": 14}

def parse_games_input(input):
    games = []
    for line in input.strip().split("\n"):
        game_id, rounds = line.split(":")
        game_id = int(game_id.split(" ")[1])  
        rounds_data = rounds.split(";")
        rounds_list = []
        for round_data in rounds_data:
            cubes = {"red": 0, "green": 0, "blue": 0}
            for cube_info in round_data.strip().split(","):
                number, color = cube_info.strip().split(" ")
                cubes[color] = max(cubes[color], int(number))
            rounds_list.append(cubes)
        games.append((game_id, rounds_list))
    return games

def is_game_possible(game, max_cubes):
    for round_cubes in game[1]:
        for color in max_cubes:
            if round_cubes[color] > max_cubes[color]:
                return False
    return True

games = parse_games_input(input)

possible_games_sum = sum(game[0] for game in games if is_game_possible(game, max_cubes))

print(f"Solution Part 1: {possible_games_sum}")

##Part 2 

def minimum_cubes_and_power(games):
    powers = []
    for game in games:
        min_cubes = {"red": 0, "green": 0, "blue": 0}
        for round_cubes in game[1]:
            for color in min_cubes:
                min_cubes[color] = max(min_cubes[color], round_cubes[color])
        power = min_cubes["red"] * min_cubes["green"] * min_cubes["blue"]
        powers.append(power)
    return sum(powers)

sum_of_powers = minimum_cubes_and_power(games)


print(f"Solution Part 2: {sum_of_powers}")