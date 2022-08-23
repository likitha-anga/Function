# def add(list):
#     i=0
#     s=0
#     while i<len(list):
#         s=s+list[i]
#         i+=1
#     print(s)
# list = [3, 5, 7, 34, 2, 89, 2, 5]
# add(list)

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