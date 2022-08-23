def function(num):
    i=0
    s=0
    a=[]
    while i<num:
        s=s+num
        a.append(s)
        i+=1
    print(a)
num=int(input("enter the number:"))
function(num)