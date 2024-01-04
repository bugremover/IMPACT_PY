'''def printime(str11,values1,values2):
    print(str11)
    print(values1)
    print(values2)
    return 10#if we didnt assigned anything then it will be none
print(type(printime("hello",[1,2,3],(1,2))))
#<class 'int'>
'''
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

        
             
        
            