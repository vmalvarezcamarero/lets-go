

series = [0, 1, 1]

a = 1
b = 1

for e in range (0, 11):
    f = b + a
    series.append(f)
    a = b
    b = f
    print(series[e], end=" ")
