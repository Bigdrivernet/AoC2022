Pairs = open("Day 4\input.txt").read().split("\n")
for i in range(len(Pairs)):
    Pair = Pairs[i].split(",")
    Pairs[i] = [Pair[0].split("-"), Pair[1].split("-")]

print(Pairs)

SumFullOverlap = 0
SumOverlap = 0
for Pair in Pairs:
    SetA = set(range(int(Pair[0][0]), int(Pair[0][1]) + 1))
    SetB = set(range(int(Pair[1][0]), int(Pair[1][1]) + 1))
    if SetA.issubset(SetB) or SetB.issubset(SetA):
        SumFullOverlap += 1
    if len(SetA.intersection(SetB)) != 0:
        SumOverlap += 1

print(SumFullOverlap)
print(SumOverlap)