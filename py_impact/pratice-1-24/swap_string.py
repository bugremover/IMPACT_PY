'''2.Reverse a given line along with the words in the line.
i/p:
This is C programm
o/p: margoP C si shiT'''
str11=str(input())
#print(str11)
list1=[]
for i in str11:
    list1.append(i)
#print(list1)
comma='.'

list2=list1[::-1]
#print(list2)
#print(list2)
#it will check the sentence has any comma at end.
#after reversing the string the comma will come at first
#so i removed it from 0th loc and added in atlast
#case 1- space before comma
if list2[1] ==' ':
    list2.remove(' ')
    list2.append(' ')
#case 2- if comma is present in string
if list2[0]==comma:
    list2.remove(comma)
    list2.append(comma)
    
str12=''.join((list2))
print(str12)
'''str13=str12.split()
print(str13)
for i in str13:
    i=i[::-1]

print(str13)'''

