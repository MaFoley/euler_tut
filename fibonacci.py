import sys
def fibonacci(n):
    fibonaccis = [0,1,1]
    while len(fibonaccis) <= n:
        fibonaccis.append(fibonaccis[-1]+fibonaccis[-2])
    return fibonaccis[n]
if __name__ == '__main__':
    nth = int(sys.argv[1])
    print(fibonacci(nth))
