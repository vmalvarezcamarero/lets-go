def g(a, b):
    return a - b


def f(a, b, c, d):
    t0 = a + b - g(a, 0)
    t1 = g(c, d)
    try:
        t3 = 2 * (t0 / t1)
        return t0 + 2*t1 + t3*t3
    except ZeroDivisionError:
        return "You cant divide a number by 0"


# -- Main program
print("Result 1: ", f(5, 2, 5, 0))
print("Result 2: ", f(0, 2, 3, 3))
print("Result 3: ", f(1, 3, 2, 3))
print("Result 4: ", f(1, 9, 22.0, 3))


l = input("Give a genome sequence: ")
def count(l):
    a = l.count("A")
    c = l.count("C")
    t = l.count("T")
    g = l.count("G")
    totalcount= a+c+t+g
    return totalcount,a,c,t,g

print("The total number of lrtters is ", str(count(l)[0]))
print("A : ", str(count(l)[1]))
print("C : ", str(count(l)[2]))
print("T : ", str(count(l)[3]))
print("G : ", str(count(l)[4]))

