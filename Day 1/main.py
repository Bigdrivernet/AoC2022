Input = open("Day 1\input.txt").read()
ElvesList = Input.split("\n\n")

Elves = len(ElvesList)
print(Elves)
for i in range(len(ElvesList)):
    SubList = ElvesList[i].split("\n")
    Sum = 0
    for Element in SubList:
        Sum += int(Element)
    ElvesList[i] = Sum

ElvesList.sort()

print(ElvesList)
print(f"Maximum: {max(ElvesList)}")
SumThreeBiggest = ElvesList[Elves - 1] + ElvesList[Elves - 2] + ElvesList[Elves - 3]
print(f"Die drei Maxima: {SumThreeBiggest}")