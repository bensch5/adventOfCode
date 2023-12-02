def create_list(file):
    trees = []
    for line in file:
        line = line.strip()
        lst = []
        for digit in line:
            lst.append(digit)
        trees.append(lst)
    return trees


def day8_1(file):
    trees = create_list(file)
    visible = 0
    for y, lst in enumerate(trees):
        for x, tree in enumerate(lst):
            tree = int(tree)
            if x == 0 or x == len(lst) - 1 or y == 0 or y == len(trees) - 1:
                visible += 1
                continue
            skip1, skip2, skip3, skip4 = False, False, False, False
            # check all y values before current tree
            for i in range(y):
                if int(trees[i][x]) >= tree:
                    skip1 = True
                    break
            # check all y values after current tree
            for i in range(y + 1, len(trees)):
                if int(trees[i][x]) >= tree:
                    skip2 = True
                    break
            # check all x values before current tree
            for i in range(x):
                if int(trees[y][i]) >= tree:
                    skip3 = True
                    break
            # check all x values after current tree
            for i in range(x + 1, len(lst)):
                if int(trees[y][i]) >= tree:
                    skip4 = True
                    break
            if not (skip1 and skip2 and skip3 and skip4):
                visible += 1
    print(visible)


def day8_2(file):
    trees = create_list(file)
    best_score = 0
    for y, lst in enumerate(trees):
        if y == 0 or y == len(trees) - 1:
            continue
        for x, tree in enumerate(lst):
            if x == 0 or x == len(lst) - 1:
                continue
            tree = int(tree)
            score = 0
            # check all y values before current tree
            for i in range(y - 1, -1, -1):  # loop backwards
                if int(trees[i][x]) >= tree or i == 0:
                    score = y - i
                    break
            # check all y values after current tree
            for i in range(y + 1, len(trees)):
                if int(trees[i][x]) >= tree or i == len(trees) - 1:
                    score *= i - y
                    break
            # check all x values before current tree
            for i in range(x - 1, -1, -1):  # loop backwards
                if int(trees[y][i]) >= tree or i == 0:
                    score *= x - i
                    break
            # check all x values after current tree
            for i in range(x + 1, len(lst)):
                if int(trees[y][i]) >= tree or i == len(lst) - 1:
                    score *= i - x
                    break
            best_score = max(score, best_score)
    print(best_score)


def main():
    file = open("day8.txt")
    day8_2(file)


if __name__ == "__main__":
    main()
