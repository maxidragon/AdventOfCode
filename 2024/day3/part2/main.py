import re

input_file_path = "input.txt"

def extract_valid_muls(input_string):
    mul_pattern = r"mul\(\d+,\s*\d+\)"
    control_pattern = r"(do\(\)|don't\(\))"
    instructions = re.finditer(f"{control_pattern}|{mul_pattern}", input_string)

    valid_muls = []
    enabled = True

    for match in instructions:
        text = match.group(0)
        if text == "do()":
            enabled = True
        elif text == "don't()":
            enabled = False
        elif enabled and re.match(mul_pattern, text):
            valid_muls.append(text)
    
    return valid_muls

sum = 0

with open(input_file_path, "r") as input_file:
    for line in input_file:
        matches = extract_valid_muls(line)
        for match in matches:
            a, b = map(int, re.findall(r"\d+", match))
            sum += a * b

print(sum)
