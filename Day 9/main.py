input = open("Day 9\input.txt").read().split("\n")
for i in range(len(input)):
    input[i] = input[i].split(" ")

head = {"x" : 0, "y" : 0}
tail = {"x" : 0, "y" : 0}
tail_positions = [(0, 0)]

for move in input:
    for i in range(int(move[1])):
        match move[0]:
            case "U":
                head["y"] += 1
            case "D":
                head["y"] += -1
            case "R":
                head["x"] += 1
            case "L":
                head["x"] += -1
        
        if max(abs(tail["x"] - head["x"]), abs(tail["y"] - head["y"])) > 1:
            dx = head["x"] - tail["x"]
            dy = head["y"] - tail["y"]
            if dx < -1 or dx > 1:
                dx *= 0.5
            if dy < -1 or dy > 1:
                dy *= 0.5
            
            tail["x"] += dx
            tail["y"] += dy
                
            tail_positions.append((tail["x"], tail["y"]))

print(len(set(tail_positions)))