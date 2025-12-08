data = open("input/day4.txt").read().split("\n")

line_len = len(data[0])
data.insert(0, "."*line_len)
data.append("."*line_len)

for i, line in enumerate(data):
    data[i] = f".{line}."

def modify_char(c, s, i):
    return s[:i] + c + s[i+1:]

def remove_rolls(data, one_iter=False):
    accessible = 0
    to_remove = []
    for i in range(1, len(data) - 1):
        for j in range(0, len(data[0])):
            top = data[i - 1][j - 1:j+2].count("@")
            mid = data[i][j - 1:j+2:2].count("@")
            bottom = data[i + 1][j - 1:j+2].count("@")
            total = sum([top, mid, bottom])

            if data[i][j] == "@":
                if total < 4:
                    accessible += 1
                    to_remove.append((i, j))

    if one_iter:
        return accessible

    for v in to_remove:
        s = data[v[0]]
        s = modify_char(".", s, v[1])
        data[v[0]] = s

    if accessible != 0:
        return remove_rolls(data) + accessible
    return 0

result1 = remove_rolls(data, True)
result2 = remove_rolls(data)

print(result1)
print(result2)
