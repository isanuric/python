
with open("input.txt") as f:
    lines = f.read().splitlines() 

ll = sorted(lines, key=len, reverse=True)

for l in ll:
    print(l)