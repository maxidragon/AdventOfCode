import re

input_file_path = "input.txt"

sum = 0

with open(input_file_path, "r") as input_file:
    for line in input_file:
        matches = re.findall(r"mul\(\d+,\s*\d+\)", line)
        for match in matches:
            a, b = map(int, re.findall(r"\d+", match))
            sum += a * b

print(sum)
