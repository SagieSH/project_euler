
DIGITS = {
    0: 0,
    1: len("one"),
    2: len("two"),
    3: len("three"),
    4: len("four"),
    5: len("five"),
    6: len("six"),
    7: len("seven"),
    8: len("eight"),
    9: len("nine"),
    10: len("ten"),
    11: len("eleven"),
    12: len("twelve"),
    13: len("thirteen"),
    14: len("fourteen"),
    15: len("fifteen"),
    16: len("sixteen"),
    17: len("seventeen"),
    18: len("eighteen"),
    19: len("nineteen")
}
TENS = {
    2: len("twenty"),
    3: len("thirty"),
    4: len("forty"),
    5: len("fifty"),
    6: len("sixty"),
    7: len("seventy"),
    8: len("eighty"),
    9: len("ninety")
}


def letter_count(num):
    counter = 0
    if num == 1000:
        return len("one") + len("thousand")
    if num >= 100:
        counter += DIGITS[num // 100] + len("hundred")
        if num % 100 != 0:
            counter += len("and")
    num %= 100
    if num >= 20:
        counter += TENS[num // 10]
        num = num % 10
    counter += DIGITS[num]
    return counter


result = 0
for n in range(1, 1001):
    lc = letter_count(n)
    result += lc
    print(n, lc)

# The answer is 21124
print(result)
