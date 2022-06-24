
result = 1
last_number = 1
for square in range(1, 501):
    for _ in range(4):
        last_number += (2 * square)
        result += last_number

# The answer is 669171001
print(result)
