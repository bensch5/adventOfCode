def update_position1(diff_x, diff_y, pos):
    if diff_x > 1:
        pos[0] += 1
        if diff_y == 1:
            pos[1] += 1
        elif diff_y == -1:
            pos[1] -= 1
    elif diff_x < -1:
        pos[0] -= 1
        if diff_y == 1:
            pos[1] += 1
        elif diff_y == -1:
            pos[1] -= 1
    elif diff_y > 1:
        pos[1] += 1
        if diff_x == 1:
            pos[0] += 1
        elif diff_x == -1:
            pos[0] -= 1
    elif diff_y < -1:
        pos[1] -= 1
        if diff_x == 1:
            pos[0] += 1
        elif diff_x == -1:
            pos[0] -= 1


def day9_1(file):
    pos_h = [0, 0]
    pos_t = [0, 0]
    positions = []

    for line in file:
        cmd = line.strip().split()
        for i in range(int(cmd[1])):
            match cmd[0]:
                case 'U': pos_h[1] += 1
                case 'D': pos_h[1] -= 1
                case 'L': pos_h[0] -= 1
                case 'R': pos_h[0] += 1

            diff_x = pos_h[0] - pos_t[0]
            diff_y = pos_h[1] - pos_t[1]
            update_position1(diff_x, diff_y, pos_t)
            positions.append((pos_t[0], pos_t[1]))
    print(len(set(positions)))


def update_position2(diff_x, diff_y, pos):
    pass  # HOWWWWWW


def day9_2(file):
    rope = []
    for i in range(10):
        rope.append([0, 0])
    positions = []

    for line in file:
        cmd = line.strip().split()
        for i in range(int(cmd[1])):
            match cmd[0]:
                case 'U': rope[0][1] += 1
                case 'D': rope[0][1] -= 1
                case 'L': rope[0][0] -= 1
                case 'R': rope[0][0] += 1

            for j in range(1, 10):
                knot = rope[j]
                diff_x = rope[j - 1][0] - knot[0]
                diff_y = rope[j - 1][1] - knot[1]
                update_position2(diff_x, diff_y, knot)
                rope[j] = knot
            positions.append((rope[9][0], rope[9][1]))
    print(len(set(positions)))


def main():
    file = open("day9.txt")
    day9_2(file)


if __name__ == "__main__":
    main()
