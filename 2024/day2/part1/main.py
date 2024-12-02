input_file_path = "input.txt"

safe = 0
with open(input_file_path, "r") as input_file:
    for line in input_file:
        numbers = [int(x) for x in line.split()]
        is_safe = True
        increasing = all(numbers[i] < numbers[i+1] for i in range(len(numbers) - 1))
        decreasing = all(numbers[i] > numbers[i+1] for i in range(len(numbers) - 1))
        for i in range(len(numbers) - 1):
            diff = abs(numbers[i] - numbers[i+1])
            if diff < 1 or diff > 3:
                is_safe = False
                break
        if is_safe and (increasing or decreasing):
            safe += 1

print(safe)
