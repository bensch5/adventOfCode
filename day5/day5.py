def day5_1(file, ship):
    for line in file:
        line = line.strip().split()
        for i in range(int(line[1])):
            elem = ship[int(line[3]) - 1].pop()
            ship[int(line[5]) - 1].append(elem)
    output = ''
    for stack in ship:
        output += stack[-1]
    print(output)


def day5_2(file, ship):
    for line in file:
        line = line.strip().split()
        amount = int(line[1])
        sub_stack = []
        for i in range(amount):
            elem = ship[int(line[3]) - 1].pop(-(amount-i))
            sub_stack.append(elem)
        ship[int(line[5]) - 1].extend(sub_stack)
    output = ''
    for stack in ship:
        output += stack[-1]
    print(output)


def main():
    file = open("day5.txt", "r")
    ship = [
        ['B', 'Z', 'T'],
        ['V', 'H', 'T', 'D', 'N'],
        ['B', 'F', 'M', 'D'],
        ['T', 'J', 'G', 'W', 'V', 'Q', 'L'],
        ['W', 'D', 'G', 'P', 'V', 'F', 'Q', 'M'],
        ['V', 'Z', 'Q', 'G', 'H', 'F', 'S'],
        ['Z', 'S', 'N', 'R', 'L', 'T', 'C', 'W'],
        ['Z', 'H', 'W', 'D', 'J', 'N', 'R', 'M'],
        ['M', 'Q', 'L', 'F', 'D', 'S']
    ]
    ship_test = [
        ['Z', 'N'],
        ['M', 'C', 'D'],
        ['P']
    ]
    day5_2(file, ship)


if __name__ == "__main__":
    main()
