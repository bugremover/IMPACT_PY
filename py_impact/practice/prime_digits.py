l=[2,3,5,7]
count=4
n=11
for i in range(0,n+1):
    for j in range(0,4):
        if count >=n:
            break
        l.append(l[i]*10+l[j])
        count +=1
print(l)