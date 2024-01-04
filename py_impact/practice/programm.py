str1='''
this is harsha vardhan
i am a developer'''
# to add multiple strings
#to check type of datatype we use type(variable name
print(type(str1))  #output: <class 'str'>
#concatenating two string using + operator
#in -gives true if value is present in datastructure
#not in - gives true if value is not present in the data structure. 
print(id(str1))
a=123
print(id(a))
print(id(a),end="\t")
print(id(str1))
if "developer" in str1:   #checks whether substring is there or not
    print("sub-string is present")
else:
    print("sub-string is not present")

print(a,str1,sep="+++",end="=>")
list=[1,2,3,4]
#for loop
for i in list:
    print(i)
#for(num1:list){
    #System.out.println(num1);}

#iden
num1=153
orginial =num1
sum=0
while num1>0:
    num2=num1%10
    #result=num2*num2*num2
    sum=sum+num2*num2*num2
    num1//=10
if sum==orginial:
    print("true")
else:
    print("false")
