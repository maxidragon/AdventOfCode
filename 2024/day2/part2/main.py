input_file_path = "input.txt"

safe = 0

def is_safe_report(numbers):
    if len(numbers) < 2:
        return False
    differences = [abs(numbers[i] - numbers[i+1]) for i in range(len(numbers) - 1)]
    all_in_range = all(1 <= diff <= 3 for diff in differences)
    strictly_increasing = all(numbers[i] < numbers[i+1] for i in range(len(numbers) - 1))
    strictly_decreasing = all(numbers[i] > numbers[i+1] for i in range(len(numbers) - 1))
    return all_in_range and (strictly_increasing or strictly_decreasing)

with open(input_file_path, "r") as input_file:
    for line in input_file:
        numbers = [int(x) for x in line.split()]
        
        if is_safe_report(numbers):
            safe += 1
            continue
        
        for i in range(len(numbers)):
            modified_numbers = numbers[:i] + numbers[i+1:]
            if is_safe_report(modified_numbers):
                safe += 1
                break

print(safe)
