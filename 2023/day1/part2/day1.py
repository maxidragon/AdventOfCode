input_file_path = "input.txt"
result = 0
numbers_str = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
numbers_str_to_iterate = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def first_digit_fun(line):
    for char in line:
        if char.isdigit():
            return char
def first_word_fun(line):
    return_element = None
    earliest_element = None
    for element in numbers_str_to_iterate:
        str_element = str(element)
        if str_element in line:
            if earliest_element is None or line.index(str_element) < line.index(str(earliest_element)):
                earliest_element = str_element
        if earliest_element:
            return_element = earliest_element
    return return_element

def last_digit_fun(line):
    return_element = None
    for char in line[::-1]:
        if char.isdigit():
            return_element = char
            break
    return return_element

def last_word_fun(line):
    return_element = None
    last_element = None
    for element in numbers_str_to_iterate:
        str_element = str(element)
        if str_element in line:
            if last_element is None or line.index(str_element) > line.index(str(last_element)):
                last_element = str_element
        if last_element:
            return_element = last_element
    return return_element

def find_earliest_element(line):
    return_element = None
    first_digit = first_digit_fun(line)
    first_word = first_word_fun(line)
    if first_digit is not None and first_word is not None:
        if line.index(str(first_digit)) < line.index(str(first_word)):
            return_element = str(first_digit)
        else:
            str_to_number = numbers_str.index(first_word)
            return_element = str(str_to_number)
    else:
        if first_digit is not None:
            return_element = str(first_digit)
        else:
            str_to_number = numbers_str.index(first_word)
            return_element = str(str_to_number)

    return return_element
        
def find_last_element(line):
    return_element = None
    last_digit = last_digit_fun(line)
    last_word = last_word_fun(line)
    if last_digit is not None and last_word is not None:
        if line.index(str(last_digit)) > line.index(str(last_word)):
            return_element = str(last_digit)
        else:
            str_to_number = numbers_str.index(last_word)
            return_element = str(str_to_number)
    else:
        if last_digit is not None:
            return_element = str(last_digit)
        else:
            str_to_number = numbers_str.index(last_word)
            return_element = str(str_to_number)
    return return_element
with open(input_file_path, "r") as input_file:
    for line in input_file:
        numbers = []
        numbers.append(find_earliest_element(line))
        numbers.append(find_last_element(line))
        sum = numbers[0] + numbers[-1]    
        print(sum)
        result += int(sum)
        
print(result)    

