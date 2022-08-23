def function(num):
    # num=int(input("Enter the number:"))
    i=0
    while i<=3:
        if i%2==0:
            print(i,"even")
        else:
            print(i,"odd")
        i+=1
num=int(input("Enter the number:"))
function(num)
