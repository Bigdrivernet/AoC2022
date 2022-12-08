input_stacks, moves = open("Day 5\input.txt").read().split("\n\n")
input_stacks = input_stacks.split("\n")
del input_stacks[-1]

for i in range(len(input_stacks)):
    input_stacks[i] = input_stacks[i][1:len(input_stacks[i]):4]
input_stacks.reverse()

stacks = []
for i in range(len(input_stacks[0])):
    stack = []
    for j in range(len(input_stacks)):
        if input_stacks[j][i] != " ":
            stack.append(input_stacks[j][i])
    stacks.append(stack)

second_stacks = []
for i in range(len(input_stacks[0])):
    stack = []
    for j in range(len(input_stacks)):
        if input_stacks[j][i] != " ":
            stack.append(input_stacks[j][i])
    second_stacks.append(stack)

moves = moves.split("\n")

for i in range(len(moves)):
    move = moves[i][5:len(moves[i])]
    move = move.replace(" from ", " ")
    move = move.replace(" to ", " ")
    moves[i] = move.split()

print(moves)

for move in moves:
    for i in range(int(move[0])):
        stacks[int(move[2]) - 1].append(stacks[int(move[1]) - 1][-1])
        del stacks[int(move[1]) - 1][-1]

output = ""
for stack in stacks:
    output += stack[-1]
print(output)

for move in moves:
    for i in range(int(move[0])):
        second_stacks[int(
            move[2]) - 1].append(second_stacks[int(move[1]) - 1].pop(-(int(move[0])) + i))

second_output = ""
for stack in second_stacks:
    second_output += stack[-1]
print(second_output)