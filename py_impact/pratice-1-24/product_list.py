
n = int(input())
str1 = str(n)


digits = [int(char) for char in str1]

print("Digits:", digits)

sum_even = sum(digits[1::2])
sum_odd = sum(digits[-1::2])

print("Sum of values in even places:", sum_even)
print("Sum of values in odd places:", sum_odd)
