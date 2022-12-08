list = open("Day 2\input.txt").read().split("\n")
for i in range(len(list)):
    list[i] = list[i].split()
print(list)

score = 0
for i in range(len(list)):
    match list[i]:
        case ["A", "X"]: #Stein vs Stein; 1 + 3
            score += 4
        case ["A", "Y"]: #Stein vs Papier; 2 + 6
            score += 8
        case ["A", "Z"]: #Stein vs Schere; 3 + 0
            score += 3
        case ["B", "X"]: #Papier vs Stein; 1 + 0
            score += 1
        case ["B", "Y"]: #Papier vs Papier; 2 + 3
            score += 5
        case ["B", "Z"]: #Papier vs Schere; 3 + 6
            score += 9
        case ["C", "X"]: #Schere vs Stein; 1 + 6
            score += 7
        case ["C", "Y"]: #Schere vs Papier; 2 + 0
            score += 2
        case ["C", "Z"]: #Schere vs Schere; 3 + 3
            score += 6

print(f"\nScore: {score}")

secret_score = 0
for i in range(len(list)):
    match list[i]:
        case ["A", "X"]: #Stein vs Schere; 3 + 0
            secret_score += 3
        case ["A", "Y"]: #Stein vs Stein; 1 + 3
            secret_score += 4
        case ["A", "Z"]: #Stein vs Papier; 2 + 6
            secret_score += 8
        case ["B", "X"]: #Papier vs Stein; 1 + 0
            secret_score += 1
        case ["B", "Y"]: #Papier vs Papier; 2 + 3
            secret_score += 5
        case ["B", "Z"]: #Papier vs Schere; 3 + 6
            secret_score += 9
        case ["C", "X"]: #Schere vs Papier; 2 + 0
            secret_score += 2
        case ["C", "Y"]: #Schere vs Schere; 3 + 3
            secret_score += 6
        case ["C", "Z"]: #Schere vs Stein; 1 + 6
            secret_score += 7

print(f"SecretScore: {secret_score}")