def is_digit(char):
    return 48 <= ord(char) <= 57


def part1(s):
    result = 0
    for line in s.splitlines():
        digits = list(filter(is_digit, line))
        if digits:
            result += int(digits[0] + digits[-1])
    return result


validDigits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def part2(s):
    result = 0
    for line in s.splitlines():
        digits = []
        i = 0
        for i, char in enumerate(line):
            if is_digit(char):
                digits.append(char)
            else:
                for key, val in validDigits.items():
                    if line[i:i+len(key)] == key:
                        digits.append(val)
        if digits:
            result += int(digits[0] + digits[-1])
    return result


test_part1 = \
"""1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet
"""

test_part2 = \
"""two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""


def main():
    assert part1(test_part1) == 142
    assert part2(test_part2) == 281
    with open("./input", "r") as file:
        input = file.read()
        print("Part 1: ", part1(input))
        print("Part 2: ", part2(input))


if __name__ == '__main__':
    main()
