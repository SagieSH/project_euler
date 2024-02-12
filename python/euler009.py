
result = 0
for a in range(1, 1000):
    for b in range(a + 1, 1000 - a):
        c = 1000 - a - b
        if (a ** 2) + (b ** 2) == (c ** 2):
            print(a, b, c)
            result = a * b * c

# The answer is 31875000
print(result)
