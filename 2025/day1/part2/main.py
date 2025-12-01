input_file_path = "input.txt"

#this can be done better lol
with open(input_file_path, "r") as input_file:
    dial = 50
    times = 0
    for line in input_file:
        if line.startswith("L"):
            converted = int(line.split("L")[1])
            if converted > 100:
                converted = converted % 100
            if dial - converted < 0:
                if converted > 100:
                    dial = abs(dial - converted) - 100
                else:
                    dial = 100 - (abs(dial - converted))
            else:
                dial = dial - converted
        elif line.startswith("R"):
            converted = int(line.split("R")[1])
            if converted > 100:
                converted = converted % 100
            if dial + converted >= 100:
                if converted > 100:
                    dial = abs(dial + converted)
                else:
                    dial = (dial + converted) - 100
            else:
                dial = dial + converted 
        print(f'line : {line.strip()} dial: {dial}')
        if dial == 0:
            times +=1

print(times)
