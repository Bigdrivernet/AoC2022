

InputStacks, Moves = open("Day 5\input.txt").read().split("\n\n")
InputStacks = InputStacks.split("\n")
del InputStacks[-1]

for i in range(len(InputStacks)):
    InputStacks[i] = InputStacks[i][1:len(InputStacks[i]):4]
InputStacks.reverse()

Stacks = []
for i in range(len(InputStacks[0])):
    Stack = []
    for j in range(len(InputStacks)):
        if InputStacks[j][i] != " ":
            Stack.append(InputStacks[j][i])
    Stacks.append(Stack)

SecondStacks = []
for i in range(len(InputStacks[0])):
    Stack = []
    for j in range(len(InputStacks)):
        if InputStacks[j][i] != " ":
            Stack.append(InputStacks[j][i])
    SecondStacks.append(Stack)

Moves = Moves.split("\n")

for i in range(len(Moves)):
    Move = Moves[i][5:len(Moves[i])]
    Move = Move.replace(" from ", " ")
    Move = Move.replace(" to ", " ")
    Moves[i] = Move.split()

print(Moves)

for Move in Moves:
    for i in range(int(Move[0])):
        Stacks[int(Move[2]) - 1].append(Stacks[int(Move[1]) - 1][-1])
        del Stacks[int(Move[1]) - 1][-1]

Output = ""
for Stack in Stacks:
    Output += Stack[-1]
print(Output)

for Move in Moves:
    for i in range(int(Move[0])):
        SecondStacks[int(
            Move[2]) - 1].append(SecondStacks[int(Move[1]) - 1].pop(-(int(Move[0])) + i))

SecondOutput = ""
for Stack in SecondStacks:
    SecondOutput += Stack[-1]
print(SecondOutput)
