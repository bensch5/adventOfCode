def day4_1(file):
    pairs = 0
    for line in file:
        line = line.strip().split(',')
        for i, r in enumerate(line):
            line[i] = r.split('-')
        r00, r01 = int(line[0][0]), int(line[0][1])
        r10, r11 = int(line[1][0]), int(line[1][1])
        if (r00 in range(r10, r11 + 1) and r01 in range(r10, r11 + 1)) \
                or (r10 in range(r00, r01 + 1) and r11 in range(r00, r01 + 1)):
            pairs += 1
    print(pairs)


def day4_2(file):
    pairs = 0
    for line in file:
        line = line.strip().split(',')
        for i, r in enumerate(line):
            line[i] = r.split('-')
        r00, r01 = int(line[0][0]), int(line[0][1])
        r10, r11 = int(line[1][0]), int(line[1][1])
        if (r00 in range(r10, r11 + 1) or r01 in range(r10, r11 + 1)) \
                or (r10 in range(r00, r01 + 1) or r11 in range(r00, r01 + 1)):
            pairs += 1
    print(pairs)


def main():
    file = open("day4.txt", "r")
    day4_2(file)

    for i in range(3, 7):
        if i not in range(2, 9):
            break


if __name__ == "__main__":
    main()
