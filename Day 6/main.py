buffer = open("Day 6\input.txt").readline()

for i in range(len(buffer)):
    if len(set(buffer[i:i+4])) == 4:
        print(f"Start-of-Packet marker end: {i+4}")
        break

for i in range(len(buffer)):
    if len(set(buffer[i:i+14])) == 14:
        print(f"Start-of-Message marker end: {i+14}")
        break