
prod = 1
for n in range(1, 101):
    prod *= n

# The answer is 648
print(sum(int(c) for c in str(prod)))
