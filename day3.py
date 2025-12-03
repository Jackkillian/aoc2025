joltages = []
high_joltages = []

for bank in open("input/day3.txt"):
    init_vals = list(map(int, bank[:-1]))
    vals = init_vals[:]
    max_ = max(vals)
    index = vals.index(max_)
    if index == len(vals) - 1:
        max_2 = max_
        vals.remove(max_)
        max_ = max(vals)
    else:
        max_2 = max(vals[index + 1:])

    joltages.append(int(f"{max_}{max_2}"))

    batts = 12
    high = []
    available = init_vals[:]
    for i in range(0, 12):
        limit = -batts + i + 1
        end = len(available) + limit
        if len(available[:-batts + i + 1]) == 0:
            # very hacky quick fix because it's 2am and my brain is dead
            num = max(available)
        else:
            num = max(available[:-batts + i + 1])
        index = available.index(num)

        high.append(str(num))
        available = available[index + 1:]
    high_joltages.append(int("".join(high)))

print(sum(joltages))
print(sum(high_joltages))
