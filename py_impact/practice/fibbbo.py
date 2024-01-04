def fib0(n):# fibbonacci series 
    a=0
    b=1
    while a<n:
        print(a,end=' ')
        a,b=b,a+b
    print()

fib0(2000)