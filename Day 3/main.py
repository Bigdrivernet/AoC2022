import string
Backpacks = open("Day 3\input.txt").read().split("\n")
Sum = 0
for i in range(len(Backpacks)):
    Backpack = [Backpacks[i][:len(Backpacks[i])//2], Backpacks[i][len(Backpacks[i])//2:]]
    Backpack = set(Backpack[0]).intersection(Backpack[1])
    for Character in Backpack:
        Sum += string.ascii_letters.index(Character) + 1

print(Sum)

BadgeSum = 0
for i in range(len(Backpacks)//3):
    Badge = set(Backpacks[i*3]).intersection(Backpacks[i*3 + 1])
    Badge = Badge.intersection(Backpacks[i*3 + 2])
    for Character in Badge: #There should only be one item in a set at this point but sets are weird
        BadgeSum += string.ascii_letters.index(Character) + 1

print(BadgeSum)