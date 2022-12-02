List = open("Day 2\input.txt").read().split("\n")
for i in range(len(List)):
    List[i] = List[i].split()
print(List)

Score = 0
for i in range(len(List)):
    match List[i]:
        case ["A", "X"]: #Stein vs Stein; 1 + 3
            Score += 4
        case ["A", "Y"]: #Stein vs Papier; 2 + 6
            Score += 8
        case ["A", "Z"]: #Stein vs Schere; 3 + 0
            Score += 3
        case ["B", "X"]: #Papier vs Stein; 1 + 0
            Score += 1
        case ["B", "Y"]: #Papier vs Papier; 2 + 3
            Score += 5
        case ["B", "Z"]: #Papier vs Schere; 3 + 6
            Score += 9
        case ["C", "X"]: #Schere vs Stein; 1 + 6
            Score += 7
        case ["C", "Y"]: #Schere vs Papier; 2 + 0
            Score += 2
        case ["C", "Z"]: #Schere vs Schere; 3 + 3
            Score += 6

print(f"\nScore: {Score}")

SecretScore = 0
for i in range(len(List)):
    match List[i]:
        case ["A", "X"]: #Stein vs Schere; 3 + 0
            SecretScore += 3
        case ["A", "Y"]: #Stein vs Stein; 1 + 3
            SecretScore += 4
        case ["A", "Z"]: #Stein vs Papier; 2 + 6
            SecretScore += 8
        case ["B", "X"]: #Papier vs Stein; 1 + 0
            SecretScore += 1
        case ["B", "Y"]: #Papier vs Papier; 2 + 3
            SecretScore += 5
        case ["B", "Z"]: #Papier vs Schere; 3 + 6
            SecretScore += 9
        case ["C", "X"]: #Schere vs Papier; 2 + 0
            SecretScore += 2
        case ["C", "Y"]: #Schere vs Schere; 3 + 3
            SecretScore += 6
        case ["C", "Z"]: #Schere vs Stein; 1 + 6
            SecretScore += 7

print(f"SecretScore: {SecretScore}")