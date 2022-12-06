def day6_1(file):
    seq = []
    for pos, char in enumerate(str(file.read())):
        seq.append(char)
        if len(seq) == 4:
            if len(set(seq)) == 4:
                print(pos + 1)
            else:
                seq.pop(0)


def day6_2(file):
    seq = []
    for pos, char in enumerate(str(file.read())):
        seq.append(char)
        if len(seq) == 14:
            if len(set(seq)) == 14:
                print(pos + 1)
            else:
                seq.pop(0)


def main():
    file = open("day6.txt", "r")
    day6_2(file)


if __name__ == "__main__":
    main()
