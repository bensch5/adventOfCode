def day3_1(file):
    score = 0
    for line in file:
        line = line.strip()
        part1 = line[:int((len(line)/2))]
        part2 = line[int((len(line)/2)):]
        for char in part1:
            if char in part2:
                if char.islower():
                    score += ord(char) - 96
                else:
                    score += ord(char) - 64 + 26
                break
    print(score)


def day3_2(file):
    score = 0
    list = []
    for line in file:
        line = line.strip()
        list.append(line)
        if len(list) == 3:
            for char in list[0]:
                if char in list[1] and char in list[2]:
                    if char.islower():
                        score += ord(char) - 96
                    else:
                        score += ord(char) - 64 + 26
                    list = []
                    break
    print(score)


def main():
    file = open("day3.txt", "r")
    day3_2(file)


if __name__ == "__main__":
    main()
