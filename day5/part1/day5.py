# It is not a optimal solution, but it works if you have enough memory
# I'll try to find a better solution later
results = {
    'seed-to-soil': {},
    'soil-to-fertilizer': {},
    'fertilizer-to-water': {},
    'water-to-light': {},
    'light-to-temperature': {},
    'temperature-to-humidity': {},
    'humidity-to-location': {},
}
locations = []
with open('input.txt') as f:
    lines = f.readlines()

    seeds_str = lines[0].split(':')[1].strip()
    seeds = [int(s) for s in seeds_str.split(' ')]
    reading = None
    for line in lines[1:]:
        if line.startswith('seed-to-soil'):
            reading = 'seed-to-soil'
            continue
        elif line.startswith('soil-to-fertilizer'):
            reading = 'soil-to-fertilizer'
            continue
        elif line.startswith('fertilizer-to-water'):
            reading = 'fertilizer-to-water'
            continue
        elif line.startswith('water-to-light'):
            reading = 'water-to-light'
            continue
        elif line.startswith('light-to-temperature'):
            reading = 'light-to-temperature'
            continue
        elif line.startswith('temperature-to-humidity'):
            reading = 'temperature-to-humidity'
            continue
        elif line.startswith('humidity-to-location'):
            reading = 'humidity-to-location'
            continue
        print(reading)
        if reading:
            if line == '\n':
                reading = None
                continue
            numbers = [int(s) for s in line.strip().split(' ')]
            for i in range(0, numbers[2]):
                results[reading][str(numbers[1]+i)] = str(numbers[0]+i)
                
for seed in seeds:
    try: 
        soil = results['seed-to-soil'][str(seed)]
    except KeyError:
        soil = seed
    try:
        fertilizer = results['soil-to-fertilizer'][str(soil)]
    except KeyError:
        fertilizer = soil
    try:
        water = results['fertilizer-to-water'][str(fertilizer)]
    except KeyError:
        water = fertilizer
    try:
        light = results['water-to-light'][str(water)]
    except KeyError:
        light = water
    try:
        temperature = results['light-to-temperature'][str(light)]
    except KeyError:
        temperature = light
    try:
        humidity = results['temperature-to-humidity'][str(temperature)]
    except KeyError:
        humidity = temperature
    try:
        location = results['humidity-to-location'][str(humidity)]
    except KeyError:
        location = humidity
    locations.append(int(location))


print(min(locations))

