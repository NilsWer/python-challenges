def fib1(n):
    # performant
    zähler = 1
    i = 1
    fib = 0
    while zähler <= n:
        t = fib
        fib = i
        i = t + i
        zähler += 1
    return fib

def fib2(n):
    #nice code
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib2(n-1) + fib2(n-2)


def fib(n):
    # This function only calls the up-to-date-function (fib1(), fib2(), ... )
    return fib1(n)
"""
for i in range(2, 51):
    percent = fib(i)/fib(i-1)*100
    print("{:2}. Zahl ist {:11} und entspricht {:18}% des Vorgängers".format(i, fib(i), percent))
"""

