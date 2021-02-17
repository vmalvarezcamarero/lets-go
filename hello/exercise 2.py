def fibonacci(n):
    series = [0, 1, 1]
    a = 1
    b = 1

    for e in range(0, n - 2):
        f = b + a
        series.append(f)
        a = b
        b = f
    return series

print("5th Fibonacci number:  ", sum(fibonacci(5)))
print("10th Fibonacci number:  ", sum(fibonacci(10)))
