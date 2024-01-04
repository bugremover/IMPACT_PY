
def printLeaders(arr, size):
	
	maxvalue = arr[size-1] 
	print (maxvalue,end=' ') 
	#indexing from rightside so ...i took -1
	for i in range( size-2, -1, -1):	 
		if maxvalue < arr[i]:	 
			print (arr[i],end=' ')
			maxvalue = arr[i]
'''
def leaders( A, N):
        result= []
        maxvalue=A[N-1]
        result.append(maxvalue)
        #print(maxvalue,end=' ')
        for i in range(N-2,-1,-1):
            if A[i]>maxvalue:
                result.append(A[i])
                maxvalue=A[i]
        return result[::-1]
        
'''		

print("Size of the array:")
n=int(input())
list1=[]
for i in range(0,n):
	t=int(input())
	list1.append(t)
printLeaders(list1,n)
