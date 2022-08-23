def function(num):
    i=0
    while i<=num:
        if i%2==0:
            print(i,"=even")
        elif i%2!=0:
            print(i,"=odd")
        i+=1
num=int(input("enter the number:"))
function(num)