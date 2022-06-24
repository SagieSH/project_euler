import time

LIMIT = 10000
is_prime_lst = [None] * LIMIT * 10000
primes = []
pairs = []


def is_prime(n):
    global is_prime_lst, primes

    if n < len(is_prime_lst) and (is_prime_lst[n] is not None):
        return is_prime_lst[n]

    i = 2
    while i * i <= n:
        if n % i == 0:
            # is_prime_lst[n] = False
            return False
        i += 1

    # is_prime_lst[n] = True
    return True


def fill_is_prime_lst():
    global is_prime_lst, primes

    is_prime_lst[0] = False
    is_prime_lst[1] = False

    p = 2
    while p is not None:
        is_prime_lst[p] = True

        if p < LIMIT:
            primes.append(p)

        n = 2

        while n * p < len(is_prime_lst):
            is_prime_lst[n * p] = False
            n += 1
        try:
            p = is_prime_lst.index(None, p)
        except Exception:
            p = None


def concatenate_integers(a, b):
    return int(str(a) + str(b))


def sort_pair(pair):
    a, b = pair
    if a <= b:
        return a, b
    return b, a


def is_pair_magniv(a, b, check_in_lst=False):
    if check_in_lst:
        print('here')
        return sort_pair((a, b)) in pairs
    # a, b = pair
    return is_prime(concatenate_integers(a, b)) and \
           is_prime(concatenate_integers(b, a))


def is_triplet_magniv(pair, c):
    a, b = pair
    return is_pair_magniv(a, c) and is_pair_magniv(b, c)


def is_quad_magniv(triplet, d):
    a, b, c = triplet
    return is_pair_magniv(a, d) and is_pair_magniv(b, d) and is_pair_magniv(c, d)


def is_quint_magniv(quad, e):
    a, b, c, d = quad
    return is_pair_magniv(a, e) and is_pair_magniv(b, e) and \
           is_pair_magniv(c, e) and is_pair_magniv(d, e)


def main():
    global pairs

    start_time = time.time()
    print(f'Checking for a 5-mganiv group with a limit of: {LIMIT}')

    fill_is_prime_lst()

    print("generated primes:", len(primes))

    triplets = []
    quadros = []
    quints = []

    for index, prime1 in enumerate(primes):
        for prime2 in primes[index:]:
            if is_pair_magniv(prime1, prime2):
                pairs.append((prime1, prime2))

    print('finished pairs:', len(pairs))

    for prime in primes:
        for pair in pairs:
            if not (pair[0] < pair[1] < prime):
                continue
            if is_triplet_magniv(pair, prime):
                triplets.append((*pair, prime))

    print('finished triplets:', len(triplets))

    for prime in primes:
        for triplet in triplets:
            if not (triplet[0] < triplet[1] < triplet[2] < prime):
                continue
            if is_quad_magniv(triplet, prime):
                quadros.append((*triplet, prime))

    print('finished quadros:', len(quadros))

    min_quint_sum = 100000000
    min_quint = ()
    for prime in primes:
        for quad in quadros:
            if not (quad[0] < quad[1] < quad[2] < quad[3] < prime):
                continue
            if is_quint_magniv(quad, prime):
                current_quint = (*quad, prime)
                quints.append(current_quint)
                if sum(current_quint) < min_quint_sum:
                    min_quint_sum = sum(current_quint)
                    min_quint = current_quint

    print('finished quints:', len(quints))

    # The answer is 26033
    print(f'Best quint: {min_quint}. With the sum: {min_quint_sum}')

    end_time = time.time()
    print('Overall time is:', end_time - start_time)


if __name__ == '__main__':
    main()
