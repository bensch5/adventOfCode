import re

regex_nums = re.compile(r'\d+')

regex_symbols = re.compile(r'[^\d\n.]')


def part1(s):
    # size of both columns and lines
    size = len(s.splitlines())
    # remove all newline characters
    st = re.sub(r'\r?\n', '', s)

    symbols = {match.start() for match in regex_symbols.finditer(st)}

    result = 0
    for match in regex_nums.finditer(st):
        num = int(match.group(0))
        start, end = match.span()
        # check left+diagonals -> right+diagonals -> directly above -> directly below
        if (start % size > 0 and {start - 1, start - size - 1, start + size - 1}.intersection(symbols)) \
        or (end % size > 0 and {end, end - size, end + size}.intersection(symbols)) \
        or (set(range(start - size, end - size)).intersection(symbols)) \
        or (set(range(start + size, end + size)).intersection(symbols)) :
            result += num
    
    return result


def star_positions(st):
    for match in re.compile(r'\*').finditer(st):
        yield match.start()


def get_neighbors(pos, st, size):
    neighbors = set()
    if pos % size > 0:
        neighbors.update([pos - 1, pos - size - 1, pos + size - 1])
    if pos % size < size - 1:
        neighbors.update([pos + 1, pos - size + 1, pos + size + 1])
    if pos // size > 0:
        neighbors.add(pos - size)
    if pos // size < size - 1:
        neighbors.add(pos + size)
    return neighbors



def part2(s):
    # size of both columns and lines
    size = len(s.splitlines())
    # remove all newline characters
    st = re.sub(r'\r?\n', '', s)
    
    num_id_to_num = dict()
    pos_to_num_id = dict()
    for num_id, match in enumerate(regex_nums.finditer(st)):
        num_id_to_num[num_id] = int(match.group(0))
        pos_to_num_id.update({
            position : num_id
            for position in range(match.start(), match.end())
        })

    result = 0    
    for pos in star_positions(st):
        adjacent_num_ids = set()
        for neighbor in get_neighbors(pos, st, size):
            if neighbor in pos_to_num_id:
                adjacent_num_ids.add(pos_to_num_id[neighbor])
        
        if len(adjacent_num_ids) == 2:
            num1 = num_id_to_num[adjacent_num_ids.pop()]
            num2 = num_id_to_num[adjacent_num_ids.pop()]
            result += num1 * num2
   
    return result


test = \
"""467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.."""


def main():
    assert part1(test) == 4361
    assert part2(test) == 467835
    with open("./input", "r") as file:
        input = file.read()
        print("Part 1: ", part1(input))
        print("Part 2: ", part2(input))


if __name__ == '__main__':
    main()
