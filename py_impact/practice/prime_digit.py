prime_list = [2, 3, 5, 7]
new_prime = []

for i in range(10, 10000):  
    str1 = str(i)
    
    # Check if each digit is prime
    if all(int(digit) in prime_list for digit in str1):
        new_prime.append(i)
combine=prime_list+new_prime
#print(combine[10])
n=int(input())
print(combine[n-1])

 

'''def printime(str11,values1,values2):
    print(str11)
    print(values1)
    print(values2)
    return 10#if we didnt assigned anything then it will be none
print(type(printime("hello",[1,2,3],(1,2))))
#<class 'int'>

def isprime(num):
    if num<=1:
        return False
    flag=False
    for i in range(2,int(num/2)):
        if (num % i) == 0:#if it is divided by any number then its not prime;
            flag=True
            break
    if flag==True:
        return False
    return True
'''
        
             
        
            

    