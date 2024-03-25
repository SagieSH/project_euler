from utils.number_theory import get_prime_list

LIMIT = 10 ** 6
is_prime = get_prime_list(limit=LIMIT, get_as_boolean_list=True)

def num_rotations(num):
    num_str = str(num)
    num_len = len(num_str)
    for i in range(num_len):
        yield int(num_str)
        num_str = num_str[1:] + num_str[0]


def is_circular_prime(p):
    rotator = num_rotations(p)
    for rotation in rotator:
        if not is_prime[rotation]:
            return False
    return True


def main():
    circular_primes = list()
    for num in range(LIMIT):
        if is_circular_prime(num):
            circular_primes.append(num)

    # The answer is 55
    print(circular_primes)
    print(len(circular_primes))


if __name__ == '__main__':
    main()
