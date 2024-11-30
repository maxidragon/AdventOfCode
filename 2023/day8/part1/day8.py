instructions = ""
nodes = {}
now = ""
with open("input.txt") as f:
    lines = f.readlines()
    instructions = lines[0].strip()
    
    for line in lines[2:]:
        elem = line.split(" =")[0]
        if now == "":
            now = elem
        elements = line.split(" =")[1].split("(")
        elements = elements[1].split(")")[0].split(" ")
        elements = [x for x in elements if x != ""]
        elem1 = elements[0].split(",")[0]
        elem2 = elements[1] 
        nodes[elem] = {
            "left": elem1,
            "right": elem2
        }
steps = 0
now_instruction = 0
while now != "ZZZ":
    if now_instruction >= len(instructions):
        now_instruction = 0
    if instructions[now_instruction] == "L":
        now = nodes[now]["left"]
    elif instructions[now_instruction] == "R":
        now = nodes[now]["right"]    
    now_instruction += 1       
    steps += 1



print(steps)
