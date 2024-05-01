import sys
def fibonacci(n):
    fibonaccis = [0,1,1]
    while len(fibonaccis) <= n:
        fibonaccis.append(fibonaccis[-1]+fibonaccis[-2])
    return fibonaccis[n]
def fibonacci_digits(number_of_digits):
    fibonaccis = [0,1,1]
    while num_digits(fibonaccis[-1]) < number_of_digits:
        fibonaccis.append(fibonaccis[-1]+fibonaccis[-2])
    print(f'{len(fibonaccis)-1=}')
    return fibonaccis[-1]
def num_digits(n):
    i = 0
    while n != 0:
        i +=1
        n = n // 10
    return i
if __name__ == '__main__':
    #nth = int(sys.argv[1])
    #print(fibonacci(nth))
    bog_num = fibonacci_digits(1000)
    print(f'{bog_num=}, {num_digits(bog_num)=}')
    #print(f'\n {num_digits(99)=}')
