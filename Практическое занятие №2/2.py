import time
start = time.time()
def fib(n):
    if n <= 1:
        return n

    previousFib = 0
    currentFib = 1

    for i in range(n-1):
        newFib = previousFib + currentFib
        previousFib = currentFib
        currentFib = newFib
    return currentFib

if __name__ == '__main__':
    n = 5000
    print ('fib(n) =', fib(n))

end = time.time()
print ('Время, потраченное на выполнение программы =', end-start)