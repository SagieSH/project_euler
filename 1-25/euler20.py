
from functools import reduce


prod = reduce(lambda x, y: x*y, range(1, 101))

# The answer is 648
print(reduce((lambda c1, c2: int(c1) + int(c2)), str(prod)))
