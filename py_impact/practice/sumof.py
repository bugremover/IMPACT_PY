lst=[]
n=int(input())
if n==-1:
    print("-1")
for i in range (1,n+1):
    count=0
    for j in range(1,i+1):
        if i%j==0:
            count=count+1
    if count ==2:
        lst.append(i)

#print(lst)
#kadane algo
count =0
for i in range(0,len(lst)):
    for j in range(i,len(lst)):
        if lst[i]+lst[j] == n:
            print(n,"=",lst[i],"+",lst[j])
            count=count+1
print("No of WayS:",count)