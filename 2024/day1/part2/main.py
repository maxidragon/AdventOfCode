input_file_path = "input.txt"

distance = 0
with open(input_file_path, "r") as input_file:
    numbers_a = []
    numbers_b = []
    for line in input_file:
        try:
            number_a = int(line.split()[0])
            number_b = int(line.split()[1])
        except ValueError:
            pass
        numbers_a.append(number_a)
        numbers_b.append(number_b)
        
    sorted_numbers_a = sorted(numbers_a)
    sorted_numbers_b = sorted(numbers_b)
    
    for i in range(0, len(sorted_numbers_a)):
        distance += abs(sorted_numbers_a[i] - sorted_numbers_b[i])

print(distance)
        
