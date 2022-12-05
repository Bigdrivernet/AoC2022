Stacks = [
    ["D", "T", "W", "F", "J", "S", "H", "N"],
    ["H", "R", "P", "Q", "T", "N", "B", "G"],
    ["L", "Q", "V"],
    ["N", "B", "S", "W", "R", "Q"],
    ["N", "D", "F", "T", "V", "M", "B"],
    ["M", "D", "B", "V", "H", "T", "R"],
    ["D", "B", "Q", "J"],
    ["D", "N", "J", "V", "R", "Z", "H", "Q"],
    ["B", "N", "H", "M", "S"]
]
SecondStacks = Stacks

Moves = open("Day 5\input.txt").read().split("\n")

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