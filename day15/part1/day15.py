sum = 0
with open("input.txt", "r") as f:
    line = f.readline()
    strings = line.split(",")
    for string in strings:
        value = 0
        for char in string:
            ascii_code = ord(char)
            value += ascii_code
            value *= 17
            value = value % 256
        sum += value
        
print(sum)