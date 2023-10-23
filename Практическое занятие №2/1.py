import time
start = time.time()
def Fib(n):
    if n <= 1:
        return n

    return Fib(n-1)+Fib(n-2)

if __name__ == '__main__':
    n = 40
    print ('Fib(n) =', Fib(n))

end = time.time()
print ('Время, потраченное на выполнение программы =', end-start)
