input = open("Day 1\input.txt").read()
elves_list = input.split("\n\n")

elves = len(elves_list)
print(elves)
for i in range(len(elves_list)):
    sublist = elves_list[i].split("\n")
    sum = 0
    for element in sublist:
        sum += int(element)
    elves_list[i] = sum

elves_list.sort()

print(elves_list)
print(f"Maximum: {max(elves_list)}")
sum_three_biggest = elves_list[elves - 1] + elves_list[elves - 2] + elves_list[elves - 3]
print(f"Die drei Maxima: {sum_three_biggest}")