# list1 = [2, -7, 5, -64, -14]
# Output: pos = 2, neg = 3

# list1 = [2, -7, 5, -64, -14]
def function(list):
    i=0
    a=[]
    b=[]
    c=0
    c1=0
    while i<len(list):
        if list[i]<1:
            d=list[i]
            a.append(d)
            c+=1 
        elif list[i]>1:
            e=list[i]
            b.append(e)
            c1+=1
        i+=1
    print("negative=",c)
    print("positive=",c1)
function([2, -7, 5, -64, -14])
             
