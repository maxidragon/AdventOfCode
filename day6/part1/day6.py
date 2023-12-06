from functools import reduce


file_path = "input.txt"
races = []
with open(file_path, "r") as f:
    lines = f.readlines()
    times = lines[0].split(':')[1].strip()
    times = times.split(' ')
    times = [int(s) for s in times if s.isdigit()]
    distances = lines[1].split(':')[1].strip()
    distances = distances.split(' ')
    distances = [int(s) for s in distances if s.isdigit()]
    for i in range(len(times)):
        races.append({'time': times[i], 'distance': distances[i]})
result = []
for race in races:
    max_distance_attempts = 0
    for i in range(0, race["time"]+1):
        distance = (race["time"] - i)*i 
        if distance > race["distance"]:
            max_distance_attempts += 1
            
    result.append(max_distance_attempts)
    
multiplied = reduce(lambda x, y: x*y, result) 
print(multiplied)