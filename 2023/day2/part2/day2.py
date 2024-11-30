input_file_path = "input.txt"
result = []
with open(input_file_path, "r") as input_file:
    for line in input_file:
        id=line.split("Game ")[1]
        id=id.split(":")[0]
        game=line.split(f'{id}:')[1]
        sets=game.split("; ")
        min_red = 0
        min_green = 0
        min_blue = 0
        for set in sets:
            balls=set.split(", ")
            for ball in balls:
                removed_spaces = str.replace(ball, " ", "")
                color = ""
                if removed_spaces.count("red") > 0:
                    color = "red"
                    number_of_balls = int(removed_spaces.split(color)[0])
                    if not min_red or number_of_balls > min_red:
                        min_red = number_of_balls
                elif removed_spaces.count("green") > 0:
                    color = "green"
                    number_of_balls = int(removed_spaces.split(color)[0])
                    if not min_green or number_of_balls > min_green:
                        min_green = number_of_balls
                elif removed_spaces.count("blue") > 0:
                    color = "blue"
                    number_of_balls = int(removed_spaces.split(color)[0])
                    if not min_blue or number_of_balls > min_blue:
                        min_blue = number_of_balls
        multiplied = min_red * min_green * min_blue
        result.append(multiplied)
                                
result_sum = sum(result)
print(result_sum)
