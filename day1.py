password = 0
dial = 50

for line in open("input/day1.txt"):
    dir = (-1 if line[0] == "L" else 1)
    steps = int(line[1:])

    for i in range(steps):
        dial = (dial + dir) % 100
        if dial == 0:
            password += 1

print(f"Password is {password}")
