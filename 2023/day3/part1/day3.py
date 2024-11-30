import re

def is_adjacent_to_symbol(schematic, i, j):
    for di in [-1, 0, 1]:
        for dj in [-1, 0, 1]:
            if 0 <= i+di < len(schematic) and 0 <= j+dj < len(schematic[0]) and schematic[i+di][j+dj] not in '0123456789.':
                return True
    return False

def sum_part_numbers(schematic):
    total = 0
    for i, row in enumerate(schematic):
        for match in re.finditer(r'\d+', ''.join(row)):
            num = match.group()
            start, end = match.span()
            if any(is_adjacent_to_symbol(schematic, i, j) for j in range(start, end)):
                total += int(num)
    return total

def load_schematic(filename):
    with open(filename, 'r') as file:
        return [list(line.strip()) for line in file]

schematic = load_schematic('input.txt')

print(sum_part_numbers(schematic))