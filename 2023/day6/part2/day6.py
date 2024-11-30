file_path = "input.txt"
race = {}
with open(file_path, "r") as f:
    lines = f.readlines()
    times = lines[0].split(':')[1].strip()
    times = times.split(' ')
    time = ''
    for elem in times:
        if elem.isdigit():
            time = time + str(elem)
    distances = lines[1].split(':')[1].strip()
    distances = distances.split(' ')
    distance = ''
    for elem in distances:
        if elem.isdigit():
            distance = distance + str(elem)
    race = {
        "time": int(time),
        "distance": int(distance)
    }


max_distance_attempts = 0
for i in range(14, race["time"]):
    distance = (race["time"] - i)*i 
    if distance > race["distance"]:
        max_distance_attempts += 1

print(max_distance_attempts)  
