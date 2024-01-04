def func(num):
    return num**2
l=[1,2,3,4]
l2=[]
for i in l:
    t=func(i)
    l2.append(t)
l2=map(func,l)
print(list(l2))


l3=['1','2','3','4']
print(type(l3))
print(l3)
l4=list(map(int,l3))
print(l4)