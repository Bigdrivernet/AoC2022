def get_dir_size(dir):
    size = 0
    for child_dir in directorys[dir]["ChildDirs"]:
        size += get_dir_size(child_dir)
    return size + directorys[dir]["Size"]

input = open("Day 7\input.txt").read().split("\n")

for i in range(len(input)):
    input[i] = input[i].split(" ")

print(input)

directorys = {}
files = []
child_dirs = []
current_path = ""

for line in input:
    print(current_path)
    if line[0] == "$":  
        if line[1] == "cd" and line[2] == "..":
            current_path = current_path[:current_path.rindex("/")]

        elif line[1] == "cd":
            if current_path != "":
                current_path += f"/{line[2]}"
            else:
                current_path = line[2]

        elif line[1] == "ls":
            files = []
            child_dirs = []

    elif line[0].isdigit():
        if current_path in directorys:
            directorys[current_path]["Size"] += int(line[0])
        else:
            directorys[current_path] = {"ChildDirs" : [], "Size" : int(line[0])}
    elif line[0] == "dir":
        if current_path in directorys:
            directorys[current_path]["ChildDirs"].append(current_path + f"/{line[1]}")
        else:
            directorys[current_path] = {"ChildDirs" : [current_path + f"/{line[1]}"], "Size" : 0}


print(directorys)

sum = 0
for directory in directorys:
    size = get_dir_size(directory)
    if size <= 100000:
        sum += size

print(f"Sum of Dirs < 100000: {sum}")

unused_space = 70000000 - get_dir_size("/")
print(f"Unused Disk-Space: {unused_space}")
required_deletion = 30000000 - unused_space
print(f"Total Filesize to delete required for update: {required_deletion}")

dirs_avail_for_deletion = []
for directory in directorys:
    size = get_dir_size(directory)
    if size > required_deletion:
        dirs_avail_for_deletion.append(size)
dirs_avail_for_deletion.sort()

print(f"Smallest Dir big enough for update: {dirs_avail_for_deletion[0]}")