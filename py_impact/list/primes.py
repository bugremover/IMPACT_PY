n=range(1,100)
def is_prime(n):
    for i in range(2,n):
        if (i%n)==0:
            return False
    return True
primes=list(filter(is_prime,n))
#print(primes)
print(primes[10])