from utils import minimize_fraction


numerator_product = 1
denominator_product = 1
for x in range(100, 1000):
    big_numerator, big_denominator = x // 10, x % 100
    small_numerator, small_denominator = x // 100, x % 10
    try:
        if (big_numerator != big_denominator) and (
                (big_numerator / big_denominator) == (small_numerator / small_denominator)):
            numerator_product *= small_numerator
            denominator_product *= small_denominator
    except ZeroDivisionError:
        pass

# The answer is: 100
print(minimize_fraction(numerator_product, denominator_product)[1])
