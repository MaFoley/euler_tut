import sys
def prime_sieve(ceiling):
    primes = [1 for x in range(ceiling+1)]
    return_list = list()
    primes[0],primes[1] = 0,0
    for p, is_prime in enumerate(primes):
        if is_prime == 0:
            continue
        #p is primes, mark all multiples as composite
        return_list.append(p)
        i = 2
        while(i*p <= ceiling):
            primes[i*p] = 0
            i += 1
    return return_list
if __name__ == '__main__':
    ceiling = int(sys.argv[1])
    primes = prime_sieve(ceiling)
    print(f'{primes=} {len(primes)=}')
