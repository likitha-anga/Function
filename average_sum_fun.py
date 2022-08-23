# def average_sum(list):
#     # list=[3,4,5]
#     i=0
#     s=0
#     while i<len(list):
#         if list[i]>0:
#             s=list[i]+s
#             average=s/len(list)
#         i+=1
#     print("sum=",s)
#     print("average=",average)
# list=[3,4,5]
# average_sum(list)


# num1=int(input("enter the number:"))
# num2=int(input("enter the number:"))
# num3=int(input("enter the number:"))
# i=0
# s=0
# while i<num1:
#     if num1>0:
#         s=s+num1+s
#         average=s/num1
#     elif num2>0:
#         s=s+num2+s
#         average=s/num2
#     elif num3>0:
#         s=s+num3+s
#         average=s/num3
#     i+=1
# print("sum",s)
# print("average",average)


def function(num1,num2,num3):
    i=0
    s=0
    while i<num1:
        if num1>0:
            s=num1+s
            average=s/num1
        elif num2>0:
            s=num2+s
            average=s/num2
        elif num3>0:
            s=num3+s
            average=s/num3
        i+=1
    print("sum",s)
    print("average",average)
num1=int(input("enter the number:"))
num2=int(input("enter the number:"))
num3=int(input("enter the number:"))
function(num1,num2,num3)