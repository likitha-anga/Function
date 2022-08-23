def function(l):
    a=[]
    i=0
    while i<len(l):
        j=i
        while j<len(l)-1:
            c=str(l[i])+str(l[j+1])
            a.append(c)
            j=j+1
        i+=1
    print(a)
l=[4,3,2,8]
function(l)
