file_path = "input.txt"

with open(file_path, "r") as file:
    lines = file.readlines()

    cards_numbers = []
    for line in lines:
        line = line.replace('\n', '')
        line = line.split(': ')[1]
        numbers_str = line.split('| ')
        winning_numbers_str_arr = numbers_str[0].split(' ')
        winning_numbers = []
        for number in winning_numbers_str_arr:
            if number != '':
                winning_numbers.append(int(number))
        user_numbers_str_arr = numbers_str[1].split(' ')
        user_numbers = []
        for number in user_numbers_str_arr:
            if number != '':
                user_numbers.append(int(number))
        common = [num for num in winning_numbers if num in user_numbers]
        cards_numbers.append(common)

    s_nums = [1] * len(cards_numbers)

    i = 0
    total = 0
    for common in cards_numbers:
        for n in range(len(common)):
            s_nums[n + i + 1] += s_nums[i]

        if common:
            pow_val = 2 ** (len(common) - 1)
            total += pow_val

        i += 1


print(sum(s_nums))