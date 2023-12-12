def get_arrangements(idx, chars, hash_count, template_idx, template):
    tmp_count = 0

    while idx < len(chars):
        current_char = chars[idx]

        if current_char == '.':
            if hash_count > 0:
                if hash_count != template[template_idx] if template_idx < len(template) else 0:
                    return 0
                template_idx += 1
                hash_count = 0
        elif current_char == '#':
            hash_count += 1
            if hash_count > template[template_idx] if template_idx < len(template) else 0:
                return 0
        elif current_char == '?':
            tmp_count += get_arrangements(idx + 1, chars, hash_count + 1, template_idx, template)
            tmp_count += get_arrangements(idx + 1, chars, 0, template_idx, template)
            if hash_count == 0:
                tmp_count += get_arrangements(idx + 1, chars, 0, template_idx, template)
            elif hash_count == template[template_idx] if template_idx < len(template) else 0:
                tmp_count += get_arrangements(idx + 1, chars, 0, template_idx + 1, template)
            return tmp_count
        else:
            raise ValueError("Unknown char")

        idx += 1

    if idx >= len(chars):
        if (template_idx == len(template) - 1 and hash_count == template[template_idx]) or \
                (template_idx == len(template) and hash_count == 0):
            return 1

    return tmp_count

with open("input.txt", "r") as file:
    lines = file.read().splitlines()

arrangements = 0
for line in lines:
    parts = line.split(" ")
    template = [int(x) for x in parts[1].split(",")]

    chars = list(parts[0])
    arrangements += get_arrangements(0, chars, 0, 0, template)

print(arrangements)