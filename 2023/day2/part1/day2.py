input_file_path = "input.txt"
result = []
max_red = 12
max_green = 13
max_blue = 14
with open(input_file_path, "r") as input_file:
    for line in input_file:
        id=line.split("Game ")[1]
        id=id.split(":")[0]
        game=line.split(f'{id}:')[1]
        sets=game.split("; ")
        ok = True
        for set in sets:
            balls=set.split(", ")
            for ball in balls:
                removed_spaces = str.replace(ball, " ", "")
                color = ""
                if removed_spaces.count("red") > 0:
                    color = "red"
                    number_of_balls = int(removed_spaces.split(color)[0])
                    if number_of_balls > max_red:
                        ok = False
                elif removed_spaces.count("green") > 0:
                    color = "green"
                    number_of_balls = int(removed_spaces.split(color)[0])
                    if number_of_balls  > max_green:
                        ok = False
                elif removed_spaces.count("blue") > 0:
                    color = "blue"
                    number_of_balls = int(removed_spaces.split(color)[0])
                    if number_of_balls  > max_blue:
                        ok = False
        if ok:
            result.append(int(id))

result_sum = sum(result)
print(result_sum)