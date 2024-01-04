print("Enter the size of list:")
n=int(input())
#print("Enter kth element to rotate:")
k=int(input())
list1=[]
list2=[]
for i in range(1,n+1):
    list1.append(i)
print(list1)
start=0
end=k-1
print(list1[start])
print(list1[end])
for i in range(start,end+1):
    list2.append(list1[i])
    list2.sort(reverse=True)
    start=end
    end=k+3
print(list2)


    