
def is_palindrome(s):
    return s == s[::-1]


max_palindrome = 0
for a in range(100, 1000):
    for b in range(100, 1000):
        prod = a * b
        if is_palindrome(str(prod)) and prod > max_palindrome:
            max_palindrome = prod

# The answer if 906609
print(max_palindrome)
