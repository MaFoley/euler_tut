from euler_lib import *
import itertools
def euler_2():
    n = 0
    fib_n = 0
    sum_fib_n = 0
    while fib_n <= 4_000_000:
        if fib_n % 2 == 0:
            sum_fib_n += fib_n
        n +=1
        fib_n = fibonacci(n)
    print(f"n: {n}, fib_n: {fib_n}, sum_fib_n: {sum_fib_n}")
def euler_3():
    factorization = {}
    LCD = BIG_COMPOSITE_NUMBER
    primes = sorted(prime_sieve(10000))
    for prime in primes:
        
        while LCD % prime == 0:
            factorization[prime] = factorization.get(prime,0) + 1
            LCD = LCD // prime
            print(LCD, factorization, sep="\n")
def euler_4():
    palindromes = {}
    for x in range(900,1000):
        for y in range(900,1000):
            palindromes[x*y] = is_palindromic_number(x*y)
    candidates = {key for key in palindromes.keys() if palindromes[key] == True}
    print(sorted(candidates))
def euler_5():
    factorization = {}
    #need to build an LCD of all numbers from 1 to 20
    #step 1 build prime factorizations of all numbers
    #then take the max for each prime
    #then product them all
    for i in range(1,21):
        pf = prime_factorization(i)
        print(f"i: {i}, factors: {pf}, build_LCD: {build_LCD(pf)}")
        #compare prime factors of i to overall factorization and take higher value
        for prime in pf:
            factorization[prime] = max(factorization.get(prime,0),pf.get(prime,0))
        print(f"i: {i} current factorization: {factorization}")
    return build_LCD(factorization)
def euler_6():
    print(sum_of_squares(100))
    print(square_of_sums(100))
    print(square_of_sums(100)-sum_of_squares(100))
def euler_7():
    primes = prime_sieve(5_000_000)
    l = sorted(primes)
    print(l[10000])
def euler_9():
    primes = prime_sieve(2_000_000)
    return sum(primes)
def euler_12():
    primes = get_primes("primes_below_100MM.txt")
    for n in itertools.count(28):
        tri_n = triangle_number(n)
        factors = prime_factorization(tri_n,primes=primes)
        product = functools.reduce(lambda x,y: x*(y+1), factors.values(),1)
        if product >500:
            return print(f"{tri_n}, factored as {factors}")
def euler_14():
    index, max = 1,1
    chains = map(collatz,range(1_000_000))
    for i, chain in enumerate(chains):
        if chain > max:
            max = chain
            index = i
    print(f"{index=} {max=}")
def euler_19():
    day_of_week = 2 #Monday
    count_of_dow = {}
    for year in range(1901,2000+1):
        for month in range(1,12+1):
            for day in range(1,days_in_month(month,year)+1):
                print(f'{year=} {month=} {day=} {day_of_week=}')
                if day == 1:
                    count_of_dow[day_of_week] = count_of_dow.get(day_of_week,0) + 1
                day_of_week = day_of_week%7 +1
    print(count_of_dow)
def euler_20():
    return sum_of_digits(factorial(100))
def euler_21(ceiling):
    #sum_of_divisors(n) = sum of all divisors of a number n
    #if that sum_of_divisors also has as its sum of divisors n,
    # then they are amicable numbers
    #Find all amicable numbers < 10000
    #12: 1,2,3,4,6,12 = 28 
    #12 factorization = 2:2, 3:1
    amicable_numbers = set()
    for n in range(1,ceiling+1):
        potential_amicable = sum(get_proper_divisors(n))
        if sum(get_proper_divisors(potential_amicable)) == n and n != potential_amicable:
            amicable_numbers.add(n)
    #print(f'{sum_of_divisors[220]=} {sum_of_divisors[284]=}')
    print(f'{amicable_numbers=}')
    return sum(amicable_numbers)

def euler_26():
    #reciprocal primes. calculate the multiplicate order of 10 modulo the given prime p
    #This order always divides p-1 and there are a variety of tricks to make modular arithmetic by hand much easier
    #To show that the order of 10 mod 60013 is 5001, demonstrate 10^5001 = 1 mod 60013
    #but that 10^d != 1 for any factor of d (5001)
    #find the smallest n such that 10**n = 1 mod p. n is guaranteed to be a divisor of p-1
    primes = sorted(prime_sieve(1000))
    primes_less_1 = [p-1 for p in primes]
    divisors = [get_all_divisors(pl1) for pl1 in primes_less_1]
    periodicity = {}
    for prime, lst_of_divisors in zip(primes, divisors):
        for div in lst_of_divisors:
            if 10 **  div % prime == 1:
                periodicity[prime] = div
                break
    max = 0
    max_prime = 2
    for prime, period in periodicity.items():

        if period > max:
            max = period
            max_prime = prime
    print(f'{max_prime=} {max=}')

def euler_27():
    max = 0
    for i in range(-1000,1000+1):
        for j in range(-1000,1000+1):
            prime_list = consecutive_quadratic_primes(1,i,j)
            if max < len(prime_list):
                max = len(prime_list)
                print(f"{i=}, {j=}, {max=},{i*j}")
def euler_28():
    prime_factorizations = [prime_factorization(n) for n in range(2,100+1)]
    terms = []
    string_terms = []
    for b in range(2,100+1):
        for n in prime_factorizations:
            term = {prime: exp * b for prime, exp in n.items()}
            terms.append(term)
            string_term = '*'.join(str(k) + "exp" + str(v) 
                            for k,v in term.items()
            )
            string_terms.append(string_term)
    set_terms = set(string_terms)
    print(len(set_terms))
def euler_35():
    #circulars = [2,3,5,7,11,13,17,31,37,71,73,79,97]
    primes = prime_sieve(1_000_000)  
    circulars = [n for n in sorted(primes) if is_circular_prime(n)]
    for prime in circulars:
        print(prime)
    print(len(primes),len(circulars),sep="->")
def euler_36():
    binToDecimal = functools.partial(int,base=2)
    potential_binary_palindromes = filter(is_palindromic_number,range(1_000_000))
    binary_candidates = map(bin,potential_binary_palindromes)
    double_palindromes = filter(is_binary_palindromic_number,binary_candidates)
    decimal_palindromes = map(binToDecimal, double_palindromes)
    print(f"{sum(decimal_palindromes)=}")
def euler_37():
    primes = prime_sieve(1_000_000)
    print(is_truncatable_prime(3797))
    truncatable_primes = list(filter(is_truncatable_prime,primes))
    print(f"{truncatable_primes=},{len(truncatable_primes)=},{sum(truncatable_primes)=}")
def euler_23():
    with open("0022_names.txt") as namefile:
        csvreader = csv.reader(namefile,delimiter=',')
        names = []
        for row in csvreader:
            names.extend(row)
        
    names.sort()
    print(f"{len(names)}, {names[937:939]}")
    total_score= sum( (index + 1) * name_score(name) for index, name in enumerate(names) )
    print(f"\n {total_score=}")
def euler_30():
    fifth_powers_digits = [n for n in range(CEILING_FOR_FIFTH) if digits_to_power_sum_to_number(n,5) == n]
    print(fifth_powers_digits, sum(fifth_powers_digits),sep="\n")
def euler_33():
    print(is_digit_cancelling_fraction(49,98))
def euler_34():
    factorial_sums = []
    for n in range(10_000_000):
        if n == sum(map(math.factorial,digits_of_number(n))):
            factorial_sums.append(n)
    print(factorial_sums)
def euler_31():
    coins = [1,2,5,10,20,50,100,200]
    print(f"{make_change(10,coins)=}")
def euler_39():
    max_solutions = 0
    dict_p = {p: get_right_triangle_integer_sides(p) for p in range(12,1001)}
    for perimeter, right_triangles in dict_p.items():
        if len(right_triangles) > max_solutions:
            print(f"{perimeter=}, {len(right_triangles)=}")
            max_solutions = len(right_triangles)
SUM_OF_ABUNDANT_NUMBERS_LOWER_BOUND = 28123
def euler_23():
    abundant_numbers = list(filter(is_abundant_number,range(
        1,
        SUM_OF_ABUNDANT_NUMBERS_LOWER_BOUND)))
    
    integer_sum = (SUM_OF_ABUNDANT_NUMBERS_LOWER_BOUND + 1) * SUM_OF_ABUNDANT_NUMBERS_LOWER_BOUND // 2
    print(integer_sum)
    set_of_abundant_sums = filter(lambda x: x <= SUM_OF_ABUNDANT_NUMBERS_LOWER_BOUND
                                  ,generate_sums(abundant_numbers))
    print(integer_sum - sum(set_of_abundant_sums))
def euler_44():
    pentagonal_numbers = []
    for n in itertools.count(1):
    #for n in range(100):
        pent = pentagonal_number(n)
        
        for x in pentagonal_numbers:
            sums = pent + x
            difference = pent - x
            if is_pentagonal_number(sums) and is_pentagonal_number(difference):
                print(f"{x=} {pent=} {difference=}")
                return
        pentagonal_numbers.append(pent)
def euler_45():
    for n in itertools.count():
        tri = triangle_number(n)
        if is_hexagonal_number(tri) and is_pentagonal_number(tri):
            print(f"{n=} {tri=}")
            should_continue = input("Continue? (Y/N) ->")
            if should_continue == 'N':
                return
def euler_46():
    primes = sorted(prime_sieve(2_000_000))
    #generate odd composites
    for n in itertools.count(9,2):
        if n in primes:
            continue
        elif not goldbach_o_conjecture(n,primes):
            print(f"{n=}")
            return
        elif n % 111 == 0:
            print(f"in progress. {n=}")
def euler_47():
    primes = list(filter(lambda p: p>=1000,sorted(prime_sieve(10_000))))
    i,j = 0,0
    while i < len(primes):
        j = i + 1
        while j < len(primes):
            difference = primes[j] - primes[i]
            if all([primes[j] + difference in primes
                   ,is_permutation(primes[i],primes[j])
                   ,is_permutation(primes[i],primes[j]+difference)]):
                print(f"{primes[i]=},{primes[j]=},{primes[j] + difference=} ")
            j += 1
        i += 1
def euler_48_attempt1():
    primes = list(sorted(prime_sieve(1_000_000)))
    consecutive_summands = {}
    i,j = 0,0
    while i < len(primes):
        j = i + 1
        p = primes[i]
        while j < len(primes):
            p += primes[j]
            if p >= 1_000_000:
                break
            if p in primes:
                consecutive_summands[p] = primes[i:j+1]
                #print(f"{p=}->{primes[i:j]=}")
            j += 1
        i += 1
    max = 0
    for p, summands in consecutive_summands.items():
        if len(summands) > max:
            max = len(summands)
            print(f"{summands=} = {p}")
def euler_48_attempt2():
    primes = list(sorted(prime_sieve(1_000_000)))
    consecutive_summands = {}

    for p in primes:
        i,j = 0,1
        if p == 953:
            pass 
        for i in range(len(primes)):
            j = i+1
            sum_consecutive = primes[i]
            if sum_consecutive > p:
                break
            while j < len(primes):
                sum_consecutive += primes[j]
                if sum_consecutive > p:
                    break
                if sum_consecutive == p:
                    consecutive_summands[p] = primes[i:j+1]
                j += 1
           
            
    max = 0
    for p, summands in consecutive_summands.items():
        if len(summands) > max:
            max = len(summands)
            print(f"{len(summands)=} = {p=}")     
    print(f"{max=}")
def euler_48_attempt3():
    limit = 1_000_000
    primes = list(sorted(prime_sieve(limit)))
    consecutive_summands = {}
    for num_summands in range(2,len(primes)):
        for i in range(len(primes)-num_summands):
            sum_consecutive = sum(primes[i:i+num_summands])
            if sum_consecutive > limit:
                break
            if sum_consecutive in primes:
                consecutive_summands[sum_consecutive] = primes[i:i+num_summands]       
    max = 0
    for p, summands in consecutive_summands.items():
        if len(summands) > max:
            max = len(summands)
            print(f"{len(summands)=} = {p=}")     
    print(f"{max=}")


if __name__ == "__main__":
    euler_19()