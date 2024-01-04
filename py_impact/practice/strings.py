str1="Hello"
str2="vardhan, good boy"
print(str1*4)
print(str1+str2)
print(str1[4])
print(str1[2:7])
print('h' in str1)
print(r'hello harsha\n')
print("the string is str1:%s"%(str1))
print(len(str1))#len should be applied on an object
print(str1.upper())
#print(str1.len())// str has no attribute 'len'
#split-it will split a string and added into an array:
l1=str2.split(',') # it will be  split after , ['vardhan', ' good boy']
print(l1)
#a,b=input()
'''Exception has occurred: ValueError
too many values to unpack (expected 2)
  File "C:\Users\harsha\Desktop\py_impact\strings.py", line 16, in <module>
    a,b=input()
ValueError: too many values to unpack (expected 2)
value error: 
'''
str1=r'hello \n world'
list=str1.split(" ")
print(list)
#print(a,b)


