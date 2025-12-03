# it's slow as crap but hey it works

with open("input/day2.txt") as file:
    ranges = file.read().split(",")

invalid = []
invalid2 = []
for r in ranges:
    min, max = list(map(int, r.split("-")))
    for i in range(min, max + 1):
        s = str(i)
        if len(s) % 2 == 0:
            mid = len(s) // 2
            first = s[:mid]
            second = s[mid:]
            if second == first:
                invalid.append(i)

        for length in range(1, len(s)):
            k = len(s) // length
            part = None
            is_invalid = True
            for j in range(0, len(s), length):
                if part is None:
                    part = s[j:j + length]
                is_invalid = s[j:j + length] == part and is_invalid

            if is_invalid:
                invalid2.append(i)
                break


print(sum(invalid))
print(sum(invalid2))
