n=int(input())
if n ==1:
  print("1 is not a prime number")
count=0;
for i in range(2,n):
    if n%i==0:
      count=count+1
if count==0:
   print("prime number")
else:
   print("not prime")   

   