n=1
while n<=10:
    print("square of",n,"is",n*n)
    n=n+1

n=1
while n<=10:
    print("cube of",n,"is",n*n*n)
    n=n+1

sum =0
print("please enter 10 numbers\n")
i=1
while(i<=10):
    num=int(input("number%d="%i))
    sum=sum+num
    i=i+1
    avg=sum/10
    print("the sum of 10 number =",sum)
    print("the average of 10 number=",avg)