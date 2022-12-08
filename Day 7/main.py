def getDirSize(Dir):
    Size = 0
    for ChildDir in Directorys[Dir]["ChildDirs"]:
        Size += getDirSize(ChildDir)
    return Size + Directorys[Dir]["Size"]

Input = open("Day 7\input.txt").read().split("\n")

for i in range(len(Input)):
    Input[i] = Input[i].split(" ")

print(Input)

Directorys = {}
Files = []
ChildDirs = []
CurrentPath = ""

for Line in Input:
    print(CurrentPath)
    if Line[0] == "$":  
        if Line[1] == "cd" and Line[2] == "..":
            CurrentPath = CurrentPath[:CurrentPath.rindex("/")]

        elif Line[1] == "cd":
            if CurrentPath != "":
                CurrentPath += f"/{Line[2]}"
            else:
                CurrentPath = Line[2]

        elif Line[1] == "ls":
            Files = []
            ChildDirs = []

    elif Line[0].isdigit():
        if CurrentPath in Directorys:
            Directorys[CurrentPath]["Size"] += int(Line[0])
        else:
            Directorys[CurrentPath] = {"ChildDirs" : [], "Size" : int(Line[0])}
    elif Line[0] == "dir":
        if CurrentPath in Directorys:
            Directorys[CurrentPath]["ChildDirs"].append(CurrentPath + f"/{Line[1]}")
        else:
            Directorys[CurrentPath] = {"ChildDirs" : [CurrentPath + f"/{Line[1]}"], "Size" : 0}


print(Directorys)

Sum = 0
for Directory in Directorys:
    Size = getDirSize(Directory)
    if Size <= 100000:
        Sum += Size

print(f"Sum of Dirs < 100000: {Sum}")

UnusedSpace = 70000000 - getDirSize("/")
print(f"Unused Disk-Space: {UnusedSpace}")
RequiredDeletion = 30000000 - UnusedSpace
print(f"Total Filesize to delete required for update: {RequiredDeletion}")

DirsAvailforDel = []
for Directory in Directorys:
    Size = getDirSize(Directory)
    if Size > RequiredDeletion:
        DirsAvailforDel.append(Size)
DirsAvailforDel.sort()

print(f"Smallest Dir big enough for update: {DirsAvailforDel[0]}")