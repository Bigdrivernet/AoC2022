pairs = open("Day 4\input.txt").read().split("\n")
for i in range(len(pairs)):
    pair = pairs[i].split(",")
    pairs[i] = [pair[0].split("-"), pair[1].split("-")]

print(pairs)

sum_full_overlap = 0
sum_overlap = 0
for pair in pairs:
    set_a = set(range(int(pair[0][0]), int(pair[0][1]) + 1))
    set_b = set(range(int(pair[1][0]), int(pair[1][1]) + 1))
    if set_a.issubset(set_b) or set_b.issubset(set_a):
        sum_full_overlap += 1
    if len(set_a.intersection(set_b)) != 0:
        sum_overlap += 1

print(sum_full_overlap)
print(sum_overlap)