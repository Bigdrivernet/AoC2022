forest = open("Day 8\input.txt").read().split("\n")

trees_visible = 0

for i in range(len(forest)):
    for j in range(len(forest[0])):
        tree = int(forest[i][j])
        max_trees = [-1, -1, -1, -1] #Top, Right, Bottom, Left
        upper = []
        lower = []
        for n in range(i):
            upper.append(forest[n][j])
        for n in range(i+1, len(forest)):
            lower.append(forest[n][j])
        
        top = set(upper)
        if not len(top) == 0:
            max_trees[0] = int(max(top))
        right = set(set(forest[i][j+1:]))
        if not len(right) == 0:
            max_trees[1] = int(max(right))
        bottom = set(lower)
        if not len(bottom) == 0:
            max_trees[2] = int(max(bottom))
        left = set(set(forest[i][:j]))
        if not len(left) == 0:
            max_trees[3] = int(max(left))
        
        for max_tree in max_trees:
            if max_tree < tree:
                trees_visible += 1
                break

print(trees_visible)

scenic_scores = []

for i in range(len(forest)):
    for j in range(len(forest[0])):
        tree = int(forest[i][j])
        scenic_top = 0
        scenic_right = 0
        scenic_bottom = 0
        scenic_left = 0
        for n in reversed(range(i)):
            scenic_top += 1
            if int(forest[n][j]) >= tree:
                break
        for current_tree in forest[i][j+1:]:
            scenic_right += 1
            if int(current_tree) >= tree:
                break
        for n in range(i + 1, len(forest)):
            scenic_bottom += 1
            if int(forest[n][j]) >= tree:
                break
        for current_tree in reversed(forest[i][:j]):
            scenic_left += 1
            if int(current_tree) >= tree:
                break
        scenic_scores.append(scenic_top * scenic_right * scenic_bottom * scenic_left)

print(max(scenic_scores))