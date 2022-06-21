
def is_prime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def is_goldbach(n):
    if n % 2 == 0:
        return True
    a = 0
    sq_2 = 2 * a * a
    while sq_2 < n:
        if is_prime(n - sq_2):
            return True
        a += 1
        sq_2 = 2 * a * a
    return False


def find_smallest_non_goldbach():
    n = 1
    while is_goldbach(n):
        n += 1
        if n % 1000 == 0:
            print(n)
    return n


if __name__ == '__main__':
    print(find_smallest_non_goldbach())
