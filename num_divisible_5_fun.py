def function(num):
    i=1
    while i<=num:
        if i%num:
            print(i,"*",num,"=",i*num)
        i+=1
num=int(input("enter the number:"))
function(num)