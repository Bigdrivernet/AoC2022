Forest = open("Day 8\input.txt").read().split("\n")

TreesVisible = 0

for i in range(len(Forest)):
    for j in range(len(Forest[0])):
        Tree = int(Forest[i][j])
        MaxTrees = [-1, -1, -1, -1] #Top, Right, Bottom, Left
        upper = []
        lower = []
        for n in range(i):
            upper.append(Forest[n][j])
        for n in range(i+1, len(Forest)):
            lower.append(Forest[n][j])
        
        Top = set(upper)
        if not len(Top) == 0:
            MaxTrees[0] = int(max(Top))
        Right = set(set(Forest[i][j+1:]))
        if not len(Right) == 0:
            MaxTrees[1] = int(max(Right))
        Bottom = set(lower)
        if not len(Bottom) == 0:
            MaxTrees[2] = int(max(Bottom))
        Left = set(set(Forest[i][:j]))
        if not len(Left) == 0:
            MaxTrees[3] = int(max(Left))
        
        for MaxTree in MaxTrees:
            if MaxTree < Tree:
                TreesVisible += 1
                break

print(TreesVisible)

ScenicScores = []

for i in range(len(Forest)):
    for j in range(len(Forest[0])):
        Tree = int(Forest[i][j])
        ScenicTop = 0
        ScenicRight = 0
        ScenicBottom = 0
        ScenicLeft = 0
        for n in reversed(range(i)):
            ScenicTop += 1
            if int(Forest[n][j]) >= Tree:
                break
        for CurrentTree in Forest[i][j+1:]:
            ScenicRight += 1
            if int(CurrentTree) >= Tree:
                break
        for n in range(i + 1, len(Forest)):
            ScenicBottom += 1
            if int(Forest[n][j]) >= Tree:
                break
        for CurrentTree in reversed(Forest[i][:j]):
            ScenicLeft += 1
            if int(CurrentTree) >= Tree:
                break
        ScenicScores.append(ScenicTop * ScenicRight * ScenicBottom * ScenicLeft)

print(max(ScenicScores))