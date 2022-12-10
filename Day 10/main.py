input = open("Day 10\input.txt").read().split("\n")
for i in range(len(input)):
    input[i] = input[i].split(" ")

x_values = []
x = 1
cycle = 0
crt = []


for instruction in input:
    if instruction[0] == "addx":
        cycle += 1
        if abs(x - ((cycle-1)%40)) < 2:
            crt.append("#")
        else:
            crt.append(" ")
        x_values.append(x)
        cycle += 1
        if abs(x - ((cycle-1)%40)) < 2:
            crt.append("#")
        else:
            crt.append(" ")
        x_values.append(x)
        x += int(instruction[1])
    elif instruction[0] == "noop":
        cycle += 1
        if abs(x - ((cycle-1)%40)) < 2:
            crt.append("#")
        else:
            crt.append(" ")
        x_values.append(x)

sum = 0
for cycle in [20, 60, 100, 140, 180, 220]:
    sum += cycle * x_values[cycle - 1]

print(sum)

width = 40
height = 6

for i in range(height):
    print("".join(crt[i * width : (i + 1) * width - 1]))
