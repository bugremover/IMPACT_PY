def modify_string(str1,str2):
    set_s1=set(str1)
    set_s2=set(str2)
    uncommon_s1=set_s1-set_s2
    uncommon_s2=set_s2-set_s1
    new_string=''.join(list(uncommon_s1)+list(uncommon_s2))
    return new_string

str1="gafd"
str2="aacdb"
result=modify_string(str1,str2)
print(result)
'''
Problem statement: Given two strings s1 and s2. 
Modify string s1 such that all the common ccharacters of s1 and s2 is to be removed 
and the uncommon characters of s1 and s2 is to be concatenated.


'''