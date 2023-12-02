def day1_1(file):
    max = 0
    current = 0
    for line in file:
        if line.isspace():
            if current > max:
                max = current
            current = 0
        else:
            current += int(line)
    print(max)


def day1_2(file):
    max1, max2, max3 = 0, 0, 0
    current = 0
    for line in file:
        if line.isspace():
            max1, max2, max3 = update_max(current, max1, max2, max3)
            current = 0
        else:
            current += int(line)
    print(sum(update_max(current, max1, max2, max3)))


def update_max(current, max1, max2, max3):
    if current > max1:
        max3 = max2
        max2 = max1
        max1 = current
    elif current > max2:
        max3 = max2
        max2 = current
    elif current > max3:
        max3 = current
    return max1, max2, max3


def main():
    file = open("day1.txt", "r")
    day1_2(file)


if __name__ == "__main__":
    main()
