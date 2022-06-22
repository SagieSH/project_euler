
NUMBERS_PATH = "euler13_numbers.txt"


def parse_numbers():
    numbers = []
    with open(NUMBERS_PATH, 'r') as numbers_file:
        for line in numbers_file:
            if line[-1] == '\n':
                line = line[:-1]
            numbers.append(int(line))
    return numbers


result = 0
all_numbers = parse_numbers()
for number in all_numbers:
    result = (result + number)

# The answer is 5537376230
print(str(result)[:10])
