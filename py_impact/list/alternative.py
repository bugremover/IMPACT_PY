'''
1.alternative merge two strinngs
harsha
ABCDEF
o/p:hAaBrCsDhEaF

'''
def merge_alternatively(str1, str2):
    len1, len2 = len(str1), len(str2)
    result = ''
    
    
    max_len = max(len1, len2)
    #running program till the max length of given strings
    #
    for i in range(max_len):
        if i < len1:
            result += str1[i]
        if i < len2:
            result += str2[i]

    return result

str1 = str(input())
str2 = str(input())
output = merge_alternatively(str1, str2)
print(output)
