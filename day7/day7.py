class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return "{} (file, size={})".format(self.name, self.size)


class Dir:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.children = []
        self.size = 0

    def __repr__(self):
        return "{} (dir)".format(self.name)


def build_tree(file):
    current_dir = Dir(None, '/')
    root = current_dir
    for line in file:
        cmd = line.strip().split()
        if cmd[0] == '$':
            if cmd[1] == 'cd':
                if cmd[2] == '..':
                    current_dir = current_dir.parent
                else:
                    for child in current_dir.children:
                        if child.name == cmd[2]:
                            current_dir = child
        elif cmd[0] == 'dir':
            new_dir = Dir(current_dir, cmd[1])
            current_dir.children.append(new_dir)
        elif cmd[0].isdigit():
            new_file = File(current_dir, int(cmd[0]))
            current_dir.children.append(new_file)
    return root


def calc_dir_sizes(node):
    if isinstance(node, File):
        return int(node.size)
    elif isinstance(node, Dir):
        for child in node.children:
            node.size += calc_dir_sizes(child)
        return node.size


def calc_output_p1(node):
    output = 0
    if isinstance(node, Dir):
        if node.size <= 100000:
            output += node.size
        for child in node.children:
            output += calc_output_p1(child)
    return output


def day7_1(file):
    tree = build_tree(file)
    calc_dir_sizes(tree)
    print(calc_output_p1(tree))


def calc_output_p2(node, space, min):
    if isinstance(node, Dir):
        if min > node.size >= space:
            min = node.size
        for child in node.children:
            min = calc_output_p2(child, space, min)
    return min


def day7_2(file):
    tree = build_tree(file)
    calc_dir_sizes(tree)
    required_space = 30000000 - (70000000 - tree.size)
    print(calc_output_p2(tree, required_space, tree.size))


def main():
    file = open("day7.txt", "r")
    day7_2(file)


if __name__ == "__main__":
    main()
