n=int(input())
b=""
summ=0
for i in range(1,n+1):
    b=b+'3'*i
    summ=summ+int(b)
    b=''
print(summ)
'''
n=6
x=3
s=0
sum=0
for i in range(0,n):
    s=x+s*10
    sum+=s
    print(s)
print(sum)
'''