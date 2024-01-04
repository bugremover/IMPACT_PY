n=5
for i in range(1,(n*n)+1):
    if i%n ==0:
        print(i,end="\n")
    else:
        print(i,end="*")

