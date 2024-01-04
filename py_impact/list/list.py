'''
l1=[1,2,3,56,0,34,78,555,11]
#e=l1.sort()#
l1.sort(reverse=True)# u cant print this directly..u will get none
print(l1)#print the reverse
#sort method will permanently applied on list
print(id(l1))
'''
#for checking duplicate values

num=[1,2,34,5,6,7,8,2,3,4]
cnt=num.count(2)
print(cnt)