def function(list,list1):
    i=0
    a=[]
    while i<len(list):
        b=list[i]+list1[i]
        a.append(b)
        i+=1
    return a
s=function([2,3,4,5],[6,7,8,9])
print(s)

