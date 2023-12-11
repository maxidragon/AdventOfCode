def get_galaxies(universe_map, empty_space_size):
    galaxies = []

    real_y = 0
    for y, row in enumerate(universe_map):
        if row[0] == '@':
            real_y += empty_space_size
            continue
        real_x = 0
        for x, cell in enumerate(row):
            if cell == '@':
                real_x += empty_space_size
                continue
            if cell == '#':
                galaxies.append((real_x, real_y))
            real_x += 1
        real_y += 1
    return galaxies

def expand_universe(input_str):
    lines = []

    for line in input_str.splitlines():
        line = line.strip()

        if all(c == '.' for c in line):
            lines.append(line.replace(".", "@"))
        else:
            lines.append(line)

    universe_map = [list(line) for line in lines]

    for x in range(len(universe_map[0])):
        tmp_dots = sum(1 for y in range(len(universe_map)) if universe_map[y][x] in ('.', '@'))

        if tmp_dots == len(universe_map):
            replace_column(universe_map, x, '@')

    return universe_map


def replace_column(matrix, column, c):
    for row in matrix:
        row[column] = c

def get_pairs(input_list):
    pairs = []

    for i, item1 in enumerate(input_list):
        for item2 in input_list[i + 1:]:
            pairs.append((item1, item2))

    return pairs

with open("input.txt", "r") as file:
    input_str = file.read()

universe_map = expand_universe(input_str)
galaxies = get_galaxies(universe_map, 1000000)
pairs = get_pairs(galaxies)    
sum2 = sum(abs(x1 - x2) + abs(y1 - y2) for ((x1, y1), (x2, y2)) in pairs)
print(sum2)
