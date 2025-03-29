def josephus(n, m):
    circle = list(range(1, n + 1))
    index = 0
    while len(circle) > 1:
        index = (index + m - 1) % len(circle)
        circle.pop(index)
    return circle[0]
n = int(input("Enter the number of persons in the circle: "))
m = int(input("Enter the elimination count: "))
print("Input:", n, m)
print("Output:", josephus(n, m))
