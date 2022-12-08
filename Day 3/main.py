import string
backpacks = open("Day 3\input.txt").read().split("\n")
sum = 0
for i in range(len(backpacks)):
    backpack = [backpacks[i][:len(backpacks[i])//2], backpacks[i][len(backpacks[i])//2:]]
    backpack = set(backpack[0]).intersection(backpack[1])
    for character in backpack:
        sum += string.ascii_letters.index(character) + 1

print(sum)

badge_sum = 0
for i in range(len(backpacks)//3):
    badge = set(backpacks[i*3]).intersection(backpacks[i*3 + 1])
    badge = badge.intersection(backpacks[i*3 + 2])
    for character in badge: #There should only be one item in a set at this point but sets are weird
        badge_sum += string.ascii_letters.index(character) + 1

print(badge_sum)