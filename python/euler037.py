from utils.number_theory import get_prime_list

SIZE = 10**7


primes = get_prime_list(limit=SIZE, get_as_boolean_list=True)
left_primes = [False] * SIZE
right_primes = [False] * SIZE
left_and_right_primes = []


def is_left_prime(num):
    if not primes[num]:
        return False
    
    if not left_primes[int(str(num)[:-1])]:
        return False
    
    left_primes[num] = True
    return True

    
def is_right_prime(num):
    if not primes[num]:
        return False
    
    if not right_primes[int(str(num)[1:])]:
        return False
    
    right_primes[num] = True
    return True


def is_left_right_primt(num):
    # important to get both becuase the caching happens inside the functions.
    left = is_left_prime(num)
    right = is_right_prime(num)
    
    return left and right


def main():
    found = 0

    for num in range(SIZE):
        if len(str(num)) == 1:
            if primes[num]:
                left_primes[num] = True
                right_primes[num] = True
        elif is_left_right_primt(num):
                left_and_right_primes.append(num)
                found += 1
        
        if found == 11:
            break
    
    print(f"All left and right: {left_and_right_primes}")
    print(f"There are {len(left_and_right_primes)} of them overall.")
    print(f"The sum is: {sum(left_and_right_primes)}")



if __name__ == '__main__':
    main()
