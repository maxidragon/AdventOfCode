input_file_path = "input.txt"

similarity = 0
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
        

    for number in numbers_a:
        similarity += number * numbers_b.count(number)

print(similarity)
        
