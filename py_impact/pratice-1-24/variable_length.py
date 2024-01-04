
'''def printstr(args,*vargs):
    print("args:",args)
    for i in vargs:
        print(i,end='')
printstr(1,"harsha ","vardhan")
printstr(2,"sidha","artha")'''

def printstr(*vargs):
    print(len(vargs))
    for i in vargs:
        print(i)
printstr(1,2,3,4)
printstr(3,4,567)