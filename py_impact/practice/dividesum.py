lst=[]
n=int(input())
for i in range(1,n):
    lst.append(i)
#print(lst)
count=0
for i in range(0,len(lst)):
    for j in range(i,len(lst)):
        for k in range(j,len(lst)):
            for m in range(k,len(lst)):
                if lst[i]+lst[j]+lst[k]+lst[m] == n:
                    print(lst[i],"+",lst[j],"+",lst[k],"+",lst[m])
                    count=count+1
print("No of ways:",count)