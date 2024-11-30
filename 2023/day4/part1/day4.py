file_path = "input.txt"
score = 0

with open(file_path, 'r') as f:
    for line in f:
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
        points = 0
        for number in user_numbers:
            if number in winning_numbers:
                if points == 0:
                    points = 1
                else:
                    points = points * 2
        score += points

print(score)