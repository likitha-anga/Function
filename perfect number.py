def my_function(num):
    i=1
    sum=0
    while i<num:
        if num%i==0:
            sum=sum+i
        i+=1
    if num==sum:
        print(num,"it is perfect number")
    else:
        print(num,"not a perfect number")
num=int(input("enter the number:"))
my_function(num)