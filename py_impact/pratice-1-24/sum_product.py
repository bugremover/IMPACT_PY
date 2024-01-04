def sum(value):
    sum1=0
    while value!=0:
        remainder=value%10;
        sum1+=remainder
        value//=10
    print(sum1)
def multi(value):
    multi1=1
    while value!=0:
        remainder=value%10;
        multi1=multi1*remainder
        value//=10
    print(multi1)
sum(12)
multi(12)

