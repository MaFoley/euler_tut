import collections
import functools
import time
import operator
import itertools
import math
BIG_COMPOSITE_NUMBER = 600_851_475_143
import string
import math
import csv
CEILING_FOR_FIFTH = 5 * 9 ** 5
def name_score(name: str) -> int:
    return sum(string.ascii_uppercase.find(char)+1 for char in name)
def digits_to_power_sum_to_number(number,exp):
    sum = 0
    if number in [0,1]:
        return None
    while number != 0:
        sum += (number % 10) ** exp
        number = number // 10
    return sum
def digits_of_number(number: int) -> list:
    digits = []
    while number != 0:
        digits.append(number % 10)
        number = number // 10
    return digits
def is_digit_cancelling_fraction(numerator, denominator):
    naive_numerator, naive_denominator = numerator // 10, denominator // 10
    return (naive_numerator/naive_denominator == numerator / denominator)
def timeit(func):
    @functools.wraps(func)
    def timeit_wrapper(*args,**kwargs):
        start_time = time.perf_counter()
        result = func(*args,**kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'{func.__name__}{args} {kwargs} Took {total_time}')
        return result
    return timeit_wrapper
#using empty dict as default on purpose. Side effect wanted for memoization
def memoized(func, _memoized_cache = {}):
    '''Decorator function to cache values'''
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if (func, args) in _memoized_cache:
            return _memoized_cache[(func, args)]
        else:
            value = func(*args, **kwargs)
            _memoized_cache[(func,args)] = value
            return value
    return wrapper
def digits_of_number(number: int) -> list:
    digits = []
    while number != 0:
        digits.append(number % 10)
        number = number // 10
    return digits
def sum_multiples():
    summation = 0
    summation = sum(x for x in range(1000) 
        if x % 3 == 0 or x % 5 == 0)
    return summation
def prime_factorization(LCD: int,*,primes=None) -> dict:
    factorization = {}
    if primes == None:
        primes = prime_sieve(LCD)
    if LCD < 2:
        return {}
    for prime in primes:
        while LCD % prime == 0:
            factorization[prime] = factorization.get(prime,0) + 1
            LCD = LCD // prime
            if LCD == 1:
                return factorization
def build_LCD(prime_facts: dict) -> int:
    result = 1
    for prime, exp in prime_facts.items():
        result *= prime ** exp
    return result
def is_palindromic_number(n: int) -> bool:
    s = str(n)
    for beg,end in zip(s,s[::-1]):
        if beg != end:
            return False
    return True
@memoized
def get_primes(filename: str) -> list:
    primes = []
    with open(filename,"r") as f:
        #cleaned_line = "".join(line.split())
        int_primes = [int(line.rstrip()) for line in f]
    return sorted(int_primes)
def triangle_number(n):
    return (n ** 2 + n)//2
def pentagonal_number(n):
    return (n * (3*n-1))//2
def is_pentagonal_number(n) -> bool:
    return math.sqrt(1+24*n) % 6 == 5
def is_hexagonal_number(n) -> bool:
    return math.sqrt(1+8*n) % 4 == 3
def hexagonal_number(n):
    return (n*(2*n-1))
@memoized
def collatz(n):
    if n in {0,1}:
        return n
    if n % 2 == 0:
        return collatz(n//2) + 1
    elif n % 2 == 1:
        return collatz(3*n + 1) + 1
@memoized
def sum_of_squares(n):
    return sum(x ** 2 for x in range(1,n+1))
@memoized
def square_of_sums(n):
    sums = (n * (n + 1)) // 2
    return sums ** 2
@timeit
@memoized
def fibonacci(n):
    #position 1 = 1
    #position 2 = 2
    #all other positions = fib(-1)+fib(-2)
    if n ==0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fibonacci(n-1)+fibonacci(n-2)
@memoized
def prime_sieve(ceiling) -> set:
    if ceiling == 0:
        return {}
    nums = [n for n in range(ceiling + 1)]
    nums[1] = 0 #unity isnt prime
    for n in nums:
        if n != 0:
            for denominator in range(2*n,ceiling+1,n):
                nums[denominator] = 0
    return set(filter(None, nums))  
def get_all_divisors(n) -> list:
    """
    returns divisors of n including itself
    """
    if n <1:
        return []
    divisors = [1]
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            divisors.append(i)
            if i != n/i:
                divisors.append(n//i)
    divisors.append(n)
    return sorted(divisors)
def get_proper_divisors(n) -> list:
    """
    returns divisors of n excluding itself
    """
    if n <1:
        return []
    divisors = [1]
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            divisors.append(i)
            if i != n/i:
                divisors.append(n//i)
    """
    returns divisors of n excluding itself
    """
    if n <1:
        return []
    divisors = [1]
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            divisors.append(i)
            if i != n/i:
                divisors.append(n//i)
    return sorted(divisors)
def is_abundant_number(n):
    return sum(get_proper_divisors(n)) > n
def is_sum_of_abundant_numbers(n:int, abundants: list) -> bool:
    for i, a in enumerate(abundants):
        for b in abundants[i:]:
            if a + b == n:
                return True
            elif a + b > n:
                break
    return False
def generate_sums(abundant_numbers) -> set:
    sums = set()
    for i, a in enumerate(abundant_numbers):
        for b in abundant_numbers[i:]:
            if (a+b) not in sums:
                sums.add(a+b)
    return sums

def consecutive_quadratic_primes(a,b,c):
    list_of_primes = []
    prime_factors = prime_sieve(2_000_000)
    for n in itertools.count():
        candidate = a*n*n + b*n + c
        if candidate in prime_factors:
            list_of_primes.append(candidate)
        else:
            break
    return list_of_primes
def squares_sieve(ceiling) -> set:
    nums = [n for n in range(ceiling + 1)]
    nums[1] = 0 #unity isnt prime
    for n in nums:
        if n != 0:
            denominators = [n ** i for i in range(2,8) if n ** i <= ceiling]
            for denominator in denominators:
                nums[denominator] = 0
    return set(filter(None, nums))   
def is_truncatable_prime(prime):
    primes = prime_sieve(1_000_000 if prime < 1_000_000 else prime)
    digits = digits_of_number(prime)
    if len(digits) == 1:
        return False #single digits aren't truncatable
    for i in range(1,len(digits)+1):
         if prime % (10 ** i) not in primes:
             return False
    while prime != 0:
        if prime not in primes:
            return False
        prime = prime // 10
    return True
def is_circular_prime(prime):
    primes = prime_sieve(1_000_000 if prime < 1_000_000 else prime)
    digits = digits_of_number(prime)
    for j in range(len(digits)):
        rotation = sum(digit * 10 ** ((i+j)%len(digits)) for i,digit in enumerate(digits))
        if rotation not in primes:
            return False
    return True
def is_binary_palindromic_number(n: str) -> bool:
    bits = n[2:]
    for beg,end in zip(bits,bits[::-1]):
        if beg != end:
            return False
    return True
#TO-DO print output of making change
def make_change(change: int, coins: list):
    if change == 0:
        return 1
    elif len(coins)<1 or change < 0:
        return 0
    else:
        return make_change(change - coins[0], coins) + make_change(change, coins[1:])
def is_right_triangle(a,b,c) -> bool:
    if 0 in [a,b,c]:
        return False
    return a**2 + b**2 == c**2
def get_right_triangle_integer_sides(perimeter) -> list:
    if perimeter < 3:
        return []
    results = []
    a = 1
    b = 1
    c = perimeter - a - b
    
    while a < c:
        while b < c:
            if is_right_triangle(a,b,c):
                results.append((a,b,c))
            b+=1
            c-=1
        a += 1
        b = a
        c = perimeter - a - b
    return results
def is_triangle_number(n):
    i = 0
    while triangle_number(i) <= n:
        if triangle_number(i) == n:
            return True
        i += 1
    return False
def goldbach_o_conjecture(n: int,primes: list) -> bool:
    
    for p in primes:
        if p > n:
            break
        for i in range(int(math.sqrt(n))):
            if p + 2*i*i == n:
                return True
    return False
def is_permutation(x,y)->bool:
    x_digits = sorted(digits_of_number(x))
    y_digits = sorted(digits_of_number(y))
    return x_digits == y_digits
if __name__ == "__main__":
    prime_sieve(1_000_000)