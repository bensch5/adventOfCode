def day10_1(file, cycles):
    lines = [line.strip().split() for line in file]
    addx = False
    addx_val = 0
    reg_val = 1
    cycle = 1
    i = 0
    output = 0
    while i in range(len(lines)):
        if addx:
            addx = False
            reg_val += addx_val
            i += 1
        else:
            if lines[i][0] == "addx":
                addx = True
                addx_val = int(lines[i][1])
            elif lines[i][0] == "noop":
                i += 1

        cycle += 1

        if cycle in cycles:
            output += reg_val * cycle

    print(output)


def day10_2(file):
    lines = [line.strip().split() for line in file]
    addx = False
    addx_val = 0
    reg_val = 1
    cycle = 1
    i = 0
    output = ""
    while i in range(len(lines)):
        if addx:
            addx = False
            reg_val += addx_val
            i += 1
        else:
            if lines[i][0] == "addx":
                addx = True
                addx_val = int(lines[i][1])
            elif lines[i][0] == "noop":
                i += 1

        if cycle % 40 in range(reg_val - 1, reg_val + 2):
            output += "#"
        else:
            output += "."

        if cycle % 40 == 0:
            output += "\n"

        cycle += 1

    print(output)


def main():
    file = open("day10.txt")
    lst = [20, 60, 100, 140, 180, 220]
    day10_2(file)  # WHY IS THIS ONE CHARACTER AHEAD


if __name__ == "__main__":
    main()
