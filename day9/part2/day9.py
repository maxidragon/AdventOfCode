def extrapolate(history):
    sequences = [list(map(int, history.split()[::-1]))]
    
    while any(sequences[-1]):
        differences = [sequences[-1][i + 1] - sequences[-1][i] for i in range(len(sequences[-1]) - 1)]
        sequences.append(differences)

    result = sequences[-1][-1]

    for i in range(len(sequences) - 2, -1, -1):
        result = sequences[i][-1] + result

    return result


file_path = "input.txt"
with open(file_path, "r") as file:
    oasis_lines = file.read().splitlines()

    extrapolated_values = [extrapolate(line) for line in oasis_lines]
    total_sum = sum(extrapolated_values)
    print(total_sum)


