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

knots = [{"x" : 0, "y" : 0}, {"x" : 0, "y" : 0}, {"x" : 0, "y" : 0}, {"x" : 0, "y" : 0}, {"x" : 0, "y" : 0}, {"x" : 0, "y" : 0}, {"x" : 0, "y" : 0}, {"x" : 0, "y" : 0}, {"x" : 0, "y" : 0}, {"x" : 0, "y" : 0}]
tail_positions = [(0, 0)]

for move in input:
    for i in range(int(move[1])):
        match move[0]:
            case "U":
                knots[0]["y"] += 1
            case "D":
                knots[0]["y"] += -1
            case "R":
                knots[0]["x"] += 1
            case "L":
                knots[0]["x"] += -1
        for i in range(1, len(knots)):
            if max(abs(knots[i]["x"] - knots[i - 1]["x"]), abs(knots[i]["y"] - knots[i - 1]["y"])) > 1:
                dx = knots[i - 1]["x"] - knots[i]["x"]
                dy = knots[i - 1]["y"] - knots[i]["y"]
                if dx < -1 or dx > 1:
                    dx *= 0.5
                if dy < -1 or dy > 1:
                    dy *= 0.5
            
                knots[i]["x"] += dx
                knots[i]["y"] += dy
                if i == (len(knots) - 1):
                    tail_positions.append((knots[i]["x"], knots[i]["y"]))

print(len(set(tail_positions)))
