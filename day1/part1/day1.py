input_file_path = "input.txt"
result = 0
with open(input_file_path, "r") as input_file:
    for line in input_file:
        numbers = []
        for char in line:
            try:
                number = int(char)
                numbers.append(char)
            except ValueError:
                pass
        sum = numbers[0] + numbers[-1]    
        result += int(sum)
        
print(result)    
