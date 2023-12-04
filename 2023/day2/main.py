import re

regex1 = re.compile(r'Game\s(\d+):(.*)')

regex2 = re.compile(r'(\d+)\s(red|blue|green)')


def is_valid_amount(color, amount):
    if (color == 'red' and amount > 12) \
    or (color == 'green' and amount > 13) \
    or (color == 'blue' and amount > 14):
        return False
    return True


def part1(s):
    result = 0
    for line in s.splitlines():
        game_id, game_info = regex1.match(line).groups()

        valid = True
        for match in regex2.finditer(game_info):
            amount, color = match.groups()
            if not is_valid_amount(color, int(amount)):
                valid = False
                break

        if valid:
            result += int(game_id)

    return result


def part2(s):
    result = 0
    for line in s.splitlines():
        game_id, game_info = regex1.match(line).groups()

        red = green = blue = 0
        for match in regex2.finditer(game_info):
            amount, color = match.groups()
            match color:
                case 'red': red = max(red, int(amount))
                case 'green': green = max(green, int(amount))
                case _: blue = max(blue, int(amount))
        
        result += red * green * blue

    return result


test = \
"""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""


def main():
    assert part1(test) == 8
    assert part2(test) == 2286
    with open("./input", "r") as file:
        input = file.read()
        print("Part 1: ", part1(input))
        print("Part 2: ", part2(input))


if __name__ == '__main__':
    main()
